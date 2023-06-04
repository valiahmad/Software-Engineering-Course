from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys




class Login(QDialog):

    mylblfont = QFont('B Nazanin', 13, QFont.Bold)
    warningfont = QFont('B Mitra', 14, QFont.Bold)
    titlefont = QFont('B Mitra', 20, QFont.Bold)
    # rx = QRegExp("[[0-9]*[a-z]*[A-Z]*]*")
    # validator = QRegExpValidator(rx)

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        self.setGeometry(200,100,1000,500)
        self.setWindowTitle('دانشگاه آزاد اسلامی واحد تهران شمال')
        self.setWindowIcon(QIcon('./Icon/icon.png'))


        pixmap = QPixmap('./Icon/Tehranshomallogo.png')
        logo = QLabel(self)
        logo.move(900,0)
        logo.resize(80,150)
        logo.setPixmap(pixmap.scaled(logo.size(), Qt.IgnoreAspectRatio))


        lbltitle = QLabel(self)
        lbltitle.move(280,50)
        lbltitle.setFont(self.titlefont)
        lbltitle.setText('سیستم جامع کتابخانه دانشگاه آزاد اسلامی\n واحد تهران شمال')
        lbltitle.setAlignment(Qt.AlignCenter)
        lbltitle.adjustSize()


        lbluser = QLabel(self)
        lbluser.move(520,250)
        lbluser.setFont(self.mylblfont)
        lbluser.setText('نام کاربری:')
        lbluser.setAlignment(Qt.AlignLeft)
        lbluser.adjustSize()


        lblpass = QLabel(self)
        lblpass.move(520,280)
        lblpass.setFont(self.mylblfont)
        lblpass.setText('رمز عبور:')
        lblpass.setAlignment(Qt.AlignLeft)
        lblpass.adjustSize()


        self.qleuser = QLineEdit(self)
        self.qleuser.move(370,255)
        self.qleuser.setText('')
        self.qleuser.setFrame(False)
        # self.qleuser.setValidator(validator)


        self.qlepass = QLineEdit(self)
        self.qlepass.move(370,285)
        self.qlepass.setText('')
        self.qlepass.setFrame(False)
        self.qlepass.setEchoMode(QLineEdit.Password)
        # self.qlepass.setValidator(validator)


        self.qleWarning = QLabel('Red', self)
        self.qleWarning.move(370,400)
        self.qleWarning.setFont(self.mylblfont)
        self.qleWarning.setText('نام کاربری یا رمز عبور اشتباه است!')
        self.qleWarning.setAlignment(Qt.AlignLeft)
        self.qleWarning.adjustSize()
        self.qleWarning.setStyleSheet('QLabel {color : red;}')
        self.qleWarning.hide()



        qpb = QPushButton(self)
        qpb.setText('ورود')
        qpb.setFont(self.mylblfont)
        qpb.setGeometry(420, 320, 70, 30)
        qpb.setStyleSheet('''
                            QPushButton {
                                border: 2px solid #8f8f91;
                                border-radius: 15px;
                                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                                stop: 0 #f6f7fa, stop: 1 #dadbde);
                                min-width: 80px;
                            }

                            QPushButton:pressed {
                                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                                stop: 0 #dadbde, stop: 1 #f6f7fa);
                            }''')
        qpb.clicked.connect(self.handleLogin)


    def handleLogin(self):
        if (self.qleuser.text() == 'admin' and
            self.qlepass.text() == 'admin'):
            self.accept()
        else:
            self.qleWarning.show()



if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    login = Login()

    from secondPageGUI import MainWindow
    if login.exec_() == QDialog.Accepted:
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())