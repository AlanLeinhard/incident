# coding:cp1251
from ast import For
import cmd
import time
import imp
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from subprocess import Popen, PIPE
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


def onclick():
    # cmd = ['wmic', 'logicaldisk', 'get']
    cmd = ['df -h | grep /dev/']
    # cmd = ['diskpart', '<', 'diskpart.txt']
    output = call_cmd(cmd)
    form.listWidget.clear()
    form.plainTextEdit.setPlainText(str(output) + "\n")

    i = 0
    j = 0
    for line in output.splitlines():
        # line = line.encode('cp866').decode('koi8-r')
        if line.startswith('/dev/loop') == False:
            form.listWidget.addItem(line)
    

def cmd_click():
    cmmd = form.plainTextEdit_2.toPlainText()
    form.plainTextEdit.setPlainText(str(call_cmd(cmmd)) + "\n")
    

def item_click():
    form.plainTextEdit.setPlainText(str(form.listWidget.currentItem().text()) + "\n")
    # form.listWidget.currentItem().text()
    
    # form.listWidget.currentItem().setText("qwertyuiop")


form.pushButton.clicked.connect(onclick)
# form.pushButton_2.clicked.connect(cmd_click)
form.listWidget.clicked.connect(item_click)

app.exec_()

