import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
import numpy as np
from lab3_form import Ui_MainWindow



def table_value_get_lineedit(table): #добавление лайнэдитов в таблицу
    table_matrix = np.empty((3, 4))
    for i in range(3):
        for j in range(4):
            table_matrix[i][j] = int(table.cellWidget(i, j).text())
    return table_matrix

def pessimism_coefficient(self): #запись значения коэффициента пессимизма в переменную
    prob_text = self.ui.lineEdit.text()
    prob_text = prob_text.replace(',', '.')
    if float(prob_text) >= 1:
        self.ui.lineEdit.setText('1')
        return 1
    else:
        return float(prob_text)


def Hurwitz_coefficient(self,table_matrix,pess_coef): #вычисление значения Si Коэффициента Гурвица
    min_hurw_coef = []
    max_hurw_coef = []
    for rows in table_matrix:
        min_hurw_coef.append(min(rows))
        max_hurw_coef.append(max(rows))
    hurw_coef = []
    for i in range(3):
        hurw_coef.append(pess_coef * min_hurw_coef[i] + (1 - pess_coef) * max_hurw_coef[i])
    return min_hurw_coef, max_hurw_coef, hurw_coef



class mywindow(QtWidgets.QMainWindow): #класс приложения
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.setVerticalHeaderLabels(['x1','x2','x3'])
        self.ui.tableWidget.setHorizontalHeaderLabels(['y1','y2','y3','y4','min(aij)','max(aij)',
                                                       'Si'])
        self.ui.lineEdit.setValidator(QtGui.QDoubleValidator(0.0, 1.0, 2, parent = None))
        for i in range(3):
            self.ui.tableWidget.setItem(i, 4, self.createItem(f'', Qt.ItemIsSelectable))
            self.ui.tableWidget.setItem(i, 5, self.createItem(f'', Qt.ItemIsSelectable))
            self.ui.tableWidget.setItem(i, 6, self.createItem(f'', Qt.ItemIsSelectable))
            lineedit = QtWidgets.QLineEdit()
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            lineedit.setValidator(QtGui.QIntValidator(0, 999, parent=None))
            lineedit.setFont(font)
            lineedit_2 = QtWidgets.QLineEdit()
            lineedit_2.setValidator(QtGui.QIntValidator(0, 999, parent=None))
            lineedit_2.setFont(font)
            lineedit_3 = QtWidgets.QLineEdit()
            lineedit_3.setValidator(QtGui.QIntValidator(0, 999, parent=None))
            lineedit_3.setFont(font)
            lineedit_4 = QtWidgets.QLineEdit()
            lineedit_4.setValidator(QtGui.QIntValidator(0, 999, parent=None))
            lineedit_4.setFont(font)
            self.ui.tableWidget.setCellWidget(i, 0, lineedit)
            self.ui.tableWidget.setCellWidget(i, 1, lineedit_2)
            self.ui.tableWidget.setCellWidget(i, 2, lineedit_3)
            self.ui.tableWidget.setCellWidget(i, 3, lineedit_4)
        self.ui.pushButton.clicked.connect(self.btn1)


    def btn1(self): #активируется при нажатии button
        table = self.ui.tableWidget
        try:
            table_matrix = table_value_get_lineedit(table)
        except ValueError:
            return False
        print(table_matrix)
        pess_coef = pessimism_coefficient(self)
        print(pess_coef)
        min_value, max_value, hurf_coef = Hurwitz_coefficient(self, table_matrix, pess_coef)
        for i in range(3):
            self.ui.tableWidget.setItem(i, 4, self.createItem(f'{int(min_value[i])}', Qt.ItemIsSelectable))
            self.ui.tableWidget.setItem(i, 5, self.createItem(f'{int(max_value[i])}', Qt.ItemIsSelectable))
            self.ui.tableWidget.setItem(i, 6, self.createItem(f'{round(hurf_coef[i],3)}', Qt.ItemIsSelectable))
        self.ui.label_4.setText(f'Критерий Гурвица является критерием пессимизма - оптимизма.' 
                                f'За оптимальную принимается та стратегия, для которой выполняется '
                                f'соотношение: max(si),\nгде si = y min(aij) + (1-y)max(aij))\n'
                                f'Выбираем из {str([round(i,3) for i in hurf_coef])} '
                                f'максимальный элемент max = {round(max(hurf_coef),3)}\n'
                                f'Вывод: выбираем стратегию N = {hurf_coef.index(max(hurf_coef)) + 1}')














    def createItem(self, text, flags):  # функция для добавления элементов в таблицы
        tableWidgetItem = QtWidgets.QTableWidgetItem(text)
        tableWidgetItem.setFlags(flags)
        return tableWidgetItem










app = QtWidgets.QApplication(sys.argv)
application = mywindow()
application.show()

sys.exit(app.exec_())