
""" Draw GDML volumes with matplotlib. """

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def plot_box(box, ax=None,):
    vertices = [[0, 1, 2,3], [3,4,5],[0,3,4,1]]
    tupleList = zip(x, y, z)
    print tupleList



    poly3d = [[tupleList[vertices[ix][iy]] for iy in range(len(vertices[ix]))] for ix in range(len(vertices))]


