from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


wintitle = "Sketchpad (Alpha)"


class warningdialog(QDialog):
    def warndialogue():
      message = QMessageBox()
      message.setWindowTitle("Alpha Warning")
      message.setText("Please Note this is Early Software, Some features have not been implemeneted yet")
      message.setIcon(QMessageBox.Warning)
      message.setStandardButtons(QMessageBox.Ok)
      message.exec_()

class mainwin(QMainWindow):

  def main():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle(wintitle)
    window.setFixedSize(QSize(800, 500))
    window.show()

    warningdialog.warndialogue()
      
      
    layout = QHBoxLayout()
    window.setLayout(layout)

    app.exec()

