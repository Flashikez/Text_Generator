# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogSave.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage

import modules.generator as generator

class Ui_Dialog(object):
    def __init__(self,settings):
        self.settings = settings

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 491)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 391, 382))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.cmbBoxFormat = QtWidgets.QComboBox(self.layoutWidget)
        self.cmbBoxFormat.setObjectName("cmbBoxFormat")
        self.cmbBoxFormat.addItem("",QImage.Format_Grayscale8)
        self.cmbBoxFormat.addItem("",QImage.Format_Grayscale16)
        self.cmbBoxFormat.addItem("",QImage.Format_Mono)
        self.cmbBoxFormat.addItem("",QImage.Format_RGBA64)
        self.cmbBoxFormat.addItem("",QImage.Format_RGB32)
        self.cmbBoxFormat.addItem("",QImage.Format_RGB16)
        self.cmbBoxFormat.addItem("",QImage.Format_ARGB32)
        self.cmbBoxFormat.addItem("",QImage.Format_RGB666)
        self.cmbBoxFormat.addItem("",QImage.Format_RGB555)
        self.cmbBoxFormat.addItem("",QImage.Format_RGB888)
        self.cmbBoxFormat.addItem("",QImage.Format_RGB444)
        self.verticalLayout_2.addWidget(self.cmbBoxFormat)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.cmbBoxFormat_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.cmbBoxFormat_2.setObjectName("cmbBoxFormat_2")
        self.cmbBoxFormat_2.addItem("",".jpg")
        self.cmbBoxFormat_2.addItem("",".jpeg")
        self.cmbBoxFormat_2.addItem("",".bmp")
        self.cmbBoxFormat_2.addItem("",".png")
        self.cmbBoxFormat_2.addItem("",".ppm")
        self.cmbBoxFormat_2.addItem("",".xbm")
        self.cmbBoxFormat_2.addItem("",".xpm")
        self.verticalLayout_6.addWidget(self.cmbBoxFormat_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.btnFolder = QtWidgets.QPushButton(self.layoutWidget)
        self.btnFolder.setObjectName("btnFolder")
        self.verticalLayout.addWidget(self.btnFolder)
        self.lineEdit_Selected_Folder = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_Selected_Folder.setEnabled(False)
        self.lineEdit_Selected_Folder.setObjectName("lineEdit_Selected_Folder")
        self.verticalLayout.addWidget(self.lineEdit_Selected_Folder)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.spinBox_train = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_train.setObjectName("spinBox_train")
        self.spinBox_train.setMaximum(100000000)

        self.verticalLayout_4.addWidget(self.spinBox_train)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.spinBox_test = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_test.setObjectName("spinBox_test")
        self.spinBox_test.setMaximum(100000000)
        self.verticalLayout_3.addWidget(self.spinBox_test)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.btnGenerate = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnGenerate.setFont(font)
        self.btnGenerate.setObjectName("btnGenerate")
        self.verticalLayout_6.addWidget(self.btnGenerate)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_6.addWidget(self.progressBar)
        self.lbStatus = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbStatus.setFont(font)
        self.lbStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lbStatus.setObjectName("lbStatus")
        self.verticalLayout_6.addWidget(self.lbStatus)
        self.btnFolder.clicked.connect(self.choose_folder)
        self.btnGenerate.clicked.connect(self.start_Generating)
        self.folder_accepted = False
        self.retranslateUi(Dialog)
        self.spinBox_train.setValue(200)
        self.spinBox_test.setValue(50)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Formát obrázka"))
        self.cmbBoxFormat.setItemText(0, _translate("Dialog", "Grayscale8"))
        self.cmbBoxFormat.setItemText(1, _translate("Dialog", "Grayscale16"))
        self.cmbBoxFormat.setItemText(2, _translate("Dialog", "Mono (1-bit na pixel)"))
        self.cmbBoxFormat.setItemText(3, _translate("Dialog", "RGBA64"))
        self.cmbBoxFormat.setItemText(4, _translate("Dialog", "RGB32"))
        self.cmbBoxFormat.setItemText(5, _translate("Dialog", "RGB16"))
        self.cmbBoxFormat.setItemText(6, _translate("Dialog", "ARGB32"))
        self.cmbBoxFormat.setItemText(7, _translate("Dialog", "RGB666"))
        self.cmbBoxFormat.setItemText(8, _translate("Dialog", "RGB555"))
        self.cmbBoxFormat.setItemText(9, _translate("Dialog", "RGB888"))
        self.cmbBoxFormat.setItemText(10, _translate("Dialog", "RGB444"))
        self.label_9.setText(_translate("Dialog", "Prípona"))
        self.cmbBoxFormat_2.setItemText(0, _translate("Dialog", "JPG"))
        self.cmbBoxFormat_2.setItemText(1, _translate("Dialog", "JPEG"))
        self.cmbBoxFormat_2.setItemText(2, _translate("Dialog", "BMP"))
        self.cmbBoxFormat_2.setItemText(3, _translate("Dialog", "PNG"))
        self.cmbBoxFormat_2.setItemText(4, _translate("Dialog", "PPM (Portable pixmap)"))
        self.cmbBoxFormat_2.setItemText(5, _translate("Dialog", "XBM (X11 Bitmap)"))
        self.cmbBoxFormat_2.setItemText(6, _translate("Dialog", "XPM (X11 Pixmap)"))
        self.label_7.setText(_translate("Dialog", "Priečinok"))
        self.btnFolder.setText(_translate("Dialog", "Vyber priečinok"))
        self.label_8.setText(_translate("Dialog", "Počet"))
        self.label_2.setText(_translate("Dialog", "Tréning"))
        self.label_4.setText(_translate("Dialog", "Test"))
        self.btnGenerate.setText(_translate("Dialog", "Generuj"))
        self.lbStatus.setText(_translate("Dialog", "STATUS"))
        self.lbStatus.setVisible(False)
        self.progressBar.setVisible(False)

    def choose_folder(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly)
        dir = dialog.getExistingDirectory()

        if dir is '':
            self.folder_accepted = False
            self.selected_dir = "Nevybraný priečinok"
        else:
            self.selected_dir = dir
            self.folder_accepted = True
        self.lineEdit_Selected_Folder.setText(self.selected_dir)

    def map_extension(self):
        return self.cmbBoxFormat_2.currentData()

    def map_format(self):
        return self.cmbBoxFormat.currentData()

    def start_Generating(self):
        if (not self.folder_accepted):
            self.lbStatus.setText("Nezvolený priečinok")
            return

        train_num = self.spinBox_train.value()
        test_num = self.spinBox_test.value()

        if train_num == 0 and test_num==0:
            return

        train_path = self.selected_dir + "/train/"
        test_path = self.selected_dir + "/test/"
        format = self.map_format()
        extension = self.map_extension()
        if train_num is not 0 or test_num is not 0:
            self.progressBar.setMaximum(train_num+test_num)
        self.progressBar.setMinimum(0)

        if not os.path.exists(train_path):
            os.makedirs(train_path)
        if not os.path.exists(test_path):
            os.makedirs(test_path)

        self.progressBar.setVisible(True)

        for i in range(0, train_num+1):
            self.progressBar.setValue(i)
            image, text,valid = generator.generateImage(self.settings,format=format)
            image.save(f"{train_path}{text}{extension}")

        for i in range(train_num+1, train_num+test_num + 1):
            self.progressBar.setValue(i)
            image, text,valid = generator.generateImage(self.settings, format=format)
            image.save(f"{test_path}{text}{extension}")
        self.lbStatus.setVisible(True)
        self.lbStatus.setText("Generovanie dokončené")
