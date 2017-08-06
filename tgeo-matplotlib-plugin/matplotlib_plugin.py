
""" Draw GDML volumes with matplotlib. """

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from numpy import cross, eye, dot
from scipy.linalg import expm3, norm




# http://stackoverflow.com/questions/28020874/permutation-of-values-on-numpy-array-matrix
# return the indices for all unique permutations of m-length lists with n unique objects 
def permutation_indices(m, n):
    inds = np.indices((m,) * n)
    return inds.reshape(n, -1).T


def plot_rectangle(rect, ax=None):
    vertices = [[0,1,3,2]]
    poly3d = [[tupleList[vertices[ix][iy]] for iy in range(len(vertices[ix]))] for ix in range(len(vertices))]
    #print poly3d
    rectanglePoly3D = Poly3DCollection(poly3d, facecolors='b', linewidths=1, alpha=0.5)
    ax.add_collection3d(rectanglePoly3D)



def apply_transformation(trafo, point):
    point = np.append(point, [1])
    point = np.dot(trafo, point)
    return point[:3]


def plot_box(x,y,z, trafo=None, ax=None):
    tupleList = permutation_indices(2, 3)
    #print tupleList
    box_dimensions = np.diag([x,y,z,1])
    if trafo is not None:
      tupleList = [apply_transformation(np.dot(trafo, box_dimensions), t) for t in tupleList]
    top_faces = [[0,1,3,2], [4,5,7,6]]
    side_faces =[[0,1,5,4],[1,3,7,5],[3,2,6,7],[2,0,4,6]]
    vertices = side_faces + top_faces
    poly3d = [[tupleList[vertices[ix][iy]] for iy in range(len(vertices[ix]))] for ix in range(len(vertices))]
    #ax.scatter(x,y,z)
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors='r', linewidths=1, alpha=1))

def rotation_matrix(axis, theta):
      return expm3(cross(eye(3), axis/norm(axis)*theta))

if __name__ == "__main__":


  trafo = np.zeros((4, 4))
  trafo[3, 3] = 1
  rot = rotation_matrix([1, 1, 1], 0)
  trafo[:3, :3] = rot

  #tupleList = [np.dot(rot, t) for t in tupleList]
  #print tupleList

  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  for i in range(10):
      trans = np.random.rand(3) - 0.5 
      trans = 5 * trans
      trafo[:3, -1] = trans
      plot_box(1,0.001,0.0001, trafo=trafo, ax=ax)

  ax.set_ylim(-10,10)
  ax.set_xlim(-10,10)
  ax.set_zlim(-10,10)

