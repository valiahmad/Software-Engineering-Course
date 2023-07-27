from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from numpy.random import randint
from mytime import Time


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
       
        self.L = ['نام:', 'نام خانوادگی:', 'نام پدر:', 'کد ملی:', 'تاریخ تولد:', 'شماره تلفن:',
                  'شماره دانشجویی:', 'رشته تحصیلی:', 'مقطع تحصیلی:', 'دانشکده:', 'آدرس:', 'کد پستی:']
        self.Labels = []
        self.LayLabels = []

        for i in range(2):
            self.lay = QVBoxLayout()
            self.LayLabels.append(self.lay)
            for j in range(6):
                self.lbl = QLabel()
                self.lbl.setFont(self.mylblfont)
                self.lbl.setText(self.L[j + (i * 6)])
                self.lbl.setAlignment(Qt.AlignLeft)
                self.lbl.adjustSize()
                self.Labels.append(self.lbl)
                self.LayLabels[i].addWidget(self.Labels[j + (i * 6)])
            

        ######################################
        self.LineEdits = []
        self.LayLineEdits = []
        for i in range(2):
            self.lay = QVBoxLayout()
            self.LayLineEdits.append(self.lay)
            for j in range(6):
                self.qle = QLineEdit()
                self.qle.setFrame(False)
                # self.qle.setValidator(validator)
                self.LineEdits.append(self.qle)
                self.LayLineEdits[i].addWidget(self.LineEdits[j + (i * 6)])




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
        self.layH2.addLayout(self.LayLabels[0])
        self.layH2.addLayout(self.LayLineEdits[0])
        self.layH2.addLayout(self.LayLabels[1])
        self.layH2.addLayout(self.LayLineEdits[1])
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

        self.resultWin = QDialog()
        self.resultWin.setGeometry(200,100,1000,500)
        self.resultWin.setWindowTitle('دانشگاه آزاد اسلامی واحد تهران شمال')
        self.resultWin.setWindowIcon(QIcon('./Icon/icon.png'))

        
        self.L.extend(['کد عضویت:','کد ثبت نام:','تاریخ ثبت نام:','تاریخ صدور:','تاریخ انقضاء:', ' '])

        for i in range(9,18):
            self.L.insert(i, self.LineEdits[i - 9].text())

        for i in range(27, 30):
            self.L.insert(i, self.LineEdits[i - 18].text())

        
        self.L.append(str(randint(12345, 99999)))
        self.L.append(str(randint(12345, 99999)))
        self.L.append(Time())
        self.L.append(Time())
        self.L.append(Time(year=1))
        self.L.append(' ')

        self.Labels = []
        self.LayLabels = []
        
        for i in range(4):
            self.lay = QVBoxLayout()
            self.LayLabels.append(self.lay)
            for j in range(9):
                self.lbl = QLabel()
                self.lbl.setFont(self.mylblfont)
                self.lbl.setText(self.L[j + (i * 9)])
                self.lbl.setAlignment(Qt.AlignLeft)
                self.lbl.adjustSize()
                self.Labels.append(self.lbl)
                self.LayLabels[i].addWidget(self.Labels[j + (i * 9)])
            


        self.lblsuc = QLabel('Red', self)
        self.lblsuc.setFont(self.titlefont)
        self.lblsuc.setText('عضو جدید با موفقیت ثبت شد.')
        self.lblsuc.setAlignment(Qt.AlignCenter)
        self.lblsuc.adjustSize()
        self.lblsuc.setStyleSheet('QLabel {color : green;}')
        
        
        self.qpbr = QPushButton(self)
        self.qpbr.setText('اتمام')
        self.qpbr.setFont(self.mylblfont)
        # self.qpbr.setGeometry(550, 420, 70, 30)
        self.qpbr.setStyleSheet('''
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
        self.layH1.addWidget(self.lblsuc)

        self.layH2 = QHBoxLayout()
        self.layH2.addLayout(self.LayLabels[0])
        self.layH2.addLayout(self.LayLabels[1])
        self.layH2.addLayout(self.LayLabels[2])
        self.layH2.addLayout(self.LayLabels[3])
        self.layH2.setDirection(QBoxLayout.RightToLeft)

        self.layH3 = QHBoxLayout()
        self.layH3.addWidget(self.qpbr, alignment=Qt.AlignCenter)

        self.mainlay = QVBoxLayout()
        self.mainlay.addLayout(self.layH1)
        self.mainlay.addLayout(self.layH2)
        self.mainlay.addLayout(self.layH3)
        self.mainlay.setSpacing(15)
        self.mainlay.setContentsMargins(300,0,200,0)

        self.resultWin.widget = QWidget(self.resultWin)
        self.resultWin.widget.setLayout(self.mainlay)

        self.qpbr.clicked.connect(self.closeResult)

        self.hide()
        self.resultWin.show()

        
    def closeResult(self):
        self.resultWin.close()
        self.show()

































































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

        self.lblTitle = QLabel(self)
        self.lblTitle.move(430,30)
        self.lblTitle.setFont(self.titlefont)
        self.lblTitle.setText('تمدید عضویت')
        self.lblTitle.setAlignment(Qt.AlignLeft)
        self.lblTitle.adjustSize()


        self.lblStdCode = QLabel(self)
        self.lblStdCode.move(680,195)
        self.lblStdCode.setFont(self.mylblfont)
        self.lblStdCode.setText('شماره دانشجویی:')
        self.lblStdCode.setAlignment(Qt.AlignLeft)
        self.lblStdCode.adjustSize()


        self.lblMemCode = QLabel(self)
        self.lblMemCode.move(380,195)
        self.lblMemCode.setFont(self.mylblfont)
        self.lblMemCode.setText('کد عضویت:')
        self.lblMemCode.setAlignment(Qt.AlignLeft)
        self.lblMemCode.adjustSize()


        self.qleStdCode = QLineEdit(self)
        self.qleStdCode.move(530,200)
        self.qleStdCode.setFrame(False)
        # self.qleStdCode.setValidator(validator)


        self.qleMemCode = QLineEdit(self)
        self.qleMemCode.move(230,200)
        self.qleMemCode.setFrame(False)
        # self.qleMemCode.setValidator(validator)


        self.qleWarning = QLabel('Red', self)
        self.qleWarning.move(430,380)
        self.qleWarning.setFont(self.mylblfont)
        self.qleWarning.setText('فرمت وارد شده اشتباه است!')
        self.qleWarning.setAlignment(Qt.AlignLeft)
        self.qleWarning.adjustSize()
        self.qleWarning.setStyleSheet('QLabel {color : red;}')
        self.qleWarning.hide()



        self.qpb = QPushButton(self)
        self.qpb.setText('جست و جو')
        self.qpb.setFont(self.mylblfont)
        self.qpb.setGeometry(550, 420, 70, 30)
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
        self.qpb.clicked.connect(self.handlePage)

        self.qpbc = QPushButton(self)
        self.qpbc.setText('بازگشت')
        self.qpbc.setFont(self.mylblfont)
        self.qpbc.setGeometry(380, 420, 70, 30)
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
        
        self.qpbc.clicked.connect(self.goBack)

    def goBack(self):
        self.close()
        self.backSignal.emit()

    def handlePage(self):
        
        self.StdCode = self.qleStdCode.text()
        self.MemCode = self.qleMemCode.text()
        self.hide()
        self.secondWin = QDialog()
        self.secondWin.setGeometry(200,100,1000,500)
        self.secondWin.setWindowTitle('دانشگاه آزاد اسلامی واحد تهران شمال')
        self.secondWin.setWindowIcon(QIcon('./Icon/icon.png'))


        # self.L = searchMember(self.StdCode, self.MemCode)
        self.L = ['نام:','نام خانوادگی:','کد ملی:','تاریخ تولد:','محمد','محمدی',
                  '9999999999','1380/01/01','شماره دانشجویی:','تاریخ ثبت نام:','تاریخ انقضاء:',
                  ' ','973005332','1402/02/01','1403/02/01',' '] # Temp
        self.Labels = []
        self.LayLabels = []

        for i in range(4):
            self.lay = QVBoxLayout()
            self.LayLabels.append(self.lay)
            for j in range(4):
                self.lbl = QLabel()
                self.lbl.setFont(self.mylblfont)
                self.lbl.setText(self.L[j + (i * 4)])
                self.lbl.setAlignment(Qt.AlignLeft)
                self.lbl.adjustSize()
                self.Labels.append(self.lbl)
                self.LayLabels[i].addWidget(self.Labels[j + (i * 4)])
            

        self.layH1 = QHBoxLayout()
        self.layH1.addLayout(self.LayLabels[0])
        self.layH1.addLayout(self.LayLabels[1])
        self.layH1.addLayout(self.LayLabels[2])
        self.layH1.addLayout(self.LayLabels[3])
        self.layH1.setDirection(QBoxLayout.RightToLeft)


        self.lblcomb = QLabel()
        self.lblcomb.setFont(self.mylblfont)
        self.lblcomb.setText('مدت تمدید:')
        self.lblcomb.setAlignment(Qt.AlignLeft)
        self.lblcomb.adjustSize()


        self.comb = QComboBox()
        self.comb.addItem('شش ماه')
        self.comb.addItem('یکسال')


        self.layH2 = QHBoxLayout()
        self.layH2.addWidget(self.lblcomb)
        self.layH2.addWidget(self.comb)
        self.layH2.setDirection(QBoxLayout.RightToLeft)



        self.qpb2 = QPushButton(self)
        self.qpb2.setText('ثبت')
        self.qpb2.setFont(self.mylblfont)
        self.qpb2.setStyleSheet('''
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



        self.qpbc2 = QPushButton(self)
        self.qpbc2.setText('انصراف')
        self.qpbc2.setFont(self.mylblfont)
        self.qpbc2.setStyleSheet('''
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




        self.layH3 = QHBoxLayout()
        self.layH3.addWidget(self.qpb2)
        self.layH3.addWidget(self.qpbc2)
        


        self.mainlay = QVBoxLayout()
        self.mainlay.addLayout(self.layH1)
        self.mainlay.addLayout(self.layH2)
        self.mainlay.addLayout(self.layH3)
        self.mainlay.setSpacing(30)
        self.mainlay.setContentsMargins(300,100,0,0)

        self.widget = QWidget(self.secondWin)
        self.widget.setLayout(self.mainlay)


        self.secondWin.show()


    def thirdWin(self):

        self.secondWin.close()
        self.resultWin = QDialog()
        self.resultWin.setGeometry(200,100,1000,500)
        self.resultWin.setWindowTitle('دانشگاه آزاد اسلامی واحد تهران شمال')
        self.resultWin.setWindowIcon(QIcon('./Icon/icon.png'))

        self.L = ['نام:', 'نام خانوادگی:', 'نام پدر:', 'کد ملی:', 'تاریخ تولد:', 'شماره تلفن:',
                  'شماره دانشجویی:', 'رشته تحصیلی:', 'مقطع تحصیلی:', 'دانشکده:', 'آدرس:', 'کد پستی:',
                  'کد عضویت:','کد ثبت نام:','تاریخ ثبت نام:','تاریخ صدور:','تاریخ انقضاء:', ' ']
        
        #################################
        # =========> DATABASE
        #################################

        # for i in range(9,18):
        #     self.L.insert(i, self.LineEdits[i - 9].text())

        # for i in range(27, 30):
        #     self.L.insert(i, self.LineEdits[i - 18].text())

        self.L.append(' ')

        self.Labels = []
        self.LayLabels = []
        
        for i in range(4):
            self.lay = QVBoxLayout()
            self.LayLabels.append(self.lay)
            for j in range(9):
                self.lbl = QLabel()
                self.lbl.setFont(self.mylblfont)
                self.lbl.setText(self.L[j + (i * 9)])
                self.lbl.setAlignment(Qt.AlignLeft)
                self.lbl.adjustSize()
                self.Labels.append(self.lbl)
                self.LayLabels[i].addWidget(self.Labels[j + (i * 9)])
            


        self.lblsuc = QLabel('Red', self)
        self.lblsuc.setFont(self.titlefont)
        self.lblsuc.setText('تمدید با موفقیت ثبت شد.')
        self.lblsuc.setAlignment(Qt.AlignCenter)ko
        self.lblsuc.adjustSize()
        self.lblsuc.setStyleSheet('QLabel {color : green;}')
        
        
        self.qpbr = QPushButton(self)
        self.qpbr.setText('اتمام')
        self.qpbr.setFont(self.mylblfont)
        # self.qpbr.setGeometry(550, 420, 70, 30)
        self.qpbr.setStyleSheet('''
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
        self.layH1.addWidget(self.lblsuc)

        self.layH2 = QHBoxLayout()
        self.layH2.addLayout(self.LayLabels[0])
        self.layH2.addLayout(self.LayLabels[1])
        self.layH2.addLayout(self.LayLabels[2])
        self.layH2.addLayout(self.LayLabels[3])
        self.layH2.setDirection(QBoxLayout.RightToLeft)

        self.layH3 = QHBoxLayout()
        self.layH3.addWidget(self.qpbr, alignment=Qt.AlignCenter)

        self.mainlay = QVBoxLayout()
        self.mainlay.addLayout(self.layH1)
        self.mainlay.addLayout(self.layH2)
        self.mainlay.addLayout(self.layH3)
        self.mainlay.setSpacing(15)
        self.mainlay.setContentsMargins(300,0,200,0)

        self.resultWin.widget = QWidget(self.resultWin)
        self.resultWin.widget.setLayout(self.mainlay)

        self.qpbr.clicked.connect(self.closeResult)

        self.hide()
        self.resultWin.show()

        
    def closeResult(self):
        self.resultWin.close()
        self.show()



    def closeSecondWin(self):
        self.secondWin.close()
        self.show()






































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
