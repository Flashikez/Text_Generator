from PyQt5 import QtWidgets



from gui.mainController import MainController
from gui.mainModel import MainModel
from gui.mainView import Ui_MainWindow






if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	view = Ui_MainWindow()
	view.setupUi(MainWindow)
	model = MainModel()
	controller = MainController(view=view,model = model)

	MainWindow.show()
	sys.exit(app.exec_())