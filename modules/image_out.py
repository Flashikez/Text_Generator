import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas, FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
def show(image,cmap='gray',c_min = 0,c_max = 255):

	plt.imshow(image)
	plt.show()
# RGBA IMAGE -> *GRAYSCALE* -> PLT FIGURE -> *RGBA* ->  PIL IMAGE OUT


def pltFigureAsImg(image,cmap='gray',c_min = 0,c_max = 255):
	fig = Figure(figsize=(5, 5), dpi=100)
	canvas = FigureCanvasAgg(fig)
	ax = fig.add_subplot(111)
	ax.imshow(image)
	canvas.draw()
	# fig.show()
	s, (width, height) = canvas.print_to_buffer()
	from PIL import Image
	im = Image.frombytes("RGBA", (width, height), s)
	return im

