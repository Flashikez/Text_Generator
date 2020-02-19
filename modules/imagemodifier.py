import io

from PIL import Image,ImageDraw
import logging


def rotate(image, angle,resampling=None,fill=None):

	if resampling is None:
		return image.rotate(angle, expand=1,fillcolor=fill)
	else:
		return image.rotate(angle,resampling,expand=1,fillcolor=fill)
def stack(bottom,top,top_pos):
	Image.Image.paste(bottom, top, top_pos)  # NAHODNA POZICIA GENERUJ
	return bottom


def makeImage(res,colormode,fillColor):
	return Image.new(colormode, res, color=fillColor)

def putText(image,text,position,font,color,aliasedText=False):
	drawable =  ImageDraw.Draw(image)
	if aliasedText:
		drawable.fontmode = "1"
	# Anti-aliasing = hladke hrany = fontmodee 0
	drawable.text(position,text,font=font,fill=color)
	return image




def convert_QImage_to_PILImage(image):
	from PyQt5.QtCore import QBuffer
	try:
		buffer = QBuffer()
		buffer.open(QBuffer.ReadWrite)
		image.save(buffer, "PNG")
		return Image.open(io.BytesIO(buffer.data()))
	except :
		logging.error("convert_QImage_to_PILImage failed")



def convert_PLTImage_to_QImage(image):
	from PyQt5 import QtGui
	from PIL.ImageQt import ImageQt
	try:
		imageq = ImageQt(image)
		return  QtGui.QImage(imageq)
	except:
		logging.error("onvert_PLTImage_to_QImagee failed")