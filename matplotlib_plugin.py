
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

tupleList = permutation_indices(2, 3)

def plot_rectangle(rect, ax=None):
    vertices = [[0,1,3,2]]
    poly3d = [[tupleList[vertices[ix][iy]] for iy in range(len(vertices[ix]))] for ix in range(len(vertices))]
    print poly3d
    rectanglePoly3D = Poly3DCollection(poly3d, facecolors='b', linewidths=1, alpha=0.5)
    ax.add_collection3d(rectanglePoly3D)

def plot_box(box, trans=None, rot=None, ax=None):
    tupleList = permutation_indices(2, 3)
    if rot is not None:
      tupleList = [np.dot(rot, t) for t in tupleList]
    if trans is not None:
      tupleList =  trans + tupleList
    top_faces = [[0,1,3,2], [4,5,7,6]]
    side_faces =[[0,1,5,4],[1,3,7,5],[3,2,6,7],[2,0,4,6]]
    vertices = side_faces + top_faces
    poly3d = [[tupleList[vertices[ix][iy]] for iy in range(len(vertices[ix]))] for ix in range(len(vertices))]
    #ax.scatter(x,y,z)
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors='r', linewidths=1, alpha=0.5))

trans = 5
rot=None

def M(axis, theta):
    return expm3(cross(eye(3), axis/norm(axis)*theta))

rot = M([1,1,1], 0.0)
print rot.shape, tupleList.shape

tupleList = [np.dot(rot, t) for t in tupleList]
print tupleList

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(1000):
    trans = np.random.rand(3) - 0.5 
    trans = 5 * trans
    plot_box(1, ax=ax, trans=trans, rot=rot)

ax.set_ylim(-10,10)
ax.set_xlim(-10,10)
ax.set_zlim(-10,10)

