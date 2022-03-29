from ast import For
import imp
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import subprocess

Form, Window = uic.loadUiType("script.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def onclick():
    # print(form.plainTextEdit.toPlainText())
    result = subprocess.run('ls', capture_output=True)

    form.plainTextEdit.insertPlainText(str(result) + "\n")
    form.listWidget.addItem("jhgjfhdghj")

def item_click():
    form.plainTextEdit.insertPlainText("click item:" + str(form.listWidget.currentItem().text()) + "\n")
    form.listWidget.currentItem().setText("qwertyuiop")
    # print(form.listWidget.selectedItems().mimeData())


form.pushButton.clicked.connect(onclick)
form.listWidget.clicked.connect(item_click)

app.exec_()

