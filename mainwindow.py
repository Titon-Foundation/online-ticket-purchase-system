################################################################################
##
## Designed & Developed by: TONMOY PAUL
## (C) MIT LICENCE 2024
##
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTextBrowser, QWidget)

#Global Variables for the project

category_info =''
name_info = ''
id_info=''
route_info=''
time_info=''
date_info=''
seat_info= []
payment_ifo=''
fare_info = None
seat_count = None
cost_info = None

ticket_price = [500,600,300,400,550,700,350]
time_list = ['5:00 PM','4:30 PM', '5:00 PM', '5:15 PM','4:45 PM', '5:30 PM', '5:45 PM']

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(748, 721)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.status_label = QLabel(self.centralwidget)
        self.status_label.setObjectName(u"status_label")

        self.gridLayout.addWidget(self.status_label, 4, 0, 1, 1)

        self.back_btn = QPushButton(self.centralwidget)
        self.back_btn.setObjectName(u"back_btn")

        self.gridLayout.addWidget(self.back_btn, 4, 1, 1, 1)

        self.ticket_purchase = QStackedWidget(self.centralwidget)
        self.ticket_purchase.setObjectName(u"ticket_purchase")
        self.RouteSearch = QWidget()
        self.RouteSearch.setObjectName(u"RouteSearch")
        self.horizontalLayout = QHBoxLayout(self.RouteSearch)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.identity_info_box = QGroupBox(self.RouteSearch)
        self.identity_info_box.setObjectName(u"identity_info_box")
        self.gridLayout_2 = QGridLayout(self.identity_info_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.name_line_edit = QLineEdit(self.identity_info_box)
        self.name_line_edit.setObjectName(u"name_line_edit")

        self.gridLayout_2.addWidget(self.name_line_edit, 7, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 258, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 8, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.identity_selector = QComboBox(self.identity_info_box)
        self.identity_selector.addItem("")
        self.identity_selector.addItem("")
        self.identity_selector.addItem("")
        self.identity_selector.addItem("")
        self.identity_selector.setObjectName(u"identity_selector")

        self.gridLayout_2.addWidget(self.identity_selector, 1, 0, 1, 1)

        self.name_label = QLabel(self.identity_info_box)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout_2.addWidget(self.name_label, 6, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 5, 0, 1, 1)

        self.id_line_edit = QLineEdit(self.identity_info_box)
        self.id_line_edit.setObjectName(u"id_line_edit")

        self.gridLayout_2.addWidget(self.id_line_edit, 4, 0, 1, 1)

        self.identity_select_label = QLabel(self.identity_info_box)
        self.identity_select_label.setObjectName(u"identity_select_label")

        self.gridLayout_2.addWidget(self.identity_select_label, 0, 0, 1, 1)

        self.id_num_label = QLabel(self.identity_info_box)
        self.id_num_label.setObjectName(u"id_num_label")

        self.gridLayout_2.addWidget(self.id_num_label, 3, 0, 1, 1)


        self.horizontalLayout.addWidget(self.identity_info_box)

        self.transport_finder_box = QGroupBox(self.RouteSearch)
        self.transport_finder_box.setObjectName(u"transport_finder_box")
        self.gridLayout_4 = QGridLayout(self.transport_finder_box)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.bus_route_selector_label = QLabel(self.transport_finder_box)
        self.bus_route_selector_label.setObjectName(u"bus_route_selector_label")

        self.gridLayout_4.addWidget(self.bus_route_selector_label, 0, 0, 1, 1)

        self.date_selector = QCalendarWidget(self.transport_finder_box)
        self.date_selector.setObjectName(u"date_selector")

        self.gridLayout_4.addWidget(self.date_selector, 6, 0, 1, 1)

        self.journey_date_label = QLabel(self.transport_finder_box)
        self.journey_date_label.setObjectName(u"journey_date_label")

        self.gridLayout_4.addWidget(self.journey_date_label, 5, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 7, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 4, 0, 1, 1)

        self.bus_time_label = QLabel(self.transport_finder_box)
        self.bus_time_label.setObjectName(u"bus_time_label")

        self.gridLayout_4.addWidget(self.bus_time_label, 3, 0, 1, 1)

        self.route_selector = QComboBox(self.transport_finder_box)
        self.route_selector.addItem("")
        self.route_selector.addItem("")
        self.route_selector.addItem("")
        self.route_selector.addItem("")
        self.route_selector.addItem("")
        self.route_selector.addItem("")
        self.route_selector.addItem("")
        self.route_selector.setObjectName(u"route_selector")

        self.gridLayout_4.addWidget(self.route_selector, 1, 0, 1, 1)

        self.route_confirm_btn = QPushButton(self.transport_finder_box)
        self.route_confirm_btn.setObjectName(u"route_confirm_btn")

        self.gridLayout_4.addWidget(self.route_confirm_btn, 8, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.transport_finder_box)

        self.ticket_purchase.addWidget(self.RouteSearch)
        self.DataEntry = QWidget()
        self.DataEntry.setObjectName(u"DataEntry")
        self.gridLayout_3 = QGridLayout(self.DataEntry)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.bus_seat_label = QLabel(self.DataEntry)
        self.bus_seat_label.setObjectName(u"bus_seat_label")
        self.bus_seat_label.setMinimumSize(QSize(330, 60))
        self.bus_seat_label.setMaximumSize(QSize(330, 60))

        self.gridLayout_3.addWidget(self.bus_seat_label, 2, 0, 1, 1)

        self.seat_box = QGroupBox(self.DataEntry)
        self.seat_box.setObjectName(u"seat_box")
        self.gridLayout_5 = QGridLayout(self.seat_box)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.e1 = QCheckBox(self.seat_box)
        self.e1.setObjectName(u"e1")

        self.gridLayout_5.addWidget(self.e1, 4, 0, 1, 1)

        self.b1 = QCheckBox(self.seat_box)
        self.b1.setObjectName(u"b1")

        self.gridLayout_5.addWidget(self.b1, 1, 0, 1, 1)

        self.g1 = QCheckBox(self.seat_box)
        self.g1.setObjectName(u"g1")

        self.gridLayout_5.addWidget(self.g1, 7, 0, 1, 1)

        self.d3 = QCheckBox(self.seat_box)
        self.d3.setObjectName(u"d3")

        self.gridLayout_5.addWidget(self.d3, 3, 2, 1, 1)

        self.i2 = QCheckBox(self.seat_box)
        self.i2.setObjectName(u"i2")

        self.gridLayout_5.addWidget(self.i2, 9, 1, 1, 1)

        self.e3 = QCheckBox(self.seat_box)
        self.e3.setObjectName(u"e3")

        self.gridLayout_5.addWidget(self.e3, 4, 2, 1, 1)

        self.c2 = QCheckBox(self.seat_box)
        self.c2.setObjectName(u"c2")

        self.gridLayout_5.addWidget(self.c2, 2, 1, 1, 1)

        self.h1 = QCheckBox(self.seat_box)
        self.h1.setObjectName(u"h1")

        self.gridLayout_5.addWidget(self.h1, 8, 0, 1, 1)

        self.f4 = QCheckBox(self.seat_box)
        self.f4.setObjectName(u"f4")

        self.gridLayout_5.addWidget(self.f4, 6, 3, 1, 1)

        self.f1 = QCheckBox(self.seat_box)
        self.f1.setObjectName(u"f1")

        self.gridLayout_5.addWidget(self.f1, 6, 0, 1, 1)

        self.d2 = QCheckBox(self.seat_box)
        self.d2.setObjectName(u"d2")

        self.gridLayout_5.addWidget(self.d2, 3, 1, 1, 1)

        self.h2 = QCheckBox(self.seat_box)
        self.h2.setObjectName(u"h2")

        self.gridLayout_5.addWidget(self.h2, 8, 1, 1, 1)

        self.a1 = QCheckBox(self.seat_box)
        self.a1.setObjectName(u"a1")

        self.gridLayout_5.addWidget(self.a1, 0, 0, 1, 1)

        self.f2 = QCheckBox(self.seat_box)
        self.f2.setObjectName(u"f2")

        self.gridLayout_5.addWidget(self.f2, 6, 1, 1, 1)

        self.a2 = QCheckBox(self.seat_box)
        self.a2.setObjectName(u"a2")

        self.gridLayout_5.addWidget(self.a2, 0, 1, 1, 1)

        self.j1 = QCheckBox(self.seat_box)
        self.j1.setObjectName(u"j1")

        self.gridLayout_5.addWidget(self.j1, 10, 0, 1, 1)

        self.e4 = QCheckBox(self.seat_box)
        self.e4.setObjectName(u"e4")

        self.gridLayout_5.addWidget(self.e4, 4, 3, 1, 1)

        self.d4 = QCheckBox(self.seat_box)
        self.d4.setObjectName(u"d4")

        self.gridLayout_5.addWidget(self.d4, 3, 3, 1, 1)

        self.j3 = QCheckBox(self.seat_box)
        self.j3.setObjectName(u"j3")

        self.gridLayout_5.addWidget(self.j3, 10, 2, 1, 1)

        self.a4 = QCheckBox(self.seat_box)
        self.a4.setObjectName(u"a4")

        self.gridLayout_5.addWidget(self.a4, 0, 3, 1, 1)

        self.h4 = QCheckBox(self.seat_box)
        self.h4.setObjectName(u"h4")

        self.gridLayout_5.addWidget(self.h4, 8, 3, 1, 1)

        self.g2 = QCheckBox(self.seat_box)
        self.g2.setObjectName(u"g2")

        self.gridLayout_5.addWidget(self.g2, 7, 1, 1, 1)

        self.j4 = QCheckBox(self.seat_box)
        self.j4.setObjectName(u"j4")

        self.gridLayout_5.addWidget(self.j4, 10, 3, 1, 1)

        self.b3 = QCheckBox(self.seat_box)
        self.b3.setObjectName(u"b3")

        self.gridLayout_5.addWidget(self.b3, 1, 2, 1, 1)

        self.g3 = QCheckBox(self.seat_box)
        self.g3.setObjectName(u"g3")

        self.gridLayout_5.addWidget(self.g3, 7, 2, 1, 1)

        self.b2 = QCheckBox(self.seat_box)
        self.b2.setObjectName(u"b2")

        self.gridLayout_5.addWidget(self.b2, 1, 1, 1, 1)

        self.g4 = QCheckBox(self.seat_box)
        self.g4.setObjectName(u"g4")

        self.gridLayout_5.addWidget(self.g4, 7, 3, 1, 1)

        self.c4 = QCheckBox(self.seat_box)
        self.c4.setObjectName(u"c4")

        self.gridLayout_5.addWidget(self.c4, 2, 3, 1, 1)

        self.i3 = QCheckBox(self.seat_box)
        self.i3.setObjectName(u"i3")

        self.gridLayout_5.addWidget(self.i3, 9, 2, 1, 1)

        self.c3 = QCheckBox(self.seat_box)
        self.c3.setObjectName(u"c3")

        self.gridLayout_5.addWidget(self.c3, 2, 2, 1, 1)

        self.j2 = QCheckBox(self.seat_box)
        self.j2.setObjectName(u"j2")

        self.gridLayout_5.addWidget(self.j2, 10, 1, 1, 1)

        self.f3 = QCheckBox(self.seat_box)
        self.f3.setObjectName(u"f3")

        self.gridLayout_5.addWidget(self.f3, 6, 2, 1, 1)

        self.b4 = QCheckBox(self.seat_box)
        self.b4.setObjectName(u"b4")

        self.gridLayout_5.addWidget(self.b4, 1, 3, 1, 1)

        self.a3 = QCheckBox(self.seat_box)
        self.a3.setObjectName(u"a3")

        self.gridLayout_5.addWidget(self.a3, 0, 2, 1, 1)

        self.i1 = QCheckBox(self.seat_box)
        self.i1.setObjectName(u"i1")

        self.gridLayout_5.addWidget(self.i1, 9, 0, 1, 1)

        self.d1 = QCheckBox(self.seat_box)
        self.d1.setObjectName(u"d1")

        self.gridLayout_5.addWidget(self.d1, 3, 0, 1, 1)

        self.c1 = QCheckBox(self.seat_box)
        self.c1.setObjectName(u"c1")

        self.gridLayout_5.addWidget(self.c1, 2, 0, 1, 1)

        self.i4 = QCheckBox(self.seat_box)
        self.i4.setObjectName(u"i4")

        self.gridLayout_5.addWidget(self.i4, 9, 3, 1, 1)

        self.e2 = QCheckBox(self.seat_box)
        self.e2.setObjectName(u"e2")

        self.gridLayout_5.addWidget(self.e2, 4, 1, 1, 1)

        self.h3 = QCheckBox(self.seat_box)
        self.h3.setObjectName(u"h3")

        self.gridLayout_5.addWidget(self.h3, 8, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 5, 1, 1, 1)


        self.gridLayout_3.addWidget(self.seat_box, 0, 0, 1, 1)

        self.purchase_details_box = QGroupBox(self.DataEntry)
        self.purchase_details_box.setObjectName(u"purchase_details_box")
        self.gridLayout_6 = QGridLayout(self.purchase_details_box)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.payment_proceed_btn = QPushButton(self.purchase_details_box)
        self.payment_proceed_btn.setObjectName(u"payment_proceed_btn")

        self.gridLayout_6.addWidget(self.payment_proceed_btn, 3, 0, 1, 1)

        self.payment_method_selector = QComboBox(self.purchase_details_box)
        self.payment_method_selector.addItem("")
        self.payment_method_selector.addItem("")
        self.payment_method_selector.addItem("")
        self.payment_method_selector.setObjectName(u"payment_method_selector")

        self.gridLayout_6.addWidget(self.payment_method_selector, 2, 0, 1, 1)

        self.purchase_details = QTextBrowser(self.purchase_details_box)
        self.purchase_details.setObjectName(u"purchase_details")

        self.gridLayout_6.addWidget(self.purchase_details, 0, 0, 1, 1)

        self.payment_label = QLabel(self.purchase_details_box)
        self.payment_label.setObjectName(u"payment_label")

        self.gridLayout_6.addWidget(self.payment_label, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.purchase_details_box, 0, 1, 3, 1)

        self.seat_confirm_btn = QPushButton(self.DataEntry)
        self.seat_confirm_btn.setObjectName(u"seat_confirm_btn")

        self.gridLayout_3.addWidget(self.seat_confirm_btn, 1, 0, 1, 1)

        self.ticket_purchase.addWidget(self.DataEntry)
        self.Payment = QWidget()
        self.Payment.setObjectName(u"Payment")
        self.gridLayout_7 = QGridLayout(self.Payment)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.print_btn = QPushButton(self.Payment)
        self.print_btn.setObjectName(u"print_btn")

        self.gridLayout_7.addWidget(self.print_btn, 2, 0, 1, 1)

        self.Confirm_box = QGroupBox(self.Payment)
        self.Confirm_box.setObjectName(u"Confirm_box")
        self.gridLayout_11 = QGridLayout(self.Confirm_box)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.confirmation_label = QLabel(self.Confirm_box)
        self.confirmation_label.setObjectName(u"confirmation_label")

        self.gridLayout_11.addWidget(self.confirmation_label, 0, 0, 1, 1)

        self.ticket_viewer = QTextBrowser(self.Confirm_box)
        self.ticket_viewer.setObjectName(u"ticket_viewer")

        self.gridLayout_11.addWidget(self.ticket_viewer, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.Confirm_box, 1, 0, 1, 1)

        self.payment_box = QGroupBox(self.Payment)
        self.payment_box.setObjectName(u"payment_box")
        self.gridLayout_8 = QGridLayout(self.payment_box)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.qr_code_box = QFrame(self.payment_box)
        self.qr_code_box.setObjectName(u"qr_code_box")
        self.qr_code_box.setFrameShape(QFrame.StyledPanel)
        self.qr_code_box.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.qr_code_box)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.qr_code_label = QLabel(self.qr_code_box)
        self.qr_code_label.setObjectName(u"qr_code_label")

        self.gridLayout_9.addWidget(self.qr_code_label, 0, 0, 1, 1)

        self.qr_code = QTextBrowser(self.qr_code_box)
        self.qr_code.setObjectName(u"qr_code")

        self.gridLayout_9.addWidget(self.qr_code, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.qr_code_box, 3, 1, 1, 1)

        self.manual_payment_box = QFrame(self.payment_box)
        self.manual_payment_box.setObjectName(u"manual_payment_box")
        self.manual_payment_box.setFrameShape(QFrame.StyledPanel)
        self.manual_payment_box.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.manual_payment_box)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.payment_pay_btn = QPushButton(self.manual_payment_box)
        self.payment_pay_btn.setObjectName(u"payment_pay_btn")

        self.gridLayout_10.addWidget(self.payment_pay_btn, 5, 0, 1, 1)

        self.payment_otp_label = QLabel(self.manual_payment_box)
        self.payment_otp_label.setObjectName(u"payment_otp_label")

        self.gridLayout_10.addWidget(self.payment_otp_label, 2, 0, 1, 1)

        self.payment_number_lineEdit = QLineEdit(self.manual_payment_box)
        self.payment_number_lineEdit.setObjectName(u"payment_number_lineEdit")

        self.gridLayout_10.addWidget(self.payment_number_lineEdit, 1, 0, 1, 1)

        self.payment_number_label = QLabel(self.manual_payment_box)
        self.payment_number_label.setObjectName(u"payment_number_label")

        self.gridLayout_10.addWidget(self.payment_number_label, 0, 0, 1, 1)

        self.payment_otp_lineEdit = QLineEdit(self.manual_payment_box)
        self.payment_otp_lineEdit.setObjectName(u"payment_otp_lineEdit")

        self.gridLayout_10.addWidget(self.payment_otp_lineEdit, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_2, 4, 0, 1, 1)


        self.gridLayout_8.addWidget(self.manual_payment_box, 3, 0, 1, 1)


        self.gridLayout_7.addWidget(self.payment_box, 0, 0, 1, 1)

        self.ticket_purchase.addWidget(self.Payment)

        self.gridLayout.addWidget(self.ticket_purchase, 1, 0, 1, 2)

        self.Title = QLabel(self.centralwidget)
        self.Title.setObjectName(u"Title")

        self.gridLayout.addWidget(self.Title, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.Title.raise_()
        self.status_label.raise_()
        self.ticket_purchase.raise_()
        self.back_btn.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.ticket_purchase.setCurrentIndex(0)
        self.bus_time_label.setText('')
        index = self.ticket_purchase.currentIndex()
        if index == 0:
            self.back_btn.setVisible(False)

        #Responses
        self.route_selector.currentIndexChanged.connect(self.route_selector_response)

        #Button Responses
        self.back_btn.clicked.connect(self.back_btn_function)
        self.route_confirm_btn.clicked.connect(self.route_confirm_function)
        self.payment_proceed_btn.clicked.connect(self.payment_proceed_function)
        self.seat_confirm_btn.clicked.connect(self.seat_confirm_function)
        self.print_btn.clicked.connect(self.print_ticket_function)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u" © TITION FOUNDATION - TONMOY PAUL 2024", None))
        self.back_btn.setText(QCoreApplication.translate("MainWindow", u"< Back", None))
        self.identity_info_box.setTitle(QCoreApplication.translate("MainWindow", u"Identity Information", None))
        self.identity_selector.setItemText(0, QCoreApplication.translate("MainWindow", u"Select", None))
        self.identity_selector.setItemText(1, QCoreApplication.translate("MainWindow", u"Faculty Member", None))
        self.identity_selector.setItemText(2, QCoreApplication.translate("MainWindow", u"Student", None))
        self.identity_selector.setItemText(3, QCoreApplication.translate("MainWindow", u"Office Staff", None))

        self.name_label.setText(QCoreApplication.translate("MainWindow", u"Enter Your Name", None))
        self.identity_select_label.setText(QCoreApplication.translate("MainWindow", u"Select Any", None))
        self.id_num_label.setText(QCoreApplication.translate("MainWindow", u"Enter Your ID Number", None))
        self.transport_finder_box.setTitle(QCoreApplication.translate("MainWindow", u"Transport Finder", None))
        self.bus_route_selector_label.setText(QCoreApplication.translate("MainWindow", u"Select Bus Route", None))
        self.journey_date_label.setText(QCoreApplication.translate("MainWindow", u"Journey Date", None))
        self.bus_time_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Bus Time:</p></body></html>", None))
        self.route_selector.setItemText(0, QCoreApplication.translate("MainWindow", u"Select", None))
        self.route_selector.setItemText(1, QCoreApplication.translate("MainWindow", u"Rajshahi", None))
        self.route_selector.setItemText(2, QCoreApplication.translate("MainWindow", u"Naogaon", None))
        self.route_selector.setItemText(3, QCoreApplication.translate("MainWindow", u"Bogura", None))
        self.route_selector.setItemText(4, QCoreApplication.translate("MainWindow", u"Natore", None))
        self.route_selector.setItemText(5, QCoreApplication.translate("MainWindow", u"Pabna", None))
        self.route_selector.setItemText(6, QCoreApplication.translate("MainWindow", u"Rangpur", None))
        self.route_selector.setItemText(7, QCoreApplication.translate("MainWindow", u"Tangail", None))

        self.route_confirm_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.bus_seat_label.setText("")
        self.seat_box.setTitle(QCoreApplication.translate("MainWindow", u"Select Your Desired Seat", None))
        self.e1.setText(QCoreApplication.translate("MainWindow", u"E1", None))
        self.b1.setText(QCoreApplication.translate("MainWindow", u"B1", None))
        self.g1.setText(QCoreApplication.translate("MainWindow", u"G1", None))
        self.d3.setText(QCoreApplication.translate("MainWindow", u"D3", None))
        self.i2.setText(QCoreApplication.translate("MainWindow", u"I2", None))
        self.e3.setText(QCoreApplication.translate("MainWindow", u"E3", None))
        self.c2.setText(QCoreApplication.translate("MainWindow", u"C2", None))
        self.h1.setText(QCoreApplication.translate("MainWindow", u"H1", None))
        self.f4.setText(QCoreApplication.translate("MainWindow", u"F4", None))
        self.f1.setText(QCoreApplication.translate("MainWindow", u"F1", None))
        self.d2.setText(QCoreApplication.translate("MainWindow", u"D2", None))
        self.h2.setText(QCoreApplication.translate("MainWindow", u"H2", None))
        self.a1.setText(QCoreApplication.translate("MainWindow", u"A1", None))
        self.f2.setText(QCoreApplication.translate("MainWindow", u"F2", None))
        self.a2.setText(QCoreApplication.translate("MainWindow", u"A2", None))
        self.j1.setText(QCoreApplication.translate("MainWindow", u"J1", None))
        self.e4.setText(QCoreApplication.translate("MainWindow", u"E4", None))
        self.d4.setText(QCoreApplication.translate("MainWindow", u"D4", None))
        self.j3.setText(QCoreApplication.translate("MainWindow", u"J3", None))
        self.a4.setText(QCoreApplication.translate("MainWindow", u"A4", None))
        self.h4.setText(QCoreApplication.translate("MainWindow", u"H4", None))
        self.g2.setText(QCoreApplication.translate("MainWindow", u"G2", None))
        self.j4.setText(QCoreApplication.translate("MainWindow", u"J4", None))
        self.b3.setText(QCoreApplication.translate("MainWindow", u"B3", None))
        self.g3.setText(QCoreApplication.translate("MainWindow", u"G3", None))
        self.b2.setText(QCoreApplication.translate("MainWindow", u"B2", None))
        self.g4.setText(QCoreApplication.translate("MainWindow", u"G4", None))
        self.c4.setText(QCoreApplication.translate("MainWindow", u"C4", None))
        self.i3.setText(QCoreApplication.translate("MainWindow", u"I3", None))
        self.c3.setText(QCoreApplication.translate("MainWindow", u"C3", None))
        self.j2.setText(QCoreApplication.translate("MainWindow", u"J2", None))
        self.f3.setText(QCoreApplication.translate("MainWindow", u"F3", None))
        self.b4.setText(QCoreApplication.translate("MainWindow", u"B4", None))
        self.a3.setText(QCoreApplication.translate("MainWindow", u"A3", None))
        self.i1.setText(QCoreApplication.translate("MainWindow", u"I1", None))
        self.d1.setText(QCoreApplication.translate("MainWindow", u"D1", None))
        self.c1.setText(QCoreApplication.translate("MainWindow", u"C1", None))
        self.i4.setText(QCoreApplication.translate("MainWindow", u"I4", None))
        self.e2.setText(QCoreApplication.translate("MainWindow", u"E2", None))
        self.h3.setText(QCoreApplication.translate("MainWindow", u"H3", None))
        self.purchase_details_box.setTitle(QCoreApplication.translate("MainWindow", u"Purchase Details", None))
        self.payment_proceed_btn.setText(QCoreApplication.translate("MainWindow", u"Proceed to Pay", None))
        self.payment_method_selector.setItemText(0, QCoreApplication.translate("MainWindow", u"bKash", None))
        self.payment_method_selector.setItemText(1, QCoreApplication.translate("MainWindow", u"Nagad", None))
        self.payment_method_selector.setItemText(2, QCoreApplication.translate("MainWindow", u"Card Payment", None))

        self.payment_label.setText(QCoreApplication.translate("MainWindow", u"Select Payment Method", None))
        self.seat_confirm_btn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.print_btn.setText(QCoreApplication.translate("MainWindow", u"Print Ticket", None))
        self.Confirm_box.setTitle(QCoreApplication.translate("MainWindow", u"Confirmation", None))
        self.confirmation_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Congratulations! You can print your ticket now. </span></p></body></html>", None))
        self.payment_box.setTitle(QCoreApplication.translate("MainWindow", u"Payment", None))
        self.qr_code_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Scan the QR Code to Pay</p></body></html>", None))
        self.qr_code.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'YaHei Consolas Hybrid'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"qr.png\" /> </p></body></html>", None))
        self.payment_pay_btn.setText(QCoreApplication.translate("MainWindow", u"Pay", None))
        self.payment_otp_label.setText(QCoreApplication.translate("MainWindow", u"OTP", None))
        self.payment_number_label.setText(QCoreApplication.translate("MainWindow", u"Number", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">University Bus Ticket Purchase</span></p></body></html>", None))
    # retranslateUi

    def route_selector_response(self):
        route_index = self.route_selector.currentIndex()
        if route_index == 0:
            self.bus_time_label.setText('')
        else:
            self.bus_time_label.setText('Bus Time: '+ time_list[route_index-1] + '   Fare: '+ str(ticket_price[route_index-1])+'BDT')

    def route_confirm_function(self):
        self.ticket_purchase.setCurrentIndex(1)
        self.back_btn.setVisible(True)

    def payment_proceed_function(self):
        self.ticket_purchase.setCurrentIndex(2)
        self.back_btn.setVisible(True)

    def back_btn_function(self):
        index = self.ticket_purchase.currentIndex()
        if index > 0:
            self.ticket_purchase.setCurrentIndex(index-1)
            if index-1 ==0:
                self.back_btn.setVisible(False)

    def seat_confirm_function(self):
        self.ticket_details()
    def seat_selection_function(self):
        checked = []
        seat_info =[]
        seat_count = 0
        checkboxes = [
            self.a1, self.a2, self.a3, self.a4,
            self.b1, self.b2, self.b3, self.b4,
            self.c1, self.c2, self.c3, self.c4,
            self.d1, self.d2, self.d3, self.d4,
            self.e1, self.e2, self.e3, self.e4,
            self.f1, self.f2, self.f3, self.f4,
            self.g1, self.g2, self.g3, self.g4,
            self.h1, self.h2, self.h3, self.h4,
            self.i1, self.i2, self.i3, self.i4,
            self.j1, self.j2, self.j3, self.j4,
        ]

        for checkbox in checkboxes:
            if checkbox.isChecked():
                seat_count = seat_count + 1
                checked.append('self.'+checkbox.objectName())

        for box in checked:
            seat_info.append(eval(box).text())

        self.bus_seat_label.setText('Selected Seats:' + ','.join(seat_info))

        return [seat_count,seat_info]


    def fetch_data(self):
        category_info = self.identity_selector.currentText()
        id_info = self.id_line_edit.text()
        name_info = self.name_line_edit.text()
        route_info = self.route_selector.currentText()
        date_info = self.date_selector.selectedDate().toString("dd-MM-yyyy")

        route_index = self.route_selector.currentIndex()
        if route_index ==0:
            fare_info = 0
            time_info = ''
        elif route_index > 0 :
            fare_info = float(ticket_price[route_index - 1])
            time_info = time_list[route_index - 1]

        seat_count = self.seat_selection_function()[0]
        seat_info = self.seat_selection_function()[1]

        cost_info = seat_count*fare_info

        return [category_info,id_info,name_info,route_info,date_info,fare_info,time_info,seat_count,seat_info, cost_info]

    def ticket_details(self):
        import random

        [category_info, id_info, name_info, route_info, date_info, fare_info, time_info, seat_count, seat_info,
         cost_info] = self.fetch_data()

        pnr_number = ''.join(random.choice('0123456789') for _ in range(10)) + id_info + date_info

        self.qr_generator(pnr_number)

        ticket = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Bus Ticket</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f0f0f0;
                }
                .container {
                    align: center;
                    width: 80px;
                    height: 80px;
                    margin: 20px auto;
                    padding: 20px;
                    background-color: #fff;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                .ticket {
                max-width: 600px;
                margin: 20px auto;
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }

                .ticket-header {
                text-align: center;
                }

                .ticket-header h1 {
                color: #333;
                }

                .ticket-details {
                margin-top: 20px;
                }

                .detail-row {
                display: flex;
                justify-content: space-between;
                margin-bottom: 10px;
                }

                .detail-label {
                color: #555;
                }

                .detail-value {
                font-weight: bold;
                }

                .seat-info {
                margin-top: 20px;
                }

                .seat-label {
                color: #555;
                }

                .seat-list {
                list-style-type: none;
                padding: 0;
                margin: 0;
                }

                .seat-list-item {
                margin-bottom: 5px;
                }

                .total-cost {
                margin-top: 20px;
                text-align: center;
                }

                .total-cost-label {
                color: #555;
                }

                .total-cost-value {
                font-size: 1.2em;
                font-weight: bold;
                }
            </style>
        </head>
        <body>

        <div class="ticket">
            <div class="ticket-header">
                <h1>Bus Ticket</h1>
            </div>
            
            <div class = "container">
                <img src='pnr.png' style="height: 80px; width: 80px;">
            </div>
            
            <div class="ticket-details">
                
                <div class="detail-row">
                    <span class="detail-label">PNR:</span>
                    <span class="detail-value">"""+pnr_number+"""</span>
                </div>
                
                <div class="detail-row">
                    <span class="detail-label">Category:</span>
                    <span class="detail-value">"""+category_info+"""</span>
                </div>
            <div class="detail-row">
                    <span class="detail-label">ID:</span>
                    <span class="detail-value">"""+id_info+"""</span>
            </div>
            <div class="detail-row">
                    <span class="detail-label">Name:</span>
                    <span class="detail-value">"""+name_info+"""</span>
            </div>
            <div class="detail-row">
                    <span class="detail-label">Route:</span>
                    <span class="detail-value">"""+route_info+"""</span>
            </div>
            <div class="detail-row">
                    <span class="detail-label">Ticket Fare:</span>
                    <span class="detail-value">"""+str(fare_info)+"""</span>
            </div>
            <div class="detail-row">
                    <span class="detail-label">Date:</span>
                    <span class="detail-value">"""+date_info+"""</span>
            </div>
            <div class="detail-row">
                    <span class="detail-label">Time:</span>
                    <span class="detail-value">"""+time_info+"""</span>
            </div>
            </div>

            <div class="detail-row">
                <span class="detail-label">Selected Seat(s):</span>
                    <span class="detail-value">"""+', '.join(seat_info)+"""</span>
            </div>
            
            <div class="total-cost">
                <div class="total-cost-label">Total Cost:</div>
                <div class="total-cost-value">"""+str(cost_info)+""" BDT</div>
            </div>
        </div>

    </body>
    </html>
                """

        ticket_info = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Bus Ticket</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            margin: 0;
                            padding: 0;
                            background-color: #f0f0f0;
                        }
                        .container {
                            align: center;
                            width: 80px;
                            height: 80px;
                            margin: 20px auto;
                            padding: 20px;
                            background-color: #fff;
                            border-radius: 8px;
                            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        }
                        .ticket {
                        max-width: 600px;
                        margin: 20px auto;
                        background-color: #fff;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        }

                        .ticket-header {
                        text-align: center;
                        }

                        .ticket-header h1 {
                        color: #333;
                        }

                        .ticket-details {
                        margin-top: 20px;
                        }

                        .detail-row {
                        display: flex;
                        justify-content: space-between;
                        margin-bottom: 10px;
                        }

                        .detail-label {
                        color: #555;
                        }

                        .detail-value {
                        font-weight: bold;
                        }

                        .seat-info {
                        margin-top: 20px;
                        }

                        .seat-label {
                        color: #555;
                        }

                        .seat-list {
                        list-style-type: none;
                        padding: 0;
                        margin: 0;
                        }

                        .seat-list-item {
                        margin-bottom: 5px;
                        }

                        .total-cost {
                        margin-top: 20px;
                        text-align: center;
                        }

                        .total-cost-label {
                        color: #555;
                        }

                        .total-cost-value {
                        font-size: 1.2em;
                        font-weight: bold;
                        }
                    </style>
                </head>
                <body>

                <div class="ticket">
                    <div class="ticket-header">
                        <h1>Bus Ticket</h1>
                    </div>
                    <div class="ticket-details">

                        <div class="detail-row">
                            <span class="detail-label">PNR:</span>
                            <span class="detail-value">""" + pnr_number + """</span>
                        </div>

                        <div class="detail-row">
                            <span class="detail-label">Category:</span>
                            <span class="detail-value">""" + category_info + """</span>
                        </div>
                    <div class="detail-row">
                            <span class="detail-label">ID:</span>
                            <span class="detail-value">""" + id_info + """</span>
                    </div>
                    <div class="detail-row">
                            <span class="detail-label">Name:</span>
                            <span class="detail-value">""" + name_info + """</span>
                    </div>
                    <div class="detail-row">
                            <span class="detail-label">Route:</span>
                            <span class="detail-value">""" + route_info + """</span>
                    </div>
                    <div class="detail-row">
                            <span class="detail-label">Ticket Fare:</span>
                            <span class="detail-value">""" + str(fare_info) + """</span>
                    </div>
                    <div class="detail-row">
                            <span class="detail-label">Date:</span>
                            <span class="detail-value">""" + date_info + """</span>
                    </div>
                    <div class="detail-row">
                            <span class="detail-label">Time:</span>
                            <span class="detail-value">""" + time_info + """</span>
                    </div>
                    </div>

                    <div class="detail-row">
                        <span class="detail-label">Selected Seat(s):</span>
                            <span class="detail-value">""" + ', '.join(seat_info) + """</span>
                    </div>

                    <div class="total-cost">
                        <div class="total-cost-label">Total Cost:</div>
                        <div class="total-cost-value">""" + str(cost_info) + """ BDT</div>
                    </div>
                </div>

            </body>
            </html>
                        """

        self.purchase_details.setText(ticket_info)
        self.ticket_viewer.setText(ticket_info)
        return ticket

    def print_ticket_function(self):
        import subprocess
        import platform
        import pdfkit
        import os

        ticket_content = self.ticket_details()

        file = open('ticket.html','w')
        file.write(ticket_content)
        file.close()
        pdfkit.from_file('ticket.html', 'ticket.pdf', verbose=True, options= {"enable-local-file-access": True})

        os.remove('ticket.html')

        system_platform = platform.system().lower()
        if system_platform == "windows":
            subprocess.run(["start", "ticket.pdf"], shell=True)
        elif system_platform == "linux":
            subprocess.run(["xdg-open", "ticket.pdf"])
        elif system_platform == "darwin":
            subprocess.run(["open", "ticket.pdf"])
        else:
            print("Unsupported operating system.")

    def qr_generator(self, text):
        import qrcode
        import os

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Get the absolute path to the current working directory
        current_directory = os.path.abspath(os.getcwd())

        # Save the QR code image with an absolute path
        qr_image_path = os.path.join(current_directory, 'pnr.png')
        img.save(qr_image_path)

        return qr_image_path

