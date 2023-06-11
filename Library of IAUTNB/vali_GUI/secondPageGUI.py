from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Pages import *

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.create_gui()
        self.create_boxes()

    def create_gui(self):

        self.setGeometry(200,100,1000,500)
        self.setWindowIcon(QIcon('./Icon/icon.png'))
        self.setWindowTitle('دانشگاه آزاد اسلامی واحد تهران شمال')

        self.centralwidget = QWidget(self)
        self.centralwidget_layout = QGridLayout(self.centralwidget)

        self.staff_scroll = QScrollArea(self.centralwidget)
        self.staff_scroll.setWidgetResizable(True)
        self.centralwidget_layout.addWidget(self.staff_scroll, 0, 0)

        self.staff_scroll_content = QWidget()
        self.staff_scroll_content.setGeometry(QRect(0, 0, 1000, 200))   
        self.staff_scroll_layout = QGridLayout(self.staff_scroll_content)

        self.staff_main = QFrame(self.staff_scroll_content)
        self.staff_main_layout = QGridLayout(self.staff_main)

        self.staff_grid = QGridLayout()
        self.staff_main_layout.addLayout(self.staff_grid, 0, 0)

        self.staff_scroll_layout.addWidget(self.staff_main, 0, 0)

        self.staff_scroll.setWidget(self.staff_scroll_content)

        self.setCentralWidget(self.centralwidget)

    def create_boxes(self):
        number = 9
        columns = 3
        menu = ['افزودن عضو جدید','تمدید عضویت','جست و جوی کتاب','ثبت امانت',
                'تمدید امانت','دریافت کتاب','افزودن کتاب','گزارش','خروج']
        for x in range(number//columns):
            for y in range(columns):
                staff_sub = QGroupBox()
                staff_sub.setFixedSize(250, 130)
                self.staff_grid.addWidget(staff_sub, x, y)

                layout = QHBoxLayout()
                staff_sub.setLayout(layout)

                icon = QPixmap('./Icon/' + str(x*columns + y + 1) + '.png')
                button = QPushButton()
                button.setIcon(QIcon(icon))
                button.setStyleSheet('''
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
                button.pressed.connect(lambda x=x, y=y: self.staff_sub_click(x*columns + y))
                layout.addWidget(button)

                lbl = QLabel()
                lbl.setText(menu[x*columns + y])
                layout.addWidget(lbl)

    def staff_sub_click(self, index):

        if index == 0:
            self.AddMember()
        elif index == 1:
            self.ExtnMember()
        elif index == 2:
            self.Search()
        elif index == 3:
            self.AddLoan()
        elif index == 4:
            self.ExtnLoan()
        elif index == 5:
            self.RecBook()
        elif index == 6:
            self.AddBook()
        elif index == 7:
            self.Report()
        elif index == 8:
            self.Exit()



    def AddMember(self):
        self.win = addMember()
        self.win.backSignal.connect(self.show)
        self.hide()
        self.win.show()
        
    def ExtnMember(self):
        self.win = extnMember()
        self.win.backSignal.connect(self.show)
        self.hide()
        self.win.show()

    def Search(self):
        self.win = search()
        self.win.backSignal.connect(self.show)
        self.hide()
        self.win.show()

    def AddLoan(self):
        self.win = addLoan()
        self.win.backSignal.connect(self.show)
        self.hide()
        self.win.show()

    def ExtnLoan(self):
        self.win = extnLoan()
        self.win.backSignal.connect(self.show)
        self.hide()
        self.win.show()

    def RecBook(self):
        self.win = recBook()
        self.win.backSignal.connect(self.show)
        self.hide()
        self.win.show()

    def AddBook(self):
        self.win = addBook()
        self.win.backSignal.connect(self.show)
        self.hide()
        self.win.show()

    def Report(self):
        self.win = report()
        self.win.backSignal.connect(self.show)
        self.hide()
        self.win.show()

    def Exit(self):
        exit()