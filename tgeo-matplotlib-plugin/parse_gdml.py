from lxml import etree
import numpy as np


from matplotlib_plugin import plot_box, rotation_matrix

filename = 'test.gdml'

with open(filename) as f:
  doc = etree.parse(f)
root = doc.getroot()

world, = root.xpath('/gdml/setup/world')
world_ref = world.get('ref')
world_volume, = root.xpath('/gdml/structure/volume[@name="%s"]' % (world_ref))

extracted_shapes = []
pos = []

def position2trafo(position, trafo):
    values = [float(position.get('x')), float(position.get('y')),
         float(position.get('z'))]
    if position.get('unit') == 'cm':
      values = [1 * pp for pp in values]
    p = np.array(values)
    tmptrafo = np.eye(4)
    tmptrafo[:3, -1] = p
    trafo = np.dot(tmptrafo, trafo)
    return trafo


def rotation2trafo(rotation, trafo):
    p = [float(rotation.get('x')), float(rotation.get('y')),
         float(rotation.get('z'))]
    if rotation.get('unit') == 'deg':
        p = [np.pi / 180. * pp for pp in p]
    rotx = np.eye(4)
    rotx[:3, :3] = rotation_matrix(np.array([1,0,0]), p[0])
    roty = np.eye(4)
    roty[:3, :3] = rotation_matrix(np.array([0,1,0]), p[1])
    rotz = np.eye(4)
    rotz[:3, :3] = rotation_matrix(np.array([0,0,1]), p[2])
    rot = np.dot(rotx, np.dot(roty, rotz))
    trafo = np.dot(rot, trafo)
    return trafo


def handle_volume(volume, trafo, ax=None):
  print trafo
  if "GenericTrackerBarrel_layer0_rod_0x24a03d0" == volume.get('name'):
    shape_ref = volume[1].get('ref')
    shapes = root.xpath('/gdml/solids/box[@name="%s"]' % (shape_ref))
    for shape in shapes:
      vec = np.array([float(shape.get('x')), float(shape.get('y')), float(shape.get('z'))])
      extracted_shapes.append(vec[:3])
      pos.append(trafo[:3, -1])
      plot_box(vec[0], vec[1], vec[2], trafo, ax)
  for physvol in volume[2:]:
    #trafo = np.eye(4)
    daughter_vol_ref = physvol.find('volumeref').get('ref')
    daughter_vol, = root.xpath('/gdml/structure/volume[@name="%s"]' % (daughter_vol_ref))

    position = None
    positionref = physvol.find('positionref')
    if positionref is not None:
      position, = root.xpath('/gdml/define/position[@name="%s"]' % (positionref.get('ref')))
    if physvol.find('position'):
      position = physvol.find('position')
    if position is not None:

      trafo = position2trafo(position, trafo)

    rotation = None
    rotationref = physvol.find('rotationref')
    if rotationref is not None:
      rotation, = root.xpath('/gdml/define/rotation[@name="%s"]' % (rotationref.get('ref')))
    if physvol.find('rotation'):
      rotation = physvol.find('rotation')
    if rotation is not None:
      trafo = rotation2trafo(rotation, trafo)

    handle_volume(daughter_vol, trafo, ax=ax)

if __name__ == "__main__":
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  trafo = np.eye(4)
  handle_volume(world_volume, trafo, ax)
  ax.set_ylim(-100,100)
  ax.set_xlim(-100,100)
  ax.set_zlim(-1000,1000)




