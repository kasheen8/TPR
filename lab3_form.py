# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kashe\Desktop\ТПР\lab3_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget {\n"
                                 " background-color:#8FBC8F;\n"
                                 "}\n"
                                 "\n"
                                 "QTableWidget {\n"
                                 " background-color:#ffffff;\n"
                                 " font-weight: bold;\n"
                                 " border: 2px solid black;\n"
                                 " color: #000000;\n"
                                 "}\n"
                                 "\n"
                                 "QSpinBox {\n"
                                 " background-color:#ffffff;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "background-color:#ffffff;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit {\n"
                                 " background-color:#ffffff;\n"
                                 " color:#000000;\n"
                                 " border: 1px solid black;\n"
                                 "}\n"
                                 "\n"
                                 "QTextEdit {\n"
                                 " background-color:#ffffff;\n"
                                 " color:#000000;\n"
                                 " border: 1px solid black;\n"
                                 "}\n"
                                 "\n"
                                 "QTabWidget {\n"
                                 " color: #000000;\n"
                                 " border: 1px solid black;\n"
                                 "}\n"
                                 "QComboBox {\n"
                                 "background-color:#ffffff;\n"
                                 "}\n"
                                 "QComboBox::drop-down {\n"
                                 " border-width: 0px;}\n"
                                 "QComboBox::drop-arrow{\n"
                                 "image:url(noimg);\n"
                                 "borider-width:0px;}"
                                 "\n"
                                 )
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(680, 10, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 441, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 170, 438, 273))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(59)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(82)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 480, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 480, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText('0')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 470, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 170, 301, 391))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Теория принятия решений. Лабораторная работа № 5"))
        self.label.setText(_translate("MainWindow", "Вариант №3"))
        self.label_2.setText(_translate("MainWindow", "Одно из предприятий, обслуживающее население, должно определить уровень потребности клиентов в течение предстоящих праздников. Точное число клиентов неизвестно, но ожидается, что оно может принять одно из четырех значений: 200, 250, 300, 350. Для каждого из этих возможных значений существует наилучший уровень предложения (с точки зрения возможных доходов). Взяв в качестве   значение 0,5;0.75, 0,1, найдите наилучшую альтернативу  , используя критерий С Гурвица. Матрица решений имеет вид:"))
        self.label_3.setText(_translate("MainWindow", "μ = "))
        self.pushButton.setText(_translate("MainWindow", "Найти наилучшую альтернативу"))
