# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'script2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MIAVIbyINCEDOS(object):
    def setupUi(self, MIAVIbyINCEDOS):
        MIAVIbyINCEDOS.setObjectName("MIAVIbyINCEDOS")
        MIAVIbyINCEDOS.resize(1392, 863)
        MIAVIbyINCEDOS.setMinimumSize(QtCore.QSize(1035, 678))
        MIAVIbyINCEDOS.setAcceptDrops(False)
        MIAVIbyINCEDOS.setAutoFillBackground(False)
        MIAVIbyINCEDOS.setStyleSheet("background-color: #171717\n"
"")
        MIAVIbyINCEDOS.setIconSize(QtCore.QSize(50, 50))
        MIAVIbyINCEDOS.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MIAVIbyINCEDOS)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-20, 10, 271, 81))
        self.label_2.setMinimumSize(QtCore.QSize(271, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white\n"
"")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 70, 81, 16))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 10, 771, 81))
        self.label_4.setMinimumSize(QtCore.QSize(771, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 110, 1281, 791))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(670, 620, 231, 51))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setAcceptDrops(False)
        self.pushButton_5.setAccessibleName("")
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 53, 56);\n"
"border-color: rgb(93, 0, 1);\n"
"border-radius: 25px 25px;\n"
"-webkit-transition-duration: 0.4s;\n"
"transition-duration: 0.4s;\n"
"hover {\n"
"    background-color: #4CAF50; /* Green */\n"
"    color: white;}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(420, 620, 231, 51))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setAccessibleName("")
        self.pushButton.setStyleSheet("background-color: rgb(255, 53, 56);\n"
"border-color: rgb(93, 0, 1);\n"
"border-radius: 25px 25px;\n"
"-webkit-transition-duration: 0.4s;\n"
"transition-duration: 0.4s;\n"
"hover {\n"
"    background-color: #4CAF50; /* Green */\n"
"    color: white;}")
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(700, 40, 661, 571))
        self.plainTextEdit_3.setStyleSheet("color:white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.994975 rgba(255, 255, 255, 0))")
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(30, 30, 559, 284))
        self.label_12.setMinimumSize(QtCore.QSize(419, 279))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_12.setObjectName("label_12")
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_3.setGeometry(QtCore.QRect(30, 190, 481, 192))
        self.listWidget_3.setStyleSheet("color:white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.listWidget_3.setObjectName("listWidget_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 80, 1381, 751))
        self.groupBox_2.setObjectName("groupBox_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(620, 70, 381, 421))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(30, 320, 112, 23))
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255)")
        self.radioButton.setObjectName("radioButton")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(20, 90, 67, 17))
        self.label_11.setObjectName("label_11")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 670, 231, 51))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAcceptDrops(False)
        self.pushButton_2.setAccessibleName("")
        self.pushButton_2.setStyleSheet("color: black;\n"
"background-color: rgb(255, 53, 56);\n"
"border-color: rgb(93, 0, 1);\n"
"border-radius: 25px 25px;\n"
"-webkit-transition-duration: 0.4s;\n"
"transition-duration: 0.4s;\n"
"hover {\n"
"    background-color: #4CAF50; /* Green */\n"
"    color: white;}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(420, 320, 112, 23))
        self.radioButton_4.setStyleSheet("color: rgb(255, 255, 255)")
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 320, 112, 23))
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 231, 39))
        self.label_8.setStyleSheet("color: white; font-size: 10pt")
        self.label_8.setObjectName("label_8")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(290, 320, 112, 23))
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255)")
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 670, 231, 51))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAcceptDrops(False)
        self.pushButton_3.setAccessibleName("")
        self.pushButton_3.setStyleSheet("color: black;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(93, 0, 1);\n"
"border-radius: 25px 25px;\n"
"-webkit-transition-duration: 0.4s;\n"
"transition-duration: 0.4s;\n"
"hover {\n"
"    background-color: #4CAF50; /* Green */\n"
"    color: black;}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(20, 270, 581, 21))
        self.label_9.setStyleSheet("color: white; font-size: 10pt")
        self.label_9.setObjectName("label_9")
        MIAVIbyINCEDOS.setCentralWidget(self.centralwidget)

        self.retranslateUi(MIAVIbyINCEDOS)
        QtCore.QMetaObject.connectSlotsByName(MIAVIbyINCEDOS)

    def retranslateUi(self, MIAVIbyINCEDOS):
        _translate = QtCore.QCoreApplication.translate
        MIAVIbyINCEDOS.setWindowTitle(_translate("MIAVIbyINCEDOS", "MIAVI by INCEDOS"))
        self.label_2.setText(_translate("MIAVIbyINCEDOS", "MIAVI"))
        self.label_3.setText(_translate("MIAVIbyINCEDOS", "by INCEDOS"))
        self.label_4.setText(_translate("MIAVIbyINCEDOS", "ScanTool for Linux"))
        self.pushButton_5.setText(_translate("MIAVIbyINCEDOS", "Анализ"))
        self.pushButton.setText(_translate("MIAVIbyINCEDOS", "Поиск дисков"))
        self.label_12.setText(_translate("MIAVIbyINCEDOS", "Обнаруженые следующие подключенные носители:"))
        self.groupBox_2.setTitle(_translate("MIAVIbyINCEDOS", "GroupBox"))
        self.radioButton.setText(_translate("MIAVIbyINCEDOS", "NTFS"))
        self.label_11.setText(_translate("MIAVIbyINCEDOS", "TextLabel"))
        self.pushButton_2.setText(_translate("MIAVIbyINCEDOS", "Далее"))
        self.radioButton_4.setText(_translate("MIAVIbyINCEDOS", "RadioButton"))
        self.radioButton_2.setText(_translate("MIAVIbyINCEDOS", "Ext4"))
        self.label_8.setText(_translate("MIAVIbyINCEDOS", "Выбраны следующие диски:"))
        self.radioButton_3.setText(_translate("MIAVIbyINCEDOS", "RadioButton"))
        self.pushButton_3.setText(_translate("MIAVIbyINCEDOS", "Назад"))
        self.label_9.setText(_translate("MIAVIbyINCEDOS", "Выберите файловую систему для сканирования дискового пространства:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MIAVIbyINCEDOS = QtWidgets.QMainWindow()
    ui = Ui_MIAVIbyINCEDOS()
    ui.setupUi(MIAVIbyINCEDOS)
    MIAVIbyINCEDOS.show()
    sys.exit(app.exec_())
