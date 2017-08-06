import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle, Ellipse

layers = [10, 20, 30, 40]
hits = [[0.1, 1.4, 1.7], [0.1, 1.35, 1.75], [0.1, 1.3, 1.8], [1.25, 1.85]]
doublets = [[[0,0], [1,1], [2,2], [1,2], [2,1]], [[0,0], [1,1],[2,2]], [[1,0], [2,1]]]


def get_ellipse(x0, y0, x1, y1):
  center = (x0 + (x1 - x0) * 0.5, y0 + (y1 - y0) * 0.5)
  height = 2.
  d = np.array([x1 - x0, y1 - y0])
  width =  1.2 * np.linalg.norm([x1 - x0, y1 - y0])
  angle = np.arctan2(d[1], d[0]) * 180. / np.pi
  return Ellipse(xy=center, width=width, height=height, angle=angle,fill=True, alpha=0.4, color="grey")

fig, ax  = plt.subplots()
patches = []
for i in range(len(layers)):
  r = layers[i]
  phis = hits[i]
  patches.append(Circle((0,0), r, color="red", alpha=0.4, fill=False, lw=3))
  plt.plot(r * np.cos(phis), r* np.sin(phis), "o", color="black")
  if i > 0: # only iterate over layer pairs
    for indexPair in doublets[i - 1]:
      phis0 = hits[i-1]
      r0 = layers[i-1]
      x0, x1 = [r0*np.cos(phis0[indexPair[0]]), r * np.cos(phis[indexPair[1]])]
      y0, y1 = [r0*np.sin(phis0[indexPair[0]]), r * np.sin(phis[indexPair[1]])]
      patches.append(get_ellipse(x0,y0,x1,y1))
      #plt.plot([x0, x1], 
      #         [y0, y1], color="blue")

colors = 100*np.random.rand(len(patches))
#p = PatchCollection(patches, alpha=0.4)
#p.set_array(np.array(colors))
#ax.add_collection(p)
for a in patches:
  ax.add_artist(a)
ax.set_aspect('equal', 'datalim')
plt.margins(x=0.1, y=0.1)
plt.axis("off")
plt.savefig("CA-cartoon.png")


