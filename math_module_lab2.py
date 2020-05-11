# -*- coding: utf-8 -*-

import numpy as np

def set_of_maximum(matrix):
    size = len(matrix)
    array_of_maximum = []
    for i in range(size):
        Maximum = True
        for j in range(size):
            if matrix[i][j] == 0:
                Maximum = False
        if Maximum:
            array_of_maximum.append(i+1)
    return array_of_maximum

def set_of_minimum(matrix):
    size = len(matrix)
    array_of_minimum = []
    for j in range(size):
        Minimum = True
        for i in range(size):
            if matrix[i][j] == 0:
                Minimum = False
        if Minimum:
            array_of_minimum.append(j + 1)
    return array_of_minimum

def set_of_majorant(matrix):
    size = len(matrix)
    array_of_majorant = []
    for j in range(size):
        Majorant = True
        for i in range(size):
            if matrix[i][j] == 1:
                Majorant = False
        if Majorant:
            array_of_majorant.append(j+1)
    return array_of_majorant

def set_of_minorant(matrix):
    size = len(matrix)
    array_of_minorant = []
    for i in range(size):
        Minorant = True
        for j in range(size):
            if matrix[i][j] == 1:
                Minorant = False
        if Minorant:
            array_of_minorant.append(i+1)
    return array_of_minorant


def iter_pow_of_order_k(row, pk):
    iter_pow = 0
    for num in row:
        if num != '∞':
            iter_pow += int(num) * pk
    return iter_pow


def object_pow(matrix):
    size = len(matrix)
    pow_list = []
    for i in range(size):
        record = {'num': i+1, 'pk': 1, 'iter_pow': 0}
        pow_list.append(record)
    for num in range(size):
        for row in range(size):
            it_pow = iter_pow_of_order_k(matrix[row], pow_list[row]['pk'])
            pow_list[row]['pk'] = it_pow
    iter_pow_sum = 0
    for i in range(size):
        iter_pow_sum += pow_list[i]['pk']
    for i in range(size):
        pow_list[i]['iter_pow'] = pow_list[i]['pk'] / iter_pow_sum
    return pow_list

def list_of_outbox(matrix):
    size = len(matrix)
    outbox_list = []
    for row in range(size):
        sum = 0
        for num in matrix[row]:
            if num != '∞':
                sum += int(num)
        record = {}
        record['num'] = row+1
        record['sum'] = sum
        outbox_list.append(record)
    sum_outbox = 0
    for i in range(size):
        sum_outbox += outbox_list[i]['sum']
    for i in range(size):
        outbox_list[i]['share'] = outbox_list[i]['sum'] / sum_outbox
    return(outbox_list)


def list_of_inbox(matrix):
    size = len(matrix)
    inbox_list = []
    for j in range(size):
        sum = 0
        for i in range(size):
            if matrix[i][j] != '∞':
                sum += int(matrix[i][j])
        record = {}
        record['num'] = j+1
        record['sum'] = sum
        inbox_list.append(record)
    sum_inbox = 0
    for i in range(size):
        sum_inbox += inbox_list[i]['sum']
    for i in range(size):
        inbox_list[i]['share'] = inbox_list[i]['sum'] / sum_inbox
    return(inbox_list)

def comb_to_bin(comb_list):
    size = len(comb_list)
    bin_list = []
    for i in range(size):
        elem = ['0','0','0']
        if 'X1' in comb_list[i]:
            elem[0] = '1'
        if 'X2' in comb_list[i]:
            elem[1] = '1'
        if 'X3' in comb_list[i]:
            elem[2] = '1'
        elem = ''.join(elem)
        bin_list.append(elem)
    return bin_list

def bin_result(bin_list):
    if bin_list.count('1') == 0:
        return '0'
    elif bin_list.count('1') == 4:
        return '1'
    elif bin_list.count('1') == 1:
        if bin_list == ['0', '0', '0', '1']:
            return '+∧+'
        elif bin_list == ['0','0','1','0']:
            return '+∧-'
        elif bin_list == ['0','1','0','0']:
            return '-∧+'
        elif bin_list == ['1','0','0','0']:
            return '-∧-'
    elif bin_list.count('1') == 3:
        if bin_list == ['1','1','1','0']:
            return '-∨-'
        if bin_list == ['1','1','0','1']:
            return '-∨+'
        if bin_list == ['1','0','1','1']:
            return '+∨-'
        if bin_list == ['0','1','1','1']:
            return '+∨+'
    elif bin_list.count('1') == 2:
        if bin_list == ['1','1','0','0']:
            return '(-∧+)∨(-∧-)'
        if bin_list == ['1','0','0','1']:
            return '(+∧+)∨(-∧-)'
        if bin_list == ['1','0','1','0']:
            return '(+∧-)∨(-∧-)'
        if bin_list == ['0','0','1','1']:
            return '(+∧-)∨(+∧+)'
        if bin_list == ['0','1','1','0']:
            return '(+∧-)∨(-∧+)'
        if bin_list == ['0','1','0','1']:
            return '(+∧+)∨(-∧+)'







if __name__ == '__main__':
    matrix = np.array([['∞',19,54,15],
                      [26,'∞',0,18],
                      [3,0,'∞',47],
                      [93,0,53,'∞']])
    # print(set_of_maximum(matrix))
    # print(set_of_minimum(matrix))
    # print(set_of_majorant(matrix))
    # print(set_of_minorant(matrix))
    print(iter_pow_of_order_k(matrix[0],1), iter_pow_of_order_k(matrix[1],1),iter_pow_of_order_k(matrix[2],1),iter_pow_of_order_k(matrix[3],1))
    object_pow(matrix)
    print(list_of_outbox(matrix))
    list_of_inbox(matrix)