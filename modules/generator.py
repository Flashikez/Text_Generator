
import random
from PyQt5 import QtCore
from PyQt5.QtCore import QRect, QPoint
from PyQt5.QtGui import QImage, QPainter, QPen, QTransform, QFont

import modules.image_out as output

import modules.imagemodifier as imgModifier
from modules.settings_defaults import Settings


def generateText(charsequence,alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):


	def findIndex(c : chr):
		index = ord(c)
		if c.isdigit():
			index -= 48
		elif c.isupper():
			index = index - 65 + 10
		elif c.islower():
			index = index -  97+26+10

		return index


	split = charsequence.split('/')
	split = split[1:]
	string = ""
	for p in split:
		# print(p)
		s = p
		if len(p) != 1:
			s = p[1:-1]
		# print(s)
		# SINGLE CHAR , NON RANDOM
		if len(s) == 1:
			string+=s
			continue
		# sekvencia napr. (A-Z) , (0-9)
		elif len(s) == 3 and s[1] == '-':
			index1 = findIndex(s[0])
			index2 = findIndex(s[2])
			if( index1 < index2):
				rand = random.randrange(index1, index2+1)
				char = alphabet[rand]
				string+=char
			elif (index1 > index2):
				firstHalf = alphabet[index1:]
				secondHalf = alphabet[:index2]
				join = firstHalf+secondHalf
				rand = random.randrange(0,len(join)+1)
				string+= join[rand]
			else:
				string+=s[0]

		else:
			string+= '!'
	# print(string)
	return string


def rotatedPoint(point,center_of_rotation,angle):

	trans = QTransform()
	trans.translate(center_of_rotation.x(),center_of_rotation.y())
	trans.rotate(angle)
	trans.translate(-center_of_rotation.x(),-center_of_rotation.y())
	return trans.map(point)


def generate_Random_Shifts_Stay_in_bounds(rect,settings,angle):
	maxShiftDown, maxShiftUp = 0, 0
	maxShiftLeft, maxShiftRight = 0, 0
	#BOTTOMLEFT A TOPRIGHT URCUJU POSUN HORE AK JE ANGLE ZAPORNY, bottomright a topleft urcuju posun doprava dolava
	# U ANGLE KLADNEHO NAOPAK
	if angle < 0:
		# Posun dole,hore
		# Dole
		bottomLeftRotated = rotatedPoint(rect.bottomLeft(), rect.center(), angle)
		# print(bottomLeftRotated)
		maxShiftDown = settings.res_height - bottomLeftRotated.y()

		# Hore
		topRight = rotatedPoint(rect.topRight(), rect.center(), angle)
		maxShiftUp = topRight.y()

		# 	Posun doprava dolava
		bottomRightRotated = rotatedPoint(rect.bottomRight(), rect.center(), angle)
		maxShiftRight = settings.res_width - bottomRightRotated.x()

		topLeftRotated = rotatedPoint(rect.topLeft(), rect.center(), angle)
		maxShiftLeft = topLeftRotated.x()
	else:
		# Posun dole,hore
		# Dole
		bottomRightRotated = rotatedPoint(rect.bottomRight(), rect.center(), angle)
		maxShiftDown = settings.res_height - bottomRightRotated.y()

		# Hore
		topLeftRotated = rotatedPoint(rect.topLeft(), rect.center(), angle)
		maxShiftUp = topLeftRotated.y()

		# 	Posun doprava dolava
		topRight = rotatedPoint(rect.topRight(), rect.center(), angle)
		maxShiftRight = settings.res_width - topRight.x()

		bottomLeftRotated = rotatedPoint(rect.bottomLeft(), rect.center(), angle)
		maxShiftLeft = bottomLeftRotated.x()


	# print('Max shift up: ',maxShiftUp)
	# print('Max shift down: ', maxShiftUp)
	# print('Max shift left: ', maxShiftUp)
	# print('Max shift right: ', maxShiftUp)

	offY = random.randrange(-maxShiftUp + settings.border_width, maxShiftDown - settings.border_width + 1)
	offX = random.randrange(-maxShiftLeft + settings.border_width, maxShiftRight - settings.border_width + 1)
	print(offX,offY)
	return offX, offY

def boundingRect(settings,text,painter,angle):
	"""Na základe rozlíšenia a veľkosti fontu, dĺžky text vráti bounding Rectangle textu
	, Výška a Šírka QRectu, je nastavená na 1, pretože tá sa doráta automaticky """

	rect = painter.boundingRect(QRect(0,0,1,1),0,text)
	# print('Width: ',settings.res_width,'height: ',settings.res_height)
	# print(settings.border_width)

	if rect.width()+settings.border_width >= settings.res_width:
		return QRect(0,0,1,1), False
	elif rect.height()+settings.border_width >= settings.res_height:
		return QRect(0,0,1,1),False

	centerX = settings.res_width//2
	centerY = settings.res_height//2


	rect.moveCenter(QPoint(centerX, centerY))
	if settings.repositionText:
		offX,offY = generate_Random_Shifts_Stay_in_bounds(rect,settings,angle)
		print(centerX+offX,centerY+offY)
		rect.moveCenter(QPoint(centerX+offX,centerY+offY))

	centerPoint = rect.center()
	painter.translate(centerPoint)

	painter.rotate(angle)
	painter.translate(-centerPoint)
	return rect,True


def generateAngle():
	"""Vráti náhodný uhol o ktorý bude text rotovaný"""
	return random.randrange(-90,90)


def generateImage(settings:Settings,format = QImage.Format_RGBA64):
	"""QImage, generovaný náhodný obrázok so zvolenými nastaveniami"""
	image = QImage(settings.res_width,settings.res_height, format)
	image.fill(settings.bg_color)

	painter = QPainter()
	painter.begin(image)

	if settings.antiAliasedFont:
		settings.font.setStyleStrategy(QFont.PreferAntialias)
		painter.setRenderHint(QPainter.TextAntialiasing)
	else:
		settings.font.setStyleStrategy(QFont.NoAntialias)




	painter.setFont(settings.font)

	text = generateText(settings.text_seq)

	if settings.rotateText:
		angle = generateAngle()
	else: angle = 0


	rect,valid = boundingRect(settings, text, painter,angle)

	if not valid:
		return image,text,False

	if settings.border:
		painter.setPen(QPen(settings.border_color,settings.border_width))

		painter.drawRect(rect)
	if settings.fill:
		painter.fillRect(rect,settings.fill_color)

	painter.setPen(QPen(settings.font_color))
	painter.drawText(rect, QtCore.Qt.AlignCenter, text)
	painter.end()
	return image,text,True




def makeQsample(settings):
	"""Vráti QImage, vytvorený PLT Graf z náhodneho generovaného obrázka z nastavení"""
	generated,text,valid = generateImage(settings)

	if not valid:
		return generated,False

	pImage = imgModifier.convert_QImage_to_PILImage(generated)
	figure = output.pltFigureAsImg(pImage)
	# figure = imgModifier.convert_PLTImage_to_QImage(figure)
	return figure,True




	# text = 'TEST'
	# font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 50)
	# width, height = font.getsize(text)
	#
	# image1 = Image.new('RGBA', (200, 150), (0, 128, 0, 255))
	# # draw1 = ImageDraw.Draw(image1)
	# # draw1.text((0, 0), text="TEXT1", font=font, fill=(255, 128, 0))
	#
	# image2 = Image.new('RGBA', (width, height), (0, 0, 128, 0))
	# draw2 = ImageDraw.Draw(image2)
	# draw2.text((0, 0), text=text, font=font, fill=(0, 255, 128))
	#
	# image2 = image2.rotate(30, expand=1)
	#
	# px, py = 10, 10
	# sx, sy = image2.size
	# image1.paste(image2, (px, py, px + sx, py + sy), image2)
	#
	# image1.show()
	#


