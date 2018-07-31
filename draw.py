import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()

fig.show()
fig.canvas.draw()


def fun(x):
	return np.exp(x/10) + np.sin(x) + np.random.normal(0, .1)


def fun2(x):
	return np.sin(.1*x) + .1 * np.cos(10 * x) + np.random.normal(0, .02, len(x))


def cycle_graph():
	li = ['r', 'b', 'g', 'c', 'y']
	j = 0

	while True:
		ax.clear()
		vals = [[-10, fun(-10)]]
		for i in range(-101, 300, 1):
			vals.append([i/10, fun(i/10)])
			n = len(vals) - 1
			ax.plot([vals[n-1][0], vals[n][0]], [vals[n-1][1], vals[n][1]], c=li[j])
			fig.canvas.draw()
		j = (j + 1) % len(li)


def moving_graph():
	n = 10000
	x = np.arange(n) / 20
	a = round(.1 * n / 10) - 10
	forward = False
	colors = ['r', 'b', 'g', 'c', 'y']
	col = -1
	while True:
		forward = not forward
		col = (col + 1) % len(colors)
		for i in range(a):
			ax.clear()
			j = i if forward else a - i
			x_temp = x[(x < j + 10) & (x > j)]
			ax.plot(x_temp, fun2(x_temp), c=colors[col])
			plt.ylim((-1.1, 1.1))
			fig.canvas.draw()


cycle_graph()
# moving_graph()
