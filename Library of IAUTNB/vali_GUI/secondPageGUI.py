from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)


        self.setGeometry(200,100,1000,500)
        self.setWindowTitle('دانشگاه آزاد اسلامی واحد تهران شمال')
        self.setWindowIcon(QIcon('./Icon/icon.png'))
        menuFrame = QFrame(self)
        