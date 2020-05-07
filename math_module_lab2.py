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





matrix = np.array([[0,0,0,0],
                  [1,0,0,0],
                  [1,0,1,1],
                  [1,0,0,1]])
print(set_of_maximum(matrix))
print(set_of_minimum(matrix))
print(set_of_majorant(matrix))
print(set_of_minorant(matrix))