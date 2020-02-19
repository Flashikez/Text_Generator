from gui.mainModel import MainModel
from gui.mainView  import Ui_MainWindow
from functools import partial



class MainController:

	def __init__(self, view: Ui_MainWindow,model:MainModel):

		self._view = view
		self._model = model
		self._connectView()

	def _connectView(self):
		assert self._view is not None
		# Connect buttons
		# btn = self._view.mainWindow
		self._view.btnGenerateSample.clicked.connect(self.btnShowSampleClicked)
		self._view.btn_Font.clicked.connect(self.fontClicked)
		self._view.btn_Font_Color.clicked.connect(partial(self.colorChooseClicked,self._view.btn_SelectedColor_Font,'selectedFontColor'))
		self._view.btn_Background_Color.clicked.connect(partial(self.colorChooseClicked,self._view.btn_SelectedColor_Background,'selectedBgColor'))
		self._view.btn_Border_Color.clicked.connect(partial(self.colorChooseClicked,self._view.btn_SelectedColor_Border,'selectedBorderColor'))
		self._view.btn_Fill_Color.clicked.connect(partial(self.colorChooseClicked,self._view.btn_SelectedColor_Fill,'selectedFillColor'))
		self.btnShowSampleClicked()

	def colorChooseClicked(self,who,field):
		color = self._view.colorDialog(getattr(self._view,field))

		if color.isValid():
			setattr(self._view,field,color)
			self._view.showSelectedColor(who,color)


	def fontClicked(self):
		font,valid = self._view.fontDialog(self._view.selectedFont)
		if valid:

			self._view.selectedFont = font
			self._view.showSelectedFont(font.toString())
		else:
			self._view.showSelectedFont('Zvolený font nie je podporovaný')

	def btnShowSampleClicked(self):
		"""MAKE SETTINGS FROM FIELDS AND SHOW SAMPLE"""
		settings = self.makeSettings()


		sample,valid = self._model.makeSample(settings)
		if valid:
			self._view.showSample(sample)
		else:
			# print('laal')
			self._view.lb_ImageSample.setVisible(True)
			self._view.lb_ImageSample.setText("Veľkosť generovaného textu presahuje veľkosť rozlíšenia,znížte rozlíšenie/upravte font")

	def makeSettings(self):
		return self._view.construct_setting()














