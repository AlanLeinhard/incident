from PyQt5 import QtCore, QtGui, QtWidgets
from subprocess import Popen, PIPE





class Global():
    output = str('')

    def call_cmd(cmd):
        proc = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True, encoding='utf-8')
        stdout, stderr = proc.communicate()
        out = stdout + stderr
        return out





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
        cmd = 'mount | grep ' + disk
        out = str(Global.call_cmd(cmd))

        out = out[out.find(' on ')+4:]
        # print(out)
        out = out[:out.find(' type'):]
        # print(out)

        # for line in out.splitlines():
        #     if line.startswith('/dev') == True:
        #         print(line + '\n')

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
        self.groupBox_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));")
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
"-webkit-transition-duration: 0.4s;\n"
"transition-duration: 0.4s;\n"
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
        self.splitter = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter.setGeometry(QtCore.QRect(30, 320, 561, 20))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.radioButton = QtWidgets.QRadioButton(self.splitter)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255)")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.splitter)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.splitter)
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255)")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.splitter)
        self.radioButton_4.setStyleSheet("color: rgb(255, 255, 255)")
        self.radioButton_4.setObjectName("radioButton_4")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(540, 40, 711, 571))
        self.tableWidget.setStyleSheet("color:white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.994975 rgba(255, 255, 255, 0))")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
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
        self.label_4.setStyleSheet("color: white; background-color: none;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 271, 81))
        self.label_2.setMinimumSize(QtCore.QSize(271, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white; background-color: none;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 110, 1281, 791))
        self.groupBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));")
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
"-webkit-transition-duration: 0.4s;\n"
"transition-duration: 0.4s;\n"
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
"-webkit-transition-duration: 0.4s;\n"
"transition-duration: 0.4s;\n"
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
        self.label_5.setStyleSheet("color: white; background-color: none;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));")
        self.label_5.setObjectName("label_5")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-290, -10, 1621, 1081))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("./ext4scanner/background.jpg"))
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
        MIAVIbyINCEDOS.setWindowTitle(_translate("MIAVIbyINCEDOS", "MIAVI by INCEDOS"))
        self.label_11.setText(_translate("MIAVIbyINCEDOS", "TextLabel"))
        self.pushButton_2.setText(_translate("MIAVIbyINCEDOS", "Далее"))
        self.label_8.setText(_translate("MIAVIbyINCEDOS", "Выбраны следующие диски:"))
        self.pushButton_3.setText(_translate("MIAVIbyINCEDOS", "Назад"))
        self.label_9.setText(_translate("MIAVIbyINCEDOS", "Выберите файловую систему для сканирования дискового пространства:"))
        self.radioButton.setText(_translate("MIAVIbyINCEDOS", "NTFS"))
        self.radioButton_2.setText(_translate("MIAVIbyINCEDOS", "Ext4"))
        self.radioButton_3.setText(_translate("MIAVIbyINCEDOS", "RadioButton"))
        self.radioButton_4.setText(_translate("MIAVIbyINCEDOS", "RadioButton"))
        self.label_4.setText(_translate("MIAVIbyINCEDOS", "ScanTool for Linux"))
        self.label_2.setText(_translate("MIAVIbyINCEDOS", "MIAVI"))
        self.pushButton_4.setText(_translate("MIAVIbyINCEDOS", "Анализ"))
        self.pushButton.setText(_translate("MIAVIbyINCEDOS", "Поиск дисков"))
        self.label_12.setText(_translate("MIAVIbyINCEDOS", "Обнаруженые следующие подключенные носители:"))
        self.label_5.setText(_translate("MIAVIbyINCEDOS", "by INCEDOS"))





        def onclick():
                cmd = ['sudo lshw -class disk']
                Global.output = str(Global.call_cmd(cmd))
                out = Global.output

                self.listWidget.clear()
                self.plainTextEdit.setPlainText(out)

                for line in out.splitlines():
                        if line.startswith('       логическое имя: ') == True:
                                info = str(line)
                                info = info[info.find('       логическое имя:'):]
                                # info = info[23:]
                                self.listWidget.addItem(info)





        def item_click():
                info = str(self.listWidget.currentItem().text())
                info = str(info[info.find('       логическое имя:'):])
                output = Global.output

                start = '  *'

                out = Global.search_for_in(start, info, output)
                self.plainTextEdit.setPlainText('')
                self.plainTextEdit.insertPlainText(out + '\n')
                self.label_11.setText(info[23:])
                self.pushButton_4.show()
                self.pushButton.hide()
                totable(Global.finddiskmount(info), self)





        def file_info(strInfo, col):
                i = 0
                for line in strInfo.splitlines():
                        self.tableWidget.setItem(i, col, QtWidgets.QTableWidgetItem(line.partition(',')[0]))
                        i+=1





        def totable(disk, self):
                self.tableWidget.clear()
                cmdDiskPath = ["df -h | grep '/dev/sdb' | awk '{print $6}'"]
                # print(cmdDiskPath)
                outputDiskPath = Global.call_cmd(cmdDiskPath).replace('\n', '')
                print(outputDiskPath)
                cmdFilePath = ['find '+outputDiskPath+' -exec stat --printf "%n \n" {} +']
                outputFilePath = Global.call_cmd(cmdFilePath)
                cmdInode = [f'find {outputDiskPath} -exec stat --printf "%i \n" {{}} +']
                outputInode = Global.call_cmd(cmdInode)
                # print(cmdFilePath)
                # print(cmdInode)
                cmdSize = [f'find {outputDiskPath} -exec stat --printf "%s \n" {{}} +']
                outputSize = Global.call_cmd(cmdSize)
                cmdAccess = [f'find {outputDiskPath} -exec stat --printf "%x \n" {{}} +']
                outputAccess = Global.call_cmd(cmdAccess)
                cmdModify = [f'find {outputDiskPath} -exec stat --printf "%y \n" {{}} +']
                outputModify = Global.call_cmd(cmdModify)
                cmdChange = [f'find {outputDiskPath} -exec stat --printf "%z \n" {{}} +']
                outputChange = Global.call_cmd(cmdChange)
                self.tableWidget.setColumnCount(6)
                self.tableWidget.setRowCount(len(outputFilePath.splitlines()))
                i = 0
                self.tableWidget.setHorizontalHeaderLabels([
                        'Путь к файлу',
                        'Инода',
                        'Размер',
                        'Дата доступа',
                        'Дата модификации',
                        'Дата изменения'
                ])
                file_info(outputFilePath, 0)
                file_info(outputInode, 1)
                file_info(outputSize, 2)
                file_info(outputAccess.replace('.',','), 3)
                file_info(outputModify.replace('.',','), 4)
                file_info(outputChange.replace('.',','), 5)
                self.tableWidget.resizeColumnsToContents()
                self.tableWidget.resizeRowsToContents()





        def anal_onclick():
                self.groupBox.hide()
                self.groupBox_2.show()





        def back_onclick():
                self.groupBox_2.hide()
                self.groupBox.show()





        self.groupBox_2.hide()
        self.pushButton_4.hide()
        # self.pushButton_2.hide()
        self.pushButton.clicked.connect(onclick)
        self.pushButton_3.clicked.connect(back_onclick)
        self.pushButton_4.clicked.connect(anal_onclick)
        self.listWidget.clicked.connect(item_click)





def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MIAVIbyINCEDOS = QtWidgets.QMainWindow()
    ui = Ui_MIAVIbyINCEDOS()
    ui.setupUi(MIAVIbyINCEDOS)
    MIAVIbyINCEDOS.show()
    sys.exit(app.exec_())





if __name__ == "__main__":
        main()
