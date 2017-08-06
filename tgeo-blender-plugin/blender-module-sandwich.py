
import bpy
from mathutils import Vector, Matrix
from collections import OrderedDict
from bpy import context
 
def makeMaterial(name, diffuse, specular, alpha):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = diffuse
    mat.diffuse_shader = 'LAMBERT' 
    mat.diffuse_intensity = 1.0 
    mat.specular_color = specular
    mat.specular_shader = 'COOKTORR'
    mat.specular_intensity = 0.5
    mat.alpha = alpha
    mat.ambient = 1
    return mat
 
def setMaterial(ob, mat):
    me = ob.data
    me.materials.append(mat)
 
def run(origin):
    # Create two materials
    gray = makeMaterial("Gray", (204 / 256., 204 / 256., 204 / 256.), (1,1,1), 1)
    red = makeMaterial('Red', (1,0,0), (1,0,0), 1)
    orange = makeMaterial("Orange", (1, 204. / 256., 0), (1, 1, 1), 1)
    green = makeMaterial("Green", ( 204. / 256., 1, 0), (1, 1, 1), 1)
    lightblue = makeMaterial("LightBlue", ( 204. / 256., 1, 1), (1, 1, 1), 1)
    darkblue = makeMaterial("DarkerBlue", ( 153. / 256., 1, 1), (1, 1, 1), 1)

    matColors = OrderedDict([ 
      #('Beryllium', gray),
      ('Carbon', red),
      ('PE', orange),
      ("Silicon-SE", green),
      ("Silicon-Mod", green),
      ("Aluminum", lightblue),
      ("Copper", darkblue),]
    )


    colors = [red, red, orange, green, lightblue, darkblue]
    totalthickness = 0
    thicknesses = {"Silicon-SE": "0.100*mm", "Silicon-Mod":"0.187*mm" , "Copper": "0.029*mm" ,'Aluminum': "0.086*mm", 'Carbon': "0.602*mm" , "PE": "0.430*mm"}
    #thicknesses = ["1*mm" ,"2*mm" ,"1*mm" ,"2*mm", "1*mm" ,"2*mm"]
    for tk in  matColors.keys():
      t = float(thicknesses[tk].replace("*mm", ""))
      bpy.ops.mesh.primitive_cube_add(location=(1., 1., 1.))
      #bpy.context.object.scale = (2, 1, t)
      bpy.ops.transform.resize(value=(68.5, 12.8, t))
      totalthickness += t
      bpy.context.object.location += Vector( (0, 0, totalthickness) )
      totalthickness += t
      setMaterial(bpy.context.object, matColors[tk])
 
if __name__ == "__main__":
    run((1,1,2))
    #bpy.ops.view3d.view_all()

    # Select objects that will be rendered
    scene = bpy.data.scenes["Scene"]
    # Create new lamp datablock
    lamp_data = bpy.data.lamps.new(name="New Lamp", type='HEMI')

    # Create new object with our lamp datablock
    lamp_object = bpy.data.objects.new(name="New Lamp", object_data=lamp_data)

    # Link lamp object to the scene so it'll appear in this scene
    scene.objects.link(lamp_object)

    # Place lamp to a specified location
    lamp_object.location = (125.0, 125.0, 125.0)

    # And finally select it make active
    lamp_object.select = True
    scene.objects.active = lamp_object

    for obj in scene.objects:
        obj.select = False
    for obj in context.visible_objects:
        if not (obj.hide or obj.hide_render):
            obj.select = True

    bpy.ops.view3d.camera_to_view_selected()
    bpy.data.cameras["Camera"].clip_end = 1000
    bpy.data.cameras['Camera'].type = 'ORTHO'
    bpy.data.cameras['Camera'].ortho_scale = 180

    bpy.data.scenes['Scene'].render.filepath = 'blender-module-sandwich.png'
    bpy.ops.render.render( write_still=True ) 



#TODO: add other needed shapes: trapezoid, cylinder, cone



# snippet to set camera:
"""
cam = bpy.data.objects['Camera']
#bpy.context.scene.render.resolution_x = 1000 #perhaps set resolution in code
#bpy.context.scene.render.resolution_y = 1000
tx = 10.0
ty = 10.0
tz = 180.0

rx = 0.0
ry = 0.0
rz = 0.0

fov = 50.0

pi = 3.14159265

scene = bpy.data.scenes["Scene"]

# Set render resolution
#scene.render.resolution_x = 480
#scene.render.resolution_y = 359

# Set camera fov in degrees
scene.camera.data.angle = fov*(pi/180.0)

# Set camera rotation in euler angles
scene.camera.rotation_mode = 'XYZ'
scene.camera.rotation_euler[0] = rx*(pi/180.0)
scene.camera.rotation_euler[1] = ry*(pi/180.0)
scene.camera.rotation_euler[2] = rz*(pi/180.0)

# Set camera translation
scene.camera.location.x = tx
scene.camera.location.y = ty
scene.camera.location.z = tz
"""
