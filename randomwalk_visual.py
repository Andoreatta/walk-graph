import matplotlib.pyplot as pyplot
from randomwalk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

pyplot.style.use('classic')
fig, ax = pyplot.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
pyplot.show()