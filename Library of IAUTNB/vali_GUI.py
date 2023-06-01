from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys



mylblfont = QFont('B Nazanin', 13, QFont.Bold)
titlefont = QFont('B Mitra', 20, QFont.Bold)
# rx = QRegExp("[[0-9]*[a-z0]*[A-Z]*]*")
# validator = QRegExpValidator(rx)

app = QApplication(sys.argv)
window = QDialog()
window.setGeometry(200,100,1000,500)
window.setWindowTitle('دانشگاه آزاد اسلامی واحد تهران شمال')
window.setWindowIcon(QIcon('./Icon/icon.png'))

pixmap = QPixmap('./Icon/Tehranshomallogo.png')
logo = QLabel(window)
logo.move(900,0)
logo.resize(80,150)
logo.setPixmap(pixmap.scaled(logo.size(), Qt.IgnoreAspectRatio))

lbltitle = QLabel(window)
lbltitle.move(280,50)
lbltitle.setFont(titlefont)
lbltitle.setText('سیستم جامع کتابخانه دانشگاه آزاد اسلامی\n واحد تهران شمال')
lbltitle.setAlignment(Qt.AlignCenter)
lbltitle.adjustSize()

lbluser = QLabel(window)
lbluser.move(520,250)
lbluser.setFont(mylblfont)
lbluser.setText('نام کاربری:')
lbluser.setAlignment(Qt.AlignLeft)
lbluser.adjustSize()

lblpass = QLabel(window)
lblpass.move(520,280)
lblpass.setFont(mylblfont)
lblpass.setText('رمز عبور:')
lblpass.setAlignment(Qt.AlignLeft)
lblpass.adjustSize()


qleuser = QLineEdit(window)
qleuser.move(370,255)
qleuser.setText('')
username = qleuser.text()
qleuser.setFrame(False)
# qleuser.setValidator(validator)

qlepass = QLineEdit(window)
qlepass.move(370,285)
qlepass.setText('')
password = qlepass.text()
qlepass.setFrame(False)
qlepass.setEchoMode(QLineEdit.Password)
# qlepass.setValidator(validator)


qpb = QPushButton(window)
qpb.setText('ورود')
qpb.setFont(mylblfont)
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
qpb.pressed.connect()






window.show()
app.exec()
