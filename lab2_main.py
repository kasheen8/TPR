# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
import numpy as np
from lab2_form import Ui_MainWindow
import math_module_lab2


def combobox_table_added(table,spinBox_value): #добавление компобоксов в таблицу
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

def lineedit_validator_table_added(table,spinBox_value):
    for i in range(spinBox_value):
        for j in range(spinBox_value):
            lineedit = QtWidgets.QLineEdit()
            lineedit.setStyleSheet('background-color: #FFFFFF;\n color: #000000;')
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            if i==j:
                lineedit.setText('∞')
                lineedit.setEnabled(False)
            else:
                lineedit.setValidator(QtGui.QIntValidator(0,99,parent = None))
                Communications = np.random.randint(2)
                if Communications:
                    lineedit.setText(str(np.random.randint(100)))
                else:
                    lineedit.setText('0')
            lineedit.setFont(font)
            table.setCellWidget(i, j, lineedit)

def table_value_get(table,size=5): #записывает значение таблицы из комбобоксов в массив
    table_matrix = np.empty((size,size))
    for i in range(size):
        for j in range(size):
            table_matrix[i][j] = table.cellWidget(i,j).currentText()
    return table_matrix

def table_value_get_lineedit(table,size=5):
    table_matrix = np.empty((size, size))
    for i in range(size):
        for j in range(size):
            if table.cellWidget(i, j).text() != '∞':
                table_matrix[i][j] = table.cellWidget(i, j).text()
            else:
                table_matrix[i][j] = 0
    return table_matrix

def table_value_set(self,table_matrix, table, size=5): #записывает значение из массива в таблицу
    for row in range(size):
        for column in range(size):
            table.setItem(row,column, QtWidgets.QTableWidgetItem(f'{int(table_matrix[row][column])}'))

def lineEdit_set(self,line_edit,array): #замена в списке скобок для вывода на экран
    set_string = str(array)
    set_string = set_string.replace('[','{')
    set_string = set_string.replace(']','}')
    line_edit.setText(set_string)

def two_column_table_set(table): #заполнение первых двух колонок таблицы истинности
    first_column_list = ['0', '0', '1', '1']
    second_column_list = ['0', '1', '0', '1']
    for i in range(4):
        table.setItem(i, 0, QtWidgets.QTableWidgetItem(f'{first_column_list[i]}'))
        table.setItem(i, 1, QtWidgets.QTableWidgetItem(f'{second_column_list[i]}'))

def logical_form(table): #вычисление значений для таблицы истинности
    bin_list = []
    for i in range(4):
        bin_list.append(table.item(i,2).text())
    string_result = math_module_lab2.bin_result(bin_list)
    func = str(table.horizontalHeaderItem(2).text())
    if len(string_result) == 1:
        return f'{func} = {string_result}'
    elif len(string_result) == 3:
        string_result = string_result.replace('-','¬')
        string_result = string_result.replace('+', ' ')
        logic_form = f'{string_result[0]}{str(table.horizontalHeaderItem(0).text())}' \
                     f'{string_result[1]}{string_result[2]}{str(table.horizontalHeaderItem(1).text())}'
        logic_form = f'{func} = {logic_form}'
        if '∧' in logic_form:
            return logic_form + ' - СДНФ'
        else:
            return logic_form + ' - СКНФ'
    elif len(string_result) == 11:
        string_result = string_result.replace('-', '¬')
        string_result = string_result.replace('+', ' ')
        logic_form = f'{string_result[:2]}{str(table.horizontalHeaderItem(0).text())}' \
                     f'{string_result[2:4]}{str(table.horizontalHeaderItem(1).text())}' \
                     f'{string_result[4:8]}{str(table.horizontalHeaderItem(0).text())}' \
                     f'{string_result[8:10]}{str(table.horizontalHeaderItem(1).text())}' \
                     f'{string_result[10]}'
        logic_form = f'{func} = {logic_form}'
        if string_result[5] == '∧':
            return logic_form + ' - СКНФ'
        else:
            return logic_form + ' - СДНФ'





class mywindow(QtWidgets.QMainWindow): #класс приложения
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btn1)
        self.ui.pushButton_3.clicked.connect(self.btn3)
        self.ui.pushButton_2.clicked.connect(self.btn2)
        self.ui.pushButton_4.clicked.connect(self.btn4)
        self.ui.spinBox_2.valueChanged.connect(self.clear_table)
        self.ui.tableWidget_6.setHorizontalHeaderLabels(('X', 'C(X)', 'β','β(C(X))'))
        self.ui.tableWidget_7.setHorizontalHeaderLabels(('β2', 'β3', 'f1'))
        self.ui.tableWidget_8.setHorizontalHeaderLabels(('β1', 'β3', 'f2'))
        self.ui.tableWidget_9.setHorizontalHeaderLabels(('β1', 'β2', 'f3'))
        list_of_combinations = ['Ø','X1','X2','X3','X1X2','X1X3','X2X3','X1X2X3']
        list_of_binaries = ['000','100','010','001','110','101','011','111']
        for i in range(8):
            self.ui.tableWidget_6.setItem(i, 0, self.createItem(f'{list_of_combinations[i]}', Qt.ItemIsSelectable))
            self.ui.tableWidget_6.setItem(i, 2, self.createItem(f'{list_of_binaries[i]}', Qt.ItemIsSelectable))
            self.ui.tableWidget_6.setItem(i, 3, self.createItem(f' ', Qt.ItemIsSelectable))
            combobox = QtWidgets.QComboBox()
            combobox.setStyleSheet('background-color: #FFFFFF;')
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            combobox.addItems(list_of_combinations)
            combobox.setCurrentIndex(0)
            combobox.setFont(font)
            self.ui.tableWidget_6.setCellWidget(i, 1, combobox)
        self.ui.pushButton_5.clicked.connect(self.btn5)

    def btn1(self): #активируется при нажатии button
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


    def btn3(self): #активируется при нажатии button_3
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


    def btn2(self): #активируется при нажатии button_2
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
        lineedit_validator_table_added(table, spinBox_value)


    def btn4(self): #активируется при нажатии button_4
        _translate = QtCore.QCoreApplication.translate
        spinBox_value = self.ui.spinBox_2.value()
        table2 = self.ui.tableWidget_2
        table3 = self.ui.tableWidget_3
        table4 = self.ui.tableWidget_4
        table5 = self.ui.tableWidget_5
        table3.clear()
        table4.clear()
        table5.clear()
        try:
            matrix = table_value_get_lineedit(table2, spinBox_value)
        except AttributeError:
            return False
        iter_pow_list = math_module_lab2.object_pow(matrix)
        outbox_list = math_module_lab2.list_of_outbox(matrix)
        inbox_list = math_module_lab2.list_of_inbox(matrix)
        table3.setColumnCount(4)
        table3.setRowCount(spinBox_value)
        table3.setHorizontalHeaderLabels(('Номер пользователя', 'Итерационная сила порядка k',
                                        'Сила пользователя','Рейтинг пользователя'))
        table3.setFixedSize(391, 171)
        for x in range (spinBox_value):
            table3.setItem(x, 0, self.createItem(f'{iter_pow_list[x]["num"]}', Qt.ItemIsSelectable))
            table3.setItem(x, 1, self.createItem(f'{iter_pow_list[x]["pk"]}', Qt.ItemIsSelectable))
            table3.setItem(x, 2, self.createItem(f'{round(iter_pow_list[x]["iter_pow"],4)}', Qt.ItemIsSelectable))
        table3.sortItems(2,QtCore.Qt.DescendingOrder)
        for x in range(spinBox_value):
            table3.setItem(x, 3, self.createItem(f'{x+1}', Qt.ItemIsSelectable))
        table3.resizeColumnsToContents()
        table4.setColumnCount(3)
        table4.setRowCount(spinBox_value)
        table4.setFixedSize(391, 150)
        table4.setHorizontalHeaderLabels(('Номер пользователя', 'Количество сообщений', 'Доля сообщений'))
        for x in range (spinBox_value):
            table4.setItem(x, 0, self.createItem(f'{outbox_list[x]["num"]}', Qt.ItemIsSelectable))
            table4.setItem(x, 1, self.createItem(f'{outbox_list[x]["sum"]}', Qt.ItemIsSelectable))
            table4.setItem(x, 2, self.createItem(f'{round(outbox_list[x]["share"],4)}', Qt.ItemIsSelectable))
        table4.sortItems(2, QtCore.Qt.DescendingOrder)
        table4.resizeColumnsToContents()
        table5.setColumnCount(3)
        table5.setRowCount(spinBox_value)
        table5.setFixedSize(391, 150)
        table5.setHorizontalHeaderLabels(('Номер пользователя', 'Количество сообщений', 'Доля сообщений'))
        for x in range(spinBox_value):
            table5.setItem(x, 0, self.createItem(f'{inbox_list[x]["num"]}', Qt.ItemIsSelectable))
            table5.setItem(x, 1, self.createItem(f'{inbox_list[x]["sum"]}', Qt.ItemIsSelectable))
            table5.setItem(x, 2, self.createItem(f'{round(inbox_list[x]["share"], 4)}', Qt.ItemIsSelectable))
        table5.sortItems(2, QtCore.Qt.DescendingOrder)
        table5.resizeColumnsToContents()

    def btn5(self): #активируется при нажатии button_5
        table6 = self.ui.tableWidget_6
        table7 = self.ui.tableWidget_7
        table8 = self.ui.tableWidget_8
        table9 = self.ui.tableWidget_9
        comb_list = []
        for i in range(8):
            comb_list.append(table6.cellWidget(i, 1).currentText())
        print(comb_list)
        bin_list = math_module_lab2.comb_to_bin(comb_list)
        print(bin_list)
        for i in range(8):
            table6.setItem(i, 3, self.createItem(f'{bin_list[i]}', Qt.ItemIsSelectable))
        two_column_table_set(table7)
        table7.setItem(0, 2, self.createItem(f'{bin_list[1][0]}', Qt.ItemIsSelectable))
        table7.setItem(1, 2, self.createItem(f'{bin_list[5][0]}', Qt.ItemIsSelectable))
        table7.setItem(2, 2, self.createItem(f'{bin_list[4][0]}', Qt.ItemIsSelectable))
        table7.setItem(3, 2, self.createItem(f'{bin_list[7][0]}', Qt.ItemIsSelectable))
        two_column_table_set(table8)
        table8.setItem(0, 2, self.createItem(f'{bin_list[2][1]}', Qt.ItemIsSelectable))
        table8.setItem(1, 2, self.createItem(f'{bin_list[6][1]}', Qt.ItemIsSelectable))
        table8.setItem(2, 2, self.createItem(f'{bin_list[4][1]}', Qt.ItemIsSelectable))
        table8.setItem(3, 2, self.createItem(f'{bin_list[7][1]}', Qt.ItemIsSelectable))
        two_column_table_set(table9)
        table9.setItem(0, 2, self.createItem(f'{bin_list[3][2]}', Qt.ItemIsSelectable))
        table9.setItem(1, 2, self.createItem(f'{bin_list[6][2]}', Qt.ItemIsSelectable))
        table9.setItem(2, 2, self.createItem(f'{bin_list[5][2]}', Qt.ItemIsSelectable))
        table9.setItem(3, 2, self.createItem(f'{bin_list[7][2]}', Qt.ItemIsSelectable))
        self.ui.label_13.setText(logical_form(table7))
        self.ui.label_15.setText(logical_form(table8))
        self.ui.label_17.setText(logical_form(table9))





    def createItem(self, text, flags): #функция для добавления элементов в таблицы
        tableWidgetItem = QtWidgets.QTableWidgetItem(text)
        tableWidgetItem.setFlags(flags)
        return tableWidgetItem

    def clear_table(self): #очистка таблиц во второй задаче
        self.ui.tableWidget_3.setRowCount(0)
        self.ui.tableWidget_3.setColumnCount(0)
        self.ui.tableWidget_3.clear()
        self.ui.tableWidget_4.setRowCount(0)
        self.ui.tableWidget_4.setColumnCount(0)
        self.ui.tableWidget_4.clear()
        self.ui.tableWidget_5.setRowCount(0)
        self.ui.tableWidget_5.setColumnCount(0)
        self.ui.tableWidget_5.clear()



app = QtWidgets.QApplication(sys.argv)
application = mywindow()
application.show()

sys.exit(app.exec_())