from ast import For
# import imp
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication
from subprocess import Popen, PIPE

from pyparsing import line
# from subprocess import PIPE

Form, Window = uic.loadUiType("script.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def call_cmd(cmd):
    proc = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True, encoding='utf-8')
    stdout, stderr = proc.communicate()
    output = stdout + stderr
    return output


def file_info(strInfo, col):
    i = 0
    for line in strInfo.splitlines():
        form.tableWidget.setItem(i, col, QtWidgets.QTableWidgetItem(line.partition(',')[0]))
        i+=1
        # print(i)    

def onclick():
    # cmd = ['wmic', 'logicaldisk', 'get']
    cmdDiskList = ["df -h | grep /dev/"]
    # cmd = ['diskpart', '<', 'diskpart.txt']
    outputDisk = call_cmd(cmdDiskList)
    form.listWidget.clear()
    form.plainTextEdit.setPlainText(str(outputDisk) + "\n")
    for line in outputDisk.splitlines():
        # line = line.encode('cp866').decode('koi8-r')
        if line.startswith('/dev/loop') == False:
            form.listWidget.addItem(line)


def cmd_click():
    cmmd = form.plainTextEdit_2.toPlainText()
    form.plainTextEdit.setPlainText(str(call_cmd(cmmd)) + "\n")
    

def item_click():
    form.tableWidget.clear()
    cmdDiskPath = ["df -h | grep '/dev/sdb' | awk '{print $6}'"]
    outputDiskPath = call_cmd(cmdDiskPath).replace('\n', '')
    cmdFilePath = ['find '+outputDiskPath+' -exec stat --printf "%n \n" {} +']
    outputFilePath = call_cmd(cmdFilePath)
    cmdInode = [f'find {outputDiskPath} -exec stat --printf "%i \n" {{}} +']
    outputInode = call_cmd(cmdInode)
    # print(cmdFilePath)
    # print(cmdInode)
    cmdSize = [f'find {outputDiskPath} -exec stat --printf "%s \n" {{}} +']
    outputSize = call_cmd(cmdSize)
    cmdAccess = [f'find {outputDiskPath} -exec stat --printf "%x \n" {{}} +']
    outputAccess = call_cmd(cmdAccess)
    cmdModify = [f'find {outputDiskPath} -exec stat --printf "%y \n" {{}} +']
    outputModify = call_cmd(cmdModify)
    cmdChange = [f'find {outputDiskPath} -exec stat --printf "%z \n" {{}} +']
    outputChange = call_cmd(cmdChange)
    form.tableWidget.setColumnCount(6)
    form.tableWidget.setRowCount(len(outputFilePath.splitlines()))
    i = 0
    form.tableWidget.setHorizontalHeaderLabels([
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
    form.tableWidget.resizeColumnsToContents()
    form.tableWidget.resizeRowsToContents()
    form.plainTextEdit.setPlainText(str(form.listWidget.currentItem().text()) + "\n")


form.pushButton.clicked.connect(onclick)
# form.pushButton_2.clicked.connect(cmd_click)
form.listWidget.clicked.connect(item_click)

app.exec_()

