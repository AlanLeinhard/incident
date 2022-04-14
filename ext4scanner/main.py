# coding:cp1251
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication
from subprocess import Popen, PIPE

Form, Window = uic.loadUiType('./ext4scanner/script4.ui')

app = QApplication([])
window = Window()
self = Form()
self.setupUi(window)
window.show()

class Global():
    output = str('')

    def call_cmd(cmd):
        proc = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True, encoding='utf-8')
        stdout, stderr = proc.communicate()
        out = stdout + stderr
        return out



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



def onclick():
    cmd = ['sudo lshw -class disk']
    Global.output = str(Global.call_cmd(cmd))

    self.listWidget.clear()
    self.plainTextEdit.setPlainText(Global.output)

    for line in Global.output.splitlines():
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
    info = info[23:]
    self.plainTextEdit.setPlainText('')
    self.plainTextEdit.insertPlainText(out + '\n')
    self.label_11.setText(info)
    self.pushButton_4.show()    
    totable(Global.finddiskmount(info))
    self.pushButton.hide()



def totable(disk):
    self.tableWidget.clear()
    cmdDiskPath = ["cd ",disk," && df -h | grep ", disk, " | awk '{print $6}'"]
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



def file_info(strInfo, col):
    i = 0
    for line in strInfo.splitlines():
        self.tableWidget.setItem(i, col, QtWidgets.QTableWidgetItem(line.partition(',')[0]))
        i+=1


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

app.exec_()