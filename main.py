# coding:cp1251
from ast import For
from cmath import inf
import cmd
import imp
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from subprocess import Popen, PIPE

Form, Window = uic.loadUiType('script2.ui')

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

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



def onclick():
    cmd = ['sudo lshw -class disk']
    Global.output = str(Global.call_cmd(cmd))
    out = Global.output

    form.listWidget_2.clear()
    form.plainTextEdit_2.setPlainText(out)

    for line in out.splitlines():
        if line.startswith('       логическое имя: ') == True:
            info = str(line)
            info = info[info.find('       логическое имя:'):]
            # info = info[23:]
            form.listWidget_2.addItem(info)
    


def item_click():
    info = str(form.listWidget_2.currentItem().text())
    info = str(info[info.find('       логическое имя:'):])
    output = Global.output

    start = '  *'

    out = Global.search_for_in(start, info, output)
    form.plainTextEdit_2.setPlainText('')
    form.plainTextEdit_2.insertPlainText(out + '\n')



form.pushButton.clicked.connect(onclick)
form.listWidget_2.clicked.connect(item_click)

app.exec_()