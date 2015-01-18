from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

nsteps = 10000
vertices = {"1":  np.array([0,0]),
            "2":  np.array([1,0]),
            "3":  np.array([0.5,0.5])}

current = np.array([0.15, 0.35])
steps = np.random.choice(vertices.keys(), nsteps)
walk = np.array([vertices[step] for step in steps])
#walk = np.vstack((current, walk))

points = current[np.newaxis, ]
for vertex in walk:
    new_point = (points[-1, ] + vertex) / 2
    points = np.vstack((points, new_point))

#avg = np.frompyfunc(lambda x, y: (x + y) / 2, 2, 1)
#points = avg.accumulate(walk, dtype=np.object)

plt.scatter(points[20:,0], points[20:,1], s=5, marker='.')
plt.savefig("sierpinski.png")
#plt.show()
