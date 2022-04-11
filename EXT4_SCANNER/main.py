# coding:cp1251
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from subprocess import Popen, PIPE

Form, Window = uic.loadUiType('./script3.ui')

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