# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
import numpy as np
from lab2_form import Ui_MainWindow
import math_module_lab2


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

def table_value_get(table,size=5):
    table_matrix = np.empty((size,size))
    for i in range(size):
        for j in range(size):
            table_matrix[i][j] = table.cellWidget(i,j).currentText()
    return table_matrix

def table_value_set(self,table_matrix, table, size=5):
    for row in range(size):
        for column in range(size):
            table.setItem(row,column, QtWidgets.QTableWidgetItem(f'{int(table_matrix[row][column])}'))

def lineEdit_set(self,line_edit,array):
    set_string = str(array)
    set_string = set_string.replace('[','{')
    set_string = set_string.replace(']','}')
    line_edit.setText(set_string)




class mywindow(QtWidgets.QMainWindow): #класс приложения
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btn1)
        self.ui.pushButton_3.clicked.connect(self.btn3)
        self.ui.pushButton_2.clicked.connect(self.btn2)

    def btn1(self):
        table = self.ui.tableWidget
        spinBox_value = self.ui.spinBox.value()
        table.setColumnCount(0)
        table.setRowCount(0)
        table.setColumnCount(spinBox_value)
        table.setRowCount(spinBox_value)
        table.clear()
        for i in range(spinBox_value):
            table.setColumnWidth(i, table.width() // spinBox_value)
            table.setRowHeight(i, table.height() // spinBox_value)
        combobox_table_added(table, spinBox_value)


    def btn3(self):
        table = self.ui.tableWidget
        spinBox_value = self.ui.spinBox.value()
        try:
            matrix = table_value_get(table,spinBox_value)
        except AttributeError:
            return False
        lineEdit_set(self,self.ui.lineEdit,math_module_lab2.set_of_maximum(matrix))
        lineEdit_set(self, self.ui.lineEdit_2, math_module_lab2.set_of_minimum(matrix))
        lineEdit_set(self, self.ui.lineEdit_3, math_module_lab2.set_of_majorant(matrix))
        lineEdit_set(self, self.ui.lineEdit_4, math_module_lab2.set_of_minorant(matrix))


    def btn2(self):
        table = self.ui.tableWidget_2
        spinBox_value = self.ui.spinBox_2.value()
        table.setColumnCount(0)
        table.setRowCount(0)
        table.setColumnCount(spinBox_value)
        table.setRowCount(spinBox_value)
        table.clear()
        for i in range(spinBox_value):
            table.setColumnWidth(i, table.width() // spinBox_value)
            table.setRowHeight(i, table.height() // spinBox_value)
        combobox_table_added(table, spinBox_value)





app = QtWidgets.QApplication(sys.argv)
application = mywindow()
application.show()

sys.exit(app.exec_())