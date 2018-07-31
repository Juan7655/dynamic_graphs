import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon


def func(x):
	return (x - 3) * (x - 5) * (x - 7) + 85
#def func(x_val):
#	return np.exp(.15 * x_val) + np.sin(4 * x_val)


a, b_min, b_max = 5, 6, 20  # integral limits
x = np.linspace(0, 20, 200)
y = func(x)

fig = plt.figure()
ax = fig.add_subplot(111)
bx = fig.add_subplot(111)

plt.ion()
fig.show()
fig.canvas.draw()

bx.plot(x, y, 'r', linewidth=2)

plt.figtext(0.9, 0.05, '$x$')
plt.figtext(0.1, 0.9, '$y$')

forward = False
poly, text = None, None
while True:
	forward = not forward
	if text is None:
		text = plt.figtext(0.05, 0.25, "")  # initialize text section
	for i in range(b_min * 10, b_max * 10):
		b = i / 10 if forward else (b_min + b_max) - i / 10
		# Make the shaded region
		ix = np.linspace(a, b)
		iy = func(ix)
		verts = [(a, 0)] + list(zip(ix, iy)) + [(b, 0)]
		if poly is not None:
			poly.remove()
		poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
		ax.add_patch(poly)
		ax.spines['right'].set_visible(False)
		ax.spines['top'].set_visible(False)
		ax.xaxis.set_ticks_position('bottom')

		fig.texts.remove(text)
		text = plt.figtext(.3, 0.5, s=r"$\int_a^b f(x)\mathrm{d}x=$ " + r"$\int_{" + str(round(a, 2)) + "}^{"
		                              + str(round(b, 2)) + r"} f(x)\mathrm{d}x$",
		                   horizontalalignment='center', fontsize=15)
		ax.set_xticks((a, b))
		ax.set_xticklabels(('$a$', '$b$'))
		ax.set_yticks([])
		fig.canvas.draw()
