from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# initializing a figure in
# which the graph will be plotted
fig = plt.figure()

# marking the x-axis and y-axis
axis = plt.axes(xlim=(0, 4), ylim=(-2, 2))

# initializing a line variable
(line,) = axis.plot([], [], lw=3)

# data which the line will
# contain (x, y)
def init():
    line.set_data([], [])
    return (line,)


def animate(i):
    x = np.linspace(0, 4, 1000)

    # plots a sine graph
    y = np.sin(2 * np.pi * (x - 0.01 * i)) * np.exp(-i * 0.003)
    line.set_data(x, y)

    return (line,)


anim = FuncAnimation(fig, animate, init_func=init, frames=2000, interval=2, blit=True)


# anim.save('continuousSineWave.mp4', writer = 'ffmpeg', fps = 30)
plt.show()
