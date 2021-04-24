# Important Modules
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

from os import path
import sys

# Import UI FILE
FORM_CLASS,_  = loadUiType(path.join(path.dirname(__file__),'intro.ui'))


class MainWindow(QMainWindow,FORM_CLASS):
    def __init__(self):
        super(MainWindow,self)
        QMainWindow.__init__(self)
        self.setupUi(self)

        # Set Window Icon
        self.setWindowIcon(QIcon("imgs/skype-icon.png"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()    