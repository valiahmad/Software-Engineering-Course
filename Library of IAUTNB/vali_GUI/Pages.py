from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class addMember(QDialog):

    backSignal = pyqtSignal()
    mylblfont = QFont('B Nazanin', 13, QFont.Bold)
    warningfont = QFont('B Mitra', 14, QFont.Bold)
    titlefont = QFont('B Mitra', 20, QFont.Bold)
    # rx = QRegExp("[[0-9]*[a-z]*[A-Z]*]*")
    # validator = QRegExpValidator(rx)

    def __init__(self, parent=None):
        super(addMember, self).__init__(parent)

        self.setGeometry(200,100,1000,500)
        self.setWindowTitle('دانشگاه آزاد اسلامی واحد تهران شمال')
        self.setWindowIcon(QIcon('./Icon/icon.png'))



        # Layout Vertical
        self.layV1 = QVBoxLayout()
        self.layV2 = QVBoxLayout()
        self.layV3 = QVBoxLayout()
        self.layV4 = QVBoxLayout()

        self.lblname = QLabel()
        self.lblname.setFont(self.mylblfont)
        self.lblname.setText('نام:')
        self.lblname.setAlignment(Qt.AlignLeft)
        self.lblname.adjustSize()
        
        self.layV1.addWidget(self.lblname)

        self.lblLname = QLabel()
        self.lblLname.setFont(self.mylblfont)
        self.lblLname.setText('نام خانوادگی:')
        self.lblLname.setAlignment(Qt.AlignLeft)
        self.lblLname.adjustSize()

        self.layV1.addWidget(self.lblLname)

        self.lblFname = QLabel()
        self.lblFname.setFont(self.mylblfont)
        self.lblFname.setText('نام پدر:')
        self.lblFname.setAlignment(Qt.AlignLeft)
        self.lblFname.adjustSize()

        self.layV1.addWidget(self.lblFname)

        self.lblNCode = QLabel()
        self.lblNCode.setFont(self.mylblfont)
        self.lblNCode.setText('کد ملی:')
        self.lblNCode.setAlignment(Qt.AlignLeft)
        self.lblNCode.adjustSize()

        self.layV1.addWidget(self.lblNCode)

        self.lblBirth = QLabel()
        self.lblBirth.setFont(self.mylblfont)
        self.lblBirth.setText('تاریخ تولد:')
        self.lblBirth.setAlignment(Qt.AlignLeft)
        self.lblBirth.adjustSize()

        self.layV1.addWidget(self.lblBirth)

        self.lblPhone = QLabel()
        self.lblPhone.setFont(self.mylblfont)
        self.lblPhone.setText('شماره تلفن:')
        self.lblPhone.setAlignment(Qt.AlignLeft)
        self.lblPhone.adjustSize()

        self.layV1.addWidget(self.lblPhone)

        self.lblStdCode = QLabel()
        self.lblStdCode.setFont(self.mylblfont)
        self.lblStdCode.setText('شماره دانشجویی:')
        self.lblStdCode.setAlignment(Qt.AlignLeft)
        self.lblStdCode.adjustSize()

        self.layV3.addWidget(self.lblStdCode)

        self.lblMajor = QLabel()
        self.lblMajor.setFont(self.mylblfont)
        self.lblMajor.setText('رشته تحصیلی:')
        self.lblMajor.setAlignment(Qt.AlignLeft)
        self.lblMajor.adjustSize()

        self.layV3.addWidget(self.lblMajor)

        self.lblGlvl = QLabel()
        self.lblGlvl.setFont(self.mylblfont)
        self.lblGlvl.setText('مقطع تحصیلی:')
        self.lblGlvl.setAlignment(Qt.AlignLeft)
        self.lblGlvl.adjustSize()

        self.layV3.addWidget(self.lblGlvl)

        self.lblDep = QLabel()
        self.lblDep.setFont(self.mylblfont)
        self.lblDep.setText('دانشکده:')
        self.lblDep.setAlignment(Qt.AlignLeft)
        self.lblDep.adjustSize()

        self.layV3.addWidget(self.lblDep)

        self.lblAdd = QLabel()
        self.lblAdd.setFont(self.mylblfont)
        self.lblAdd.setText('آدرس:')
        self.lblAdd.setAlignment(Qt.AlignLeft)
        self.lblAdd.adjustSize()

        self.layV3.addWidget(self.lblAdd)

        self.lblPCode = QLabel()
        self.lblPCode.setFont(self.mylblfont)
        self.lblPCode.setText('کد پستی:')
        self.lblPCode.setAlignment(Qt.AlignLeft)
        self.lblPCode.adjustSize()

        self.layV3.addWidget(self.lblPCode)

        ######################################
        self.qlename = QLineEdit()
        self.qlename.setFrame(False)
        # self.qlename.setValidator(validator)

        self.layV2.addWidget(self.qlename)

        self.qleLname = QLineEdit()
        self.qleLname.setFrame(False)
        # self.qleLname.setValidator(validator)

        self.layV2.addWidget(self.qleLname)

        self.qleFname = QLineEdit()
        self.qleFname.setFrame(False)
        # self.qleFname.setValidator(validator)

        self.layV2.addWidget(self.qleFname)

        self.qleNCode = QLineEdit()
        self.qleNCode.setFrame(False)
        # self.qleNCode.setValidator(validator)

        self.layV2.addWidget(self.qleNCode)

        self.qleBirth = QLineEdit()
        self.qleBirth.setFrame(False)
        # self.qleBirth.setValidator(validator)

        self.layV2.addWidget(self.qleBirth)

        self.qlePhone = QLineEdit()
        self.qlePhone.setFrame(False)
        # self.qlePhone.setValidator(validator)

        self.layV2.addWidget(self.qlePhone)

        self.qleStdCode = QLineEdit()
        self.qleStdCode.setFrame(False)
        # self.qleStdCode.setValidator(validator)

        self.layV4.addWidget(self.qleStdCode)

        self.qleMajor = QLineEdit()
        self.qleMajor.setFrame(False)
        # self.Major.setValidator(validator)

        self.layV4.addWidget(self.qleMajor)

        self.qleGlvl = QLineEdit()
        self.qleGlvl.setFrame(False)
        # self.Glvl.setValidator(validator)

        self.layV4.addWidget(self.qleGlvl)

        self.qleDep = QLineEdit()
        self.qleDep.setFrame(False)
        # self.Dep.setValidator(validator)

        self.layV4.addWidget(self.qleDep)

        self.qleAdd = QLineEdit()
        self.qleAdd.setFrame(False)
        # self.Add.setValidator(validator)

        self.layV4.addWidget(self.qleAdd)

        self.qlePCode = QLineEdit()
        self.qlePCode.setFrame(False)
        # self.qlePCode.setValidator(validator)

        self.layV4.addWidget(self.qlePCode)



        # self.qleWarning = QLabel('Red', self)
        # self.qleWarning.move(430,380)
        # self.qleWarning.setFont(self.mylblfont)
        # self.qleWarning.setText('فرمت وارد شده اشتباه است!')
        # self.qleWarning.setAlignment(Qt.AlignLeft)
        # self.qleWarning.adjustSize()
        # self.qleWarning.setStyleSheet('QLabel {color : red;}')
        # self.qleWarning.hide()



        self.qpb = QPushButton(self)
        self.qpb.setText('ثبت')
        self.qpb.setFont(self.mylblfont)
        # self.qpb.setGeometry(550, 420, 70, 30)
        self.qpb.setStyleSheet('''
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



        self.qpbc = QPushButton(self)
        self.qpbc.setText('بازگشت')
        self.qpbc.setFont(self.mylblfont)
        # self.qpbc.setGeometry(380, 420, 70, 30)
        self.qpbc.setStyleSheet('''
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
        


        self.layH1 = QHBoxLayout()
        self.lblT = QLabel()
        self.lblT.setFont(self.titlefont)
        self.lblT.setText('افزودن عضو جدید')
        self.lblT.setAlignment(Qt.AlignCenter)
        self.lblT.adjustSize()
        self.layH1.addWidget(self.lblT)

        self.layH2 = QHBoxLayout()
        self.layH2.addLayout(self.layV1)
        self.layH2.addLayout(self.layV2)
        self.layH2.addLayout(self.layV3)
        self.layH2.addLayout(self.layV4)
        self.layH2.setDirection(QBoxLayout.RightToLeft)

        self.layH3 = QHBoxLayout()
        self.layH3.addWidget(self.qpb, alignment=Qt.AlignCenter)
        self.layH3.addWidget(self.qpbc, alignment=Qt.AlignCenter)

        self.mainlay = QVBoxLayout()
        self.mainlay.addLayout(self.layH1)
        self.mainlay.addLayout(self.layH2)
        self.mainlay.addLayout(self.layH3)
        self.mainlay.setSpacing(30)
        self.mainlay.setContentsMargins(250,0,150,0)

        self.widget = QWidget(self)
        self.widget.setLayout(self.mainlay)
        

        self.qpb.clicked.connect(self.handlePage)
        self.qpbc.clicked.connect(self.goBack)

    def goBack(self):
        self.close()
        self.backSignal.emit()

    def handlePage(self):
        print('addMember')

        














class extnMember(QDialog):

    backSignal = pyqtSignal()
    mylblfont = QFont('B Nazanin', 13, QFont.Bold)
    warningfont = QFont('B Mitra', 14, QFont.Bold)
    titlefont = QFont('B Mitra', 20, QFont.Bold)
    # rx = QRegExp("[[0-9]*[a-z]*[A-Z]*]*")
    # validator = QRegExpValidator(rx)

    def __init__(self, parent=None):
        super(extnMember, self).__init__(parent)

        self.setGeometry(200,100,1000,500)
        self.setWindowTitle('دانشگاه آزاد اسلامی واحد تهران شمال')
        self.setWindowIcon(QIcon('./Icon/icon.png'))



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
        self.qleWarning.move(430,380)
        self.qleWarning.setFont(self.mylblfont)
        self.qleWarning.setText('فرمت وارد شده اشتباه است!')
        self.qleWarning.setAlignment(Qt.AlignLeft)
        self.qleWarning.adjustSize()
        self.qleWarning.setStyleSheet('QLabel {color : red;}')
        self.qleWarning.hide()



        qpb = QPushButton(self)
        qpb.setText('ثبت')
        qpb.setFont(self.mylblfont)
        qpb.setGeometry(550, 420, 70, 30)
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
        qpb.clicked.connect(self.handlePage)

        qpbc = QPushButton(self)
        qpbc.setText('بازگشت')
        qpbc.setFont(self.mylblfont)
        qpbc.setGeometry(380, 420, 70, 30)
        qpbc.setStyleSheet('''
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
        
        self.qpbc.clicked.connect(self.goBack)

    def goBack(self):
        self.close()
        self.backSignal.emit()

    def handlePage(self):
        print('extnMember')








class search(QDialog):

    backSignal = pyqtSignal()
    mylblfont = QFont('B Nazanin', 13, QFont.Bold)
    warningfont = QFont('B Mitra', 14, QFont.Bold)
    titlefont = QFont('B Mitra', 20, QFont.Bold)
    # rx = QRegExp("[[0-9]*[a-z]*[A-Z]*]*")
    # validator = QRegExpValidator(rx)

    def __init__(self, parent=None):
        super(search, self).__init__(parent)

        self.setGeometry(200,100,1000,500)
        self.setWindowTitle('دانشگاه آزاد اسلامی واحد تهران شمال')
        self.setWindowIcon(QIcon('./Icon/icon.png'))



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
        self.qleWarning.move(430,380)
        self.qleWarning.setFont(self.mylblfont)
        self.qleWarning.setText('فرمت وارد شده اشتباه است!')
        self.qleWarning.setAlignment(Qt.AlignLeft)
        self.qleWarning.adjustSize()
        self.qleWarning.setStyleSheet('QLabel {color : red;}')
        self.qleWarning.hide()



        qpb = QPushButton(self)
        qpb.setText('ثبت')
        qpb.setFont(self.mylblfont)
        qpb.setGeometry(550, 420, 70, 30)
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
        qpb.clicked.connect(self.handlePage)

        qpbc = QPushButton(self)
        qpbc.setText('بازگشت')
        qpbc.setFont(self.mylblfont)
        qpbc.setGeometry(380, 420, 70, 30)
        qpbc.setStyleSheet('''
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
        
        qpbc.clicked.connect(self.goBack)

    def goBack(self):
        self.close()
        self.backSignal.emit()

    def handlePage(self):
        print('search')





class addLoan(QDialog):

    backSignal = pyqtSignal()
    mylblfont = QFont('B Nazanin', 13, QFont.Bold)
    warningfont = QFont('B Mitra', 14, QFont.Bold)
    titlefont = QFont('B Mitra', 20, QFont.Bold)
    # rx = QRegExp("[[0-9]*[a-z]*[A-Z]*]*")
    # validator = QRegExpValidator(rx)

    def __init__(self, parent=None):
        super(addLoan, self).__init__(parent)

        self.setGeometry(200,100,1000,500)
        self.setWindowTitle('دانشگاه آزاد اسلامی واحد تهران شمال')
        self.setWindowIcon(QIcon('./Icon/icon.png'))



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
        self.qleWarning.move(430,380)
        self.qleWarning.setFont(self.mylblfont)
        self.qleWarning.setText('فرمت وارد شده اشتباه است!')
        self.qleWarning.setAlignment(Qt.AlignLeft)
        self.qleWarning.adjustSize()
        self.qleWarning.setStyleSheet('QLabel {color : red;}')
        self.qleWarning.hide()



        qpb = QPushButton(self)
        qpb.setText('ثبت')
        qpb.setFont(self.mylblfont)
        qpb.setGeometry(550, 420, 70, 30)
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
        qpb.clicked.connect(self.handlePage)

        qpbc = QPushButton(self)
        qpbc.setText('بازگشت')
        qpbc.setFont(self.mylblfont)
        qpbc.setGeometry(380, 420, 70, 30)
        qpbc.setStyleSheet('''
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
        
        qpbc.clicked.connect(self.goBack)

    def goBack(self):
        self.close()
        self.backSignal.emit()

    def handlePage(self):
        print('addLoan')






class extnLoan(QDialog):

    backSignal = pyqtSignal()
    mylblfont = QFont('B Nazanin', 13, QFont.Bold)
    warningfont = QFont('B Mitra', 14, QFont.Bold)
    titlefont = QFont('B Mitra', 20, QFont.Bold)
    # rx = QRegExp("[[0-9]*[a-z]*[A-Z]*]*")
    # validator = QRegExpValidator(rx)

    def __init__(self, parent=None):
        super(extnLoan, self).__init__(parent)

        self.setGeometry(200,100,1000,500)
        self.setWindowTitle('دانشگاه آزاد اسلامی واحد تهران شمال')
        self.setWindowIcon(QIcon('./Icon/icon.png'))



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
        self.qleWarning.move(430,380)
        self.qleWarning.setFont(self.mylblfont)
        self.qleWarning.setText('فرمت وارد شده اشتباه است!')
        self.qleWarning.setAlignment(Qt.AlignLeft)
        self.qleWarning.adjustSize()
        self.qleWarning.setStyleSheet('QLabel {color : red;}')
        self.qleWarning.hide()



        qpb = QPushButton(self)
        qpb.setText('ثبت')
        qpb.setFont(self.mylblfont)
        qpb.setGeometry(550, 420, 70, 30)
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
        qpb.clicked.connect(self.handlePage)

        qpbc = QPushButton(self)
        qpbc.setText('بازگشت')
        qpbc.setFont(self.mylblfont)
        qpbc.setGeometry(380, 420, 70, 30)
        qpbc.setStyleSheet('''
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
        
        qpbc.clicked.connect(self.goBack)

    def goBack(self):
        self.close()
        self.backSignal.emit()

    def handlePage(self):
        print('extnLoan')






class recBook(QDialog):

    backSignal = pyqtSignal()
    mylblfont = QFont('B Nazanin', 13, QFont.Bold)
    warningfont = QFont('B Mitra', 14, QFont.Bold)
    titlefont = QFont('B Mitra', 20, QFont.Bold)
    # rx = QRegExp("[[0-9]*[a-z]*[A-Z]*]*")
    # validator = QRegExpValidator(rx)

    def __init__(self, parent=None):
        super(recBook, self).__init__(parent)

        self.setGeometry(200,100,1000,500)
        self.setWindowTitle('دانشگاه آزاد اسلامی واحد تهران شمال')
        self.setWindowIcon(QIcon('./Icon/icon.png'))



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
        self.qleWarning.move(430,380)
        self.qleWarning.setFont(self.mylblfont)
        self.qleWarning.setText('فرمت وارد شده اشتباه است!')
        self.qleWarning.setAlignment(Qt.AlignLeft)
        self.qleWarning.adjustSize()
        self.qleWarning.setStyleSheet('QLabel {color : red;}')
        self.qleWarning.hide()



        qpb = QPushButton(self)
        qpb.setText('ثبت')
        qpb.setFont(self.mylblfont)
        qpb.setGeometry(550, 420, 70, 30)
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
        qpb.clicked.connect(self.handlePage)

        qpbc = QPushButton(self)
        qpbc.setText('بازگشت')
        qpbc.setFont(self.mylblfont)
        qpbc.setGeometry(380, 420, 70, 30)
        qpbc.setStyleSheet('''
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
        
        qpbc.clicked.connect(self.goBack)

    def goBack(self):
        self.close()
        self.backSignal.emit()

    def handlePage(self):
        print('recBook')






class addBook(QDialog):

    backSignal = pyqtSignal()
    mylblfont = QFont('B Nazanin', 13, QFont.Bold)
    warningfont = QFont('B Mitra', 14, QFont.Bold)
    titlefont = QFont('B Mitra', 20, QFont.Bold)
    # rx = QRegExp("[[0-9]*[a-z]*[A-Z]*]*")
    # validator = QRegExpValidator(rx)

    def __init__(self, parent=None):
        super(addBook, self).__init__(parent)

        self.setGeometry(200,100,1000,500)
        self.setWindowTitle('دانشگاه آزاد اسلامی واحد تهران شمال')
        self.setWindowIcon(QIcon('./Icon/icon.png'))



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
        self.qleWarning.move(430,380)
        self.qleWarning.setFont(self.mylblfont)
        self.qleWarning.setText('فرمت وارد شده اشتباه است!')
        self.qleWarning.setAlignment(Qt.AlignLeft)
        self.qleWarning.adjustSize()
        self.qleWarning.setStyleSheet('QLabel {color : red;}')
        self.qleWarning.hide()



        qpb = QPushButton(self)
        qpb.setText('ثبت')
        qpb.setFont(self.mylblfont)
        qpb.setGeometry(550, 420, 70, 30)
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
        qpb.clicked.connect(self.handlePage)

        qpbc = QPushButton(self)
        qpbc.setText('بازگشت')
        qpbc.setFont(self.mylblfont)
        qpbc.setGeometry(380, 420, 70, 30)
        qpbc.setStyleSheet('''
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
        
        qpbc.clicked.connect(self.goBack)

    def goBack(self):
        self.close()
        self.backSignal.emit()

    def handlePage(self):
        print('addBook')





class report(QDialog):

    backSignal = pyqtSignal()
    mylblfont = QFont('B Nazanin', 13, QFont.Bold)
    warningfont = QFont('B Mitra', 14, QFont.Bold)
    titlefont = QFont('B Mitra', 20, QFont.Bold)
    # rx = QRegExp("[[0-9]*[a-z]*[A-Z]*]*")
    # validator = QRegExpValidator(rx)

    def __init__(self, parent=None):
        super(report, self).__init__(parent)

        self.setGeometry(200,100,1000,500)
        self.setWindowTitle('دانشگاه آزاد اسلامی واحد تهران شمال')
        self.setWindowIcon(QIcon('./Icon/icon.png'))



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
        self.qleWarning.move(430,380)
        self.qleWarning.setFont(self.mylblfont)
        self.qleWarning.setText('فرمت وارد شده اشتباه است!')
        self.qleWarning.setAlignment(Qt.AlignLeft)
        self.qleWarning.adjustSize()
        self.qleWarning.setStyleSheet('QLabel {color : red;}')
        self.qleWarning.hide()



        qpb = QPushButton(self)
        qpb.setText('ثبت')
        qpb.setFont(self.mylblfont)
        qpb.setGeometry(550, 420, 70, 30)
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
        qpb.clicked.connect(self.handlePage)

        qpbc = QPushButton(self)
        qpbc.setText('بازگشت')
        qpbc.setFont(self.mylblfont)
        qpbc.setGeometry(380, 420, 70, 30)
        qpbc.setStyleSheet('''
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
        
        qpbc.clicked.connect(self.goBack)

    def goBack(self):
        self.close()
        self.backSignal.emit()

    def handlePage(self):
        print('report')
