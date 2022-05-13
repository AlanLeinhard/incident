from ast import For
from time import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog, QGridLayout, QLabel, QLineEdit, QPushButton, QDialog
from subprocess import Popen, PIPE, call
import argparse
import csv
# from multiprocessing import Process


parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--install", action="store_true",
                    help="This is the 'install' variable")
args = parser.parse_args()
a = args.install

if a:
    cmd = 'sudo -i apt install python3-pyqt5 && sudo apt install python3-pip && pip install packaging==21.3 pyparsing==3.0.7 PyQt5==5.15.6 PyQt5-Qt5==5.15.2 PyQt5-sip==12.9.1 sip==6.5.1 toml==0.10.2'
    call(cmd, shell=True)


class Global():
    output = str('')

    def call_cmd(cmd):
        # print(cmd)
        dmesg = Popen(['echo', inpwd.test_var], stdout=PIPE)
        process = Popen(['sudo', '-S'] + cmd,
                        stdin=dmesg.stdout,
                        stdout=PIPE,
                        stderr=PIPE,
                        shell=False,
                        encoding='utf-8')
        dmesg.stdout.close()
        stdout, stderr = process.communicate()
        out = stdout + stderr
        return out


class Ui_MIAVIbyINCEDOS(object):
    def setupUi(self, MIAVIbyINCEDOS):
        MIAVIbyINCEDOS.setObjectName("MIAVIbyINCEDOS")
        MIAVIbyINCEDOS.resize(1316, 863)
        MIAVIbyINCEDOS.setMinimumSize(QtCore.QSize(1035, 678))
        MIAVIbyINCEDOS.setAcceptDrops(False)
        MIAVIbyINCEDOS.setAutoFillBackground(False)
        MIAVIbyINCEDOS.setStyleSheet("background-color: #171717\n"
                                     "")
        MIAVIbyINCEDOS.setIconSize(QtCore.QSize(50, 50))
        MIAVIbyINCEDOS.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MIAVIbyINCEDOS)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 110, 1381, 751))
        self.groupBox_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(20, 110, 151, 17))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
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
                                        "hover {\n"
                                        "    background-color: #4CAF50; /* Green */\n"
                                        "    color: white;}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 60, 231, 39))
        self.label_8.setStyleSheet("color: white; font-size: 10pt")
        self.label_8.setObjectName("label_8")
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
                                        "hover {\n"
                                        "    background-color: #4CAF50; /* Green */\n"
                                        "    color: black;}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(540, 40, 711, 571))
        self.tableWidget.setStyleSheet("color:white;\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.994975 rgba(255, 255, 255, 0))")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 150, 521, 301))
        self.groupBox_3.setStyleSheet("color:white;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.994975 rgba(255, 255, 255, 0))")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 250, 111, 25))
        self.pushButton_5.setStyleSheet("color:white;\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.994975 rgba(255, 255, 255, 0))")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(10, 30, 231, 21))
        self.label_10.setStyleSheet("color: white; font-size: 10pt")
        self.label_10.setObjectName("label_10")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 70, 151, 111))
        self.listWidget_2.setStyleSheet("color:white;\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.994975 rgba(255, 255, 255, 0))")
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.splitter = QtWidgets.QSplitter(self.groupBox_3)
        self.splitter.setGeometry(QtCore.QRect(250, 70, 271, 20))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.radioButton = QtWidgets.QRadioButton(self.splitter)
        self.radioButton.setEnabled(True)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255)")
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.splitter)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(280, 30, 171, 21))
        self.label_9.setStyleSheet("color: white; font-size: 10pt")
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 0, 771, 81))
        self.label_4.setMinimumSize(QtCore.QSize(771, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(
            "color: white; background-color: none;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 271, 81))
        self.label_2.setMinimumSize(QtCore.QSize(271, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(
            "color: white; background-color: none;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 110, 1281, 791))
        self.groupBox.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 670, 231, 51))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAcceptDrops(False)
        self.pushButton_4.setAccessibleName("")
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 53, 56);\n"
                                        "border-color: rgb(93, 0, 1);\n"
                                        "border-radius: 25px 25px;\n"
                                        "hover {\n"
                                        "    background-color: #4CAF50; /* Green */\n"
                                        "    color: white;}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(490, 670, 231, 51))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setAccessibleName("")
        self.pushButton.setStyleSheet("background-color: rgb(255, 53, 56);\n"
                                      "border-color: rgb(93, 0, 1);\n"
                                      "border-radius: 25px 25px;\n"
                                      "hover {\n"
                                      "    background-color: #4CAF50; /* Green */\n"
                                      "    color: white;}")
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(700, 40, 661, 571))
        self.plainTextEdit.setStyleSheet("color:white;\n"
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.994975 rgba(255, 255, 255, 0))")
        self.plainTextEdit.setObjectName("plainTextEdit")
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
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(30, 190, 481, 192))
        self.listWidget.setStyleSheet("color:white;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.listWidget.setObjectName("listWidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 40, 68, 81))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(
            "color: white; background-color: none;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));")
        self.label_5.setObjectName("label_5")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-290, -10, 1621, 1081))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(
            "/usr/share/applications/background.jpg"))
        self.background.setObjectName("background")
        self.background.raise_()
        self.groupBox_2.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.groupBox.raise_()
        MIAVIbyINCEDOS.setCentralWidget(self.centralwidget)

        self.retranslateUi(MIAVIbyINCEDOS)
        QtCore.QMetaObject.connectSlotsByName(MIAVIbyINCEDOS)

    def retranslateUi(self, MIAVIbyINCEDOS):
        _translate = QtCore.QCoreApplication.translate
        MIAVIbyINCEDOS.setWindowTitle(_translate(
            "MIAVIbyINCEDOS", "MIAVI by INCEDOS"))
        self.label_11.setText(_translate("MIAVIbyINCEDOS", "TextLabel"))
        self.pushButton_2.setText(_translate("MIAVIbyINCEDOS", "Далее"))
        self.label_8.setText(_translate(
            "MIAVIbyINCEDOS", "Выбраны следующие диски:"))
        self.pushButton_3.setText(_translate("MIAVIbyINCEDOS", "Назад"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MIAVIbyINCEDOS", "Путь к файлу"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MIAVIbyINCEDOS", "Инода"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MIAVIbyINCEDOS", "Размер"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MIAVIbyINCEDOS", "Дата доступа"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MIAVIbyINCEDOS", "Дата модификации"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MIAVIbyINCEDOS", "Дата изменения"))
        self.groupBox_3.setTitle(_translate("MIAVIbyINCEDOS", "Сортиоовка"))
        self.pushButton_5.setText(_translate("MIAVIbyINCEDOS", "Сортировать"))
        self.label_10.setText(_translate(
            "MIAVIbyINCEDOS", "Выберите столбец для сортировки:"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MIAVIbyINCEDOS", "Путь к файлу"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MIAVIbyINCEDOS", "Инода"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MIAVIbyINCEDOS", "Размер"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("MIAVIbyINCEDOS", "Дата доступа"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("MIAVIbyINCEDOS", "Дата модификации"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("MIAVIbyINCEDOS", "Дата изменения"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.radioButton.setText(_translate(
            "MIAVIbyINCEDOS", "по возрастанию"))
        self.radioButton_2.setText(_translate("MIAVIbyINCEDOS", "по убыванию"))
        self.label_9.setText(_translate(
            "MIAVIbyINCEDOS", "Выберите вид сортировки:"))
        self.label_4.setText(_translate(
            "MIAVIbyINCEDOS", "ScanTool for Linux"))
        self.label_2.setText(_translate("MIAVIbyINCEDOS", "MIAVI"))
        self.pushButton_4.setText(_translate("MIAVIbyINCEDOS", "Анализ"))
        self.pushButton.setText(_translate("MIAVIbyINCEDOS", "Поиск дисков"))
        self.label_12.setText(_translate(
            "MIAVIbyINCEDOS", "Обнаруженые следующие подключенные носители:"))
        self.label_5.setText(_translate("MIAVIbyINCEDOS", "by INCEDOS"))

        def search_for_in(start, word, text):
            i = 0
            result = False
            out = str('')
            for line in text.splitlines():
                if line.startswith(start) == True:
                    i = i + 1
                if i == 1:
                    out = out + str(line) + '\n'
                else:
                    if i == 2:
                        for strr in out.splitlines():
                            if strr.startswith(word) == True:
                                result = True
                                break
                        if not result:
                            i = i-1
                            out = str('') + str(line)
            if out != '':
                return out
            else:
                return 'error'

        def finddiskmount(disk):
            cmd = ['df', '-h']
            out = str(Global.call_cmd(cmd))
            for line in out.splitlines():
                if line.startswith(disk) == True:
                    # print(line + '\n')
                    out = line
            out = out[out.find('/media'):]
            # print(out)
            return out

        def onclick():
            cmd = ['lshw', '-class', 'disk']
            Global.output = Global.call_cmd(cmd)
            out = Global.output
            self.listWidget.clear()
            self.plainTextEdit.setPlainText(out)
            for line in out.splitlines():
                if line.startswith('       логическое имя: ') == True:
                    info = str(line)
                    info = info[info.find('       логическое имя:'):]
                    self.listWidget.addItem(info)

        def item_click():
            info = str(self.listWidget.currentItem().text())
            info = str(info[info.find('       логическое имя:'):])
            output = Global.output
            start = '  *'
            out = search_for_in(start, info, output)
            self.plainTextEdit.setPlainText('')
            self.plainTextEdit.insertPlainText(out + '\n')
            self.label_11.setText(info[23:])
            self.pushButton_4.show()
            self.pushButton.hide()

        def file_info(strInfo, col, ifint):
            i = 0
            for line in strInfo.splitlines():
                item = line.partition(',')[0]
                if ifint:
                    item = int(item)
                    # print(item)
                    # print(self.tableWidget.cellWidget(i, col))
                self.tableWidget.setItem(
                    i, col, QtWidgets.QTableWidgetItem(item))
                i += 1

        def totable(disk):
            outputDiskPath = disk
            outputInode = ''
            outputSize = ''
            outputAccess = ''
            outputModify = ''
            outputChange = ''
            cmdFilePath = ['find', outputDiskPath]
            outputFilePath = Global.call_cmd(cmdFilePath)
            for row in outputFilePath.splitlines():
                cmdInode = ['stat', '--printf', '%i \n', row]
                outputInode += Global.call_cmd(cmdInode)
                cmdSize = ['stat', '--printf', '%s \n', row]
                outputSize += Global.call_cmd(cmdSize)
                cmdAccess = ['stat', '--printf', '%x \n', row]
                outputAccess += Global.call_cmd(cmdAccess)
                cmdModify = ['stat', '--printf', '%y \n', row]
                outputModify += Global.call_cmd(cmdModify)
                cmdChange = ['stat', '--printf', '%z \n', row]
                outputChange += Global.call_cmd(cmdChange)
            self.tableWidget.clear()
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setRowCount(len(outputFilePath.splitlines()))
            self.tableWidget.setHorizontalHeaderLabels([
                'Путь к файлу',
                'Инода',
                'Размер',
                'Дата доступа',
                'Дата модификации',
                'Дата изменения'
            ])
            file_info(outputFilePath, 0, False)
            file_info(outputInode, 1, False)
            file_info(outputSize, 2, False)
            file_info(outputAccess.replace('.', ','), 3, False)
            file_info(outputModify.replace('.', ','), 4, False)
            file_info(outputChange.replace('.', ','), 5, False)
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()
            self.tableWidget.sortByColumn(3, QtCore.Qt.AscendingOrder)

        def anal_onclick():
            self.groupBox.hide()
            self.groupBox_2.show()
            info = str(self.listWidget.currentItem().text())
            info = str(info[info.find('       логическое имя:'):])
            totable(finddiskmount(self.label_11.text()))

        def back_onclick():
            self.groupBox_2.hide()
            self.groupBox.show()
            self.pushButton_4.hide()
            self.pushButton.show()

        # def openFileNameDialog():
        #         options = QFileDialog.Options()
        #         options |= QFileDialog.DontUseNativeDialog
        #         fileName, _ = QFileDialog.getOpenFileName(
        #         QWidget(), "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
        #         if fileName:
        #                 print(fileName)

        # def openFileNamesDialog():
        #         options = QFileDialog.Options()
        #         options |= QFileDialog.DontUseNativeDialog
        #         files, _ = QFileDialog.getOpenFileNames(
        #         QWidget(), "QFileDialog.getOpenFileNames()", "", "All Files (*);;Python Files (*.py)", options=options)
        #         if files:
        #                 print(files)

        def saveFileDialog():
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(
                QWidget(), "Сохранить как", "", "All Files (*);;Text Files (*.txt)", options=options)
            if fileName:
                with open(fileName, "w") as fileOutput:
                    writer = csv.writer(fileOutput)
                    for rowNumber in range(self.tableWidget.rowCount()):
                        fields = [
                            self.tableWidget.item(
                                rowNumber, columnNumber).text()
                            for columnNumber in range(self.tableWidget.columnCount())
                        ]

                        writer.writerow(fields)

        def sorting():
            if self.listWidget_2.currentRow() < 0:
                return
            testlist0 = []
            testlist1 = []
            testlist2 = []
            testlist3 = []
            testlist4 = []
            testlist5 = []
            for rowNumber in range(self.tableWidget.rowCount()):
                fields = self.tableWidget.item(rowNumber, 0).text()
                testlist0 += [fields]
                fields = self.tableWidget.item(rowNumber, 1).text()
                testlist1 += [int(fields)]
                fields = self.tableWidget.item(rowNumber, 2).text()
                testlist2 += [int(fields)]
                fields = self.tableWidget.item(rowNumber, 3).text()
                testlist3 += [fields]
                fields = self.tableWidget.item(rowNumber, 4).text()
                testlist4 += [fields]
                fields = self.tableWidget.item(rowNumber, 5).text()
                testlist5 += [fields]
            array = []
            for i in range(len(testlist2)):
                array.append([testlist0[i], testlist1[i], testlist2[i],
                             testlist3[i], testlist4[i], testlist5[i]])
            array = sorted(
                array, key=lambda x: x[self.listWidget_2.currentRow()])
            # print(array)
            if self.radioButton_2.isChecked():
                array.reverse()
            file_info2(array, len(testlist2))

        def file_info2(arr, rows):
            self.tableWidget.clear()
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setRowCount(rows)
            i = 0
            self.tableWidget.setHorizontalHeaderLabels([
                'Путь к файлу',
                'Инода',
                'Размер',
                'Дата доступа',
                'Дата модификации',
                'Дата изменения'
            ])
            i = 0
            for line in arr:
                j = 0
                for item in line:
                    # print(item, '\n')
                    self.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(str(item)))
                    j += 1
                i += 1

        self.groupBox_2.hide()  # второе окно - скрыть
        self.pushButton_4.hide()  # анализ - скрыть
        self.pushButton.clicked.connect(onclick)  # сканирование
        self.pushButton_3.clicked.connect(back_onclick)  # назад
        self.pushButton_4.clicked.connect(anal_onclick)  # анализ
        self.listWidget.clicked.connect(item_click)  # поле в листе
        self.pushButton_2.clicked.connect(
            saveFileDialog)  # далее - долбаный csv
        self.pushButton_5.clicked.connect(sorting)


class inpwd(object):
    test_var = ''

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(500, 500)
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(-20, -40, 1621, 1081))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(
            "../../../../../usr/share/applications/background.jpg"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 125, 100, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(
            "../../../../../usr/share/applications/eye.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 260, 240, 15))
        self.label_2.setStyleSheet("color:white;\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 300, 240, 31))
        self.lineEdit.setStyleSheet("color:white;\n"
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 340, 240, 15))
        self.label_3.setStyleSheet("color:white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(135, 360, 230, 50))
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
                                        "hover {\n"
                                        "    background-color: #4CAF50; /* Green */\n"
                                        "    color: white;}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Пароль"))
        self.label_2.setText(_translate(
            "Form", "Введите пароль администратора"))
        self.pushButton_2.setText(_translate("Form", "Далее"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\">неверный пароль</p></body></html>"))

        def check_pwd():
            import subprocess
            test_var = self.lineEdit.text()
            cmd = ['sudo -S echo 1']
            dmesg = subprocess.Popen(
                ['echo', test_var], stdout=subprocess.PIPE)
            process = subprocess.Popen(cmd,
                                       stdin=dmesg.stdout,
                                       stdout=PIPE,
                                       stderr=PIPE,
                                       shell=True,
                                       encoding='utf-8')
            dmesg.stdout.close()
            dmesg = subprocess.Popen(
                ['echo', test_var], stdout=subprocess.PIPE)
            process = subprocess.Popen(cmd,
                                       stdin=dmesg.stdout,
                                       stdout=PIPE,
                                       stderr=PIPE,
                                       shell=True,
                                       encoding='utf-8')
            dmesg.stdout.close()
            stdout, stderr = process.communicate()  # костыль
            out = stdout + stderr  # костыль
            # print(process.returncode)
            # out = '1'
            check = process.returncode
            # print(check)
            if not check:
                # print('done')
                # print(inpwd.test_var)
                inpwd.test_var = test_var
                open_programm()
                pass
            else:
                print('error')
                self.label_3.show()
                self.lineEdit.setStyleSheet("color:white;\n"
                                            "background-color: rgb(239, 41, 41);")
        
                pass

        def open_programm():
            global MIAVIbyINCEDOS
            Form.close()
            MIAVIbyINCEDOS = QtWidgets.QMainWindow()
            ui = Ui_MIAVIbyINCEDOS()
            ui.setupUi(MIAVIbyINCEDOS)
            MIAVIbyINCEDOS.show()
            Form.hide()

        def defolt_color_line():
            self.lineEdit.setStyleSheet("color:white;\n"
                                            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
            pass

        self.pushButton_2.clicked.connect(check_pwd)
        self.pushButton_2.setAutoDefault(True)
        self.lineEdit.textChanged.connect(defolt_color_line)
        self.label_3.hide()


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = inpwd()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
