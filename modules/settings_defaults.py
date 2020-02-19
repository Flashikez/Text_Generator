from PyQt5.QtGui import QColor, QFont





class Settings:
	def __init__(self):
		self.setDefaults()

	def set(self,h,w,seq,fc,font,bgc,border,fill,border_w,border_c,fill_c,antiAliasedFont,rotate,repos):
		self.res_height = h
		self.res_width = w
		self.text_seq = seq
		self.font_color = fc
		self.font = font
		self.bg_color = bgc
		self.border = border
		self.fill = fill
		self.border_width = border_w
		self.border_color = border_c
		self.fill_color = fill_c
		self.antiAliasedFont = antiAliasedFont
		self.repositionText = repos
		self.rotateText = rotate

	def setDefaults(self):
		self.res_height = 112
		self.res_width = 112
		self.text_seq = "/(A-Z)/(A-Z)/ /(0-9)/(0-9)/(0-9)/ /(A-Z)/(A-Z)"
		self.font_color = QColor(0, 0, 0, 255)
		self.font = QFont("Arial Black", 7)
		self.bg_color = QColor(255, 255, 255, 255)
		self.border = True
		self.fill = False
		self.border_width = 2
		self.border_color = QColor(0, 0, 0, 255)
		self.fill_color = QColor(100, 255, 255, 255)
		self.antiAliasedFont = True
		self.repositionText = True
		self.rotateText = False

	# def dump(self):
	# 	for attr in dir(self):
	# 		print("obj.%s = %r" % (attr, getattr(self, attr)))
