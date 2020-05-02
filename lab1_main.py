# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
import numpy as np
from lab1_form import Ui_MainWindow
import math_module_lab1



class mywindow(QtWidgets.QMainWindow): #класс приложения
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btn1)
        combobox_table_added(self.ui.tableWidget_2,5)
        self.ui.comboBox.activated[str].connect(self.combobox1)
        self.ui.pushButton_2.clicked.connect(self.btn2)

    def btn1(self):
        table = self.ui.tableWidget
        spinBox_value = self.ui.spinBox.value()
        table.setColumnCount(spinBox_value)
        table.setRowCount(spinBox_value)
        print(table.width() // spinBox_value)
        print(table.height() // spinBox_value)
        for i in range(spinBox_value):
            table.setColumnWidth(i, table.width() // spinBox_value)
            table.setRowHeight(i,table.height() // spinBox_value)
        combobox_table_added(table,spinBox_value)



    def combobox1(self, text):
        table2 = self.ui.tableWidget_2
        table3 = self.ui.tableWidget_3
        table4 = self.ui.tableWidget_4
        if text == 'Включение' or text == 'Дополнение' or text == 'Обратное'or text == 'Двойственности':
            table3.setEnabled(False)
            table3.clear()
            combobox_table_added(table2,5)
        else:
            combobox_table_added(table2,5)
            combobox_table_added(table3,5)
            table3.setEnabled(True)

    def btn2(self):
        table2 = self.ui.tableWidget_2
        table3 = self.ui.tableWidget_3
        table4 = self.ui.tableWidget_4
        table2_matrix = table_value_set(table2)
        print(table2_matrix)


def combobox_table_added(table,spinBox_value):
    for i in range(spinBox_value):
        for j in range(spinBox_value):
            combobox = QtWidgets.QComboBox()
            combobox.setStyleSheet('background-color: #FFFFFF;')
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            combobox.addItems(['0', '1'])
            combobox.setCurrentIndex(np.random.randint(2))
            combobox.setFont(font)
            table.setCellWidget(i, j, combobox)

def table_value_set(table,size=5):
    table_matrix = np.empty((5,5))
    for i in range(size):
        for j in range(size):
            table_matrix[i][j] = table.cellWidget(i,j).currentText()
    return table_matrix

app = QtWidgets.QApplication(sys.argv)
application = mywindow()
application.show()

sys.exit(app.exec_())