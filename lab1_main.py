# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
import numpy as np
from lab1_form import Ui_MainWindow
import math_module_lab1


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

def table_value_get(table,size=5): #записывает значение таблицы из комбобоксов в массив
    table_matrix = np.empty((size,size))
    for i in range(size):
        for j in range(size):
            table_matrix[i][j] = table.cellWidget(i,j).currentText()
    return table_matrix

def table_value_set(self,table_matrix, table, size=5): #записывает значение из массива в таблицу
    for row in range(size):
        for column in range(size):
            table.setItem(row,column, QtWidgets.QTableWidgetItem(f'{int(table_matrix[row][column])}'))







class mywindow(QtWidgets.QMainWindow): #класс приложения
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btn1)
        combobox_table_added(self.ui.tableWidget_2,5)
        self.ui.comboBox.activated[str].connect(self.combobox1)
        self.ui.pushButton_2.clicked.connect(self.btn2)
        self.ui.pushButton_3.clicked.connect(self.btn3)
        self.ui.pushButton_4.clicked.connect(self.btn4)
        self.ui.checkBox.stateChanged.connect(lambda: self.clear_textedit(self.ui.checkBox, self.ui.textEdit))
        self.ui.checkBox_2.stateChanged.connect(lambda: self.clear_textedit(self.ui.checkBox_2, self.ui.textEdit))
        self.ui.checkBox_3.stateChanged.connect(lambda: self.clear_textedit(self.ui.checkBox_3, self.ui.textEdit))
        self.ui.checkBox_4.stateChanged.connect(lambda: self.clear_textedit(self.ui.checkBox_4, self.ui.textEdit))
        self.ui.checkBox_5.stateChanged.connect(lambda: self.clear_textedit(self.ui.checkBox_5, self.ui.textEdit))
        self.ui.checkBox_6.stateChanged.connect(lambda: self.clear_textedit(self.ui.checkBox_6, self.ui.textEdit))
        self.ui.checkBox_7.stateChanged.connect(lambda: self.clear_textedit(self.ui.checkBox_7, self.ui.textEdit))



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
            table.setRowHeight(i,table.height() // spinBox_value)
        combobox_table_added(table,spinBox_value)



    def combobox1(self, text): #показ или скрытие второй таблицы в зависимости от операции
        table2 = self.ui.tableWidget_2
        table3 = self.ui.tableWidget_3
        if text == 'Включение' or text == 'Дополнение' or text == 'Обратное'or text == 'Двойственности':
            table3.setEnabled(False)
            table3.clear()
            table3.hide()
            combobox_table_added(table2,5)
        else:
            combobox_table_added(table2,5)
            combobox_table_added(table3,5)
            table3.setEnabled(True)
            table3.show()

    def btn2(self):  #активируется при нажатии button_2
        table2 = self.ui.tableWidget_2
        table3 = self.ui.tableWidget_3
        table4 = self.ui.tableWidget_4
        text = self.ui.comboBox.currentText()
        table2_matrix = table_value_get(table2)
        if text == "Пересечение" or text == "Объединение" or text == "Произведение":
            table3_matrix = table_value_get(table3)
            if text == "Пересечение":
                result_matrix = math_module_lab1.intersection(table2_matrix,table3_matrix)
            elif text == "Объединение":
                result_matrix = math_module_lab1.union(table2_matrix,table3_matrix)
            elif text == "Произведение":
                result_matrix = math_module_lab1.composition(table2_matrix,table3_matrix)
        elif text == "Включение":
            result_matrix = math_module_lab1.inclusion(table2_matrix)
        elif text == "Дополнение":
            result_matrix = math_module_lab1.addition(table2_matrix)
        elif text == "Обратное":
            result_matrix = math_module_lab1.opposite(table2_matrix)
        elif text == "Двойственности":
            result_matrix = math_module_lab1.duality(table2_matrix)
        table_value_set(self, result_matrix, table4)

    def btn3(self):  #активируется при нажатии button_3
        table5 = self.ui.tableWidget_5
        table5_matrix= np.empty((4,4))
        for i in range(4):
            for j in range(4):
                if j > i:
                    table5_matrix[i][j] = 1
                else:
                    table5_matrix[i][j] = 0
        table_value_set(self, table5_matrix,table5,size=4)
        if(math_module_lab1.antireflexivity(table5_matrix)):
            self.ui.lineEdit.setText('+')
        else:
            self.ui.lineEdit.setText('-')
        if (math_module_lab1.asymmetry(table5_matrix)):
            self.ui.lineEdit_2.setText('+')
        else:
            self.ui.lineEdit_2.setText('-')

    def btn4(self):  #активируется при нажатии button_4
        textEdit = self.ui.textEdit
        table6 = self.ui.tableWidget_6
        list_of_checkboxes = [self.ui.checkBox, self.ui.checkBox_2, self.ui.checkBox_3, self.ui.checkBox_4,
                            self.ui.checkBox_5, self.ui.checkBox_6, self.ui.checkBox_7]
        list_of_properties = [math_module_lab1.reflexivity,math_module_lab1.antireflexivity,math_module_lab1.symmetry,
                              math_module_lab1.asymmetry,math_module_lab1.antisymmetry,math_module_lab1.transitivity,
                              math_module_lab1.acyclicity_graph]
        index_property = [i for i in range(len(list_of_checkboxes)) if list_of_checkboxes[i].isChecked()]

        if textEdit.isVisible():
            textEdit.setText(' ')
        if len(index_property) == 0:
            textEdit.clear()
            table6.clear()
            return False
        elif 0 in index_property and 1 in index_property:
            textEdit.show()
            textEdit.setText("Рефлексивность и антирефлексивность несовместимы!")
            return False
        elif 2 in index_property and 3 in index_property:
            textEdit.show()
            textEdit.setText("Симметричность и асимметричность несовместимы!")
            return False
        elif 2 in index_property and 4 in index_property:
            textEdit.show()
            textEdit.setText("Симметричность и антисимметричность несовместимы!")
            return False
        elif 0 in index_property and 6 in index_property :
            textEdit.show()
            textEdit.setText("Рефлексивность и ацикличность несовместимы!")
            return False
        elif 0 in index_property and 3 in index_property :
            textEdit.show()
            textEdit.setText("Рефлексивность и асимметричность несовместимы!")
            return False
        elif 2 in index_property and 6 in index_property :
            result_matrix = np.zeros((5,5))
            table_value_set(self,result_matrix,table6)
            return True

        success_matrix = False
        while not success_matrix:
            result_matrix = math_module_lab1.random_bin_matrix(5)
            print(result_matrix)
            success_matrix = True
            for i in index_property:
                if not list_of_properties[i](result_matrix):
                    success_matrix = False
                    break
        table_value_set(self, result_matrix, table6)
        textEdit.setText('Матрица сгенерирована')

    def clear_textedit(self, qcheckbox, qtextedit): #очистка таблицы и тексэдита при изменении значения чекбокса
        self.ui.tableWidget_6.clear()
        qtextedit.clear()






app = QtWidgets.QApplication(sys.argv)
application = mywindow()
application.show()

sys.exit(app.exec_())