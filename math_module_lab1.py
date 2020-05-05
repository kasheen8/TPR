# -*- coding: utf-8 -*-

import numpy as np
from itertools import chain, groupby

def random_bin_matrix(n): #возвращает рандомную бинарную матрицу нужного размера
    return np.random.randint(0,2,(n,n))

def inclusion(matrix): #возвращает отношение, в которое включено исходное
    size = len(matrix)
    inclusion_matrix = np.empty((size,size))
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 0:
                inclusion_matrix[i][j] = np.random.randint(0,2)
            else:
                inclusion_matrix[i][j] = 1
    return inclusion_matrix

def addition(matrix): #возвращает дополнение отношения
    size = len(matrix)
    addition_matrix = np.empty((size,size))
    for i in range(size):
        for j in range(size):
            addition_matrix[i][j] = 1 - matrix[i][j]
    return addition_matrix

def opposite(matrix): #возвращаает обратное отношение
    return np.transpose(matrix)

def intersection(matrix1, matrix2): #возвращает пересечение отношений
    size = len(matrix1)
    intersection_matrix = np.empty((size,size))
    for i in range(size):
        for j in range(size):
            intersection_matrix[i][j] = matrix1[i][j] and matrix2[i][j]
    return intersection_matrix

def union(matrix1, matrix2): #возвращает объединение отношений
    size = len(matrix1)
    union_matrix = np.empty((size,size))
    for i in range(size):
        for j in range(size):
            union_matrix[i][j] = matrix1[i][j] or matrix2[i][j]
    return union_matrix

def composition(matrix1, matrix2): #возвращает произведение отношений
    size = len(matrix1)
    compos_matrix = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            if matrix1[i][j] == 1:
                for k in range(size):
                    if matrix2[j][k] == 1:
                        compos_matrix[i][k] = 1
    return compos_matrix

def duality(matrix): #возвращает отношения двойственности
    return(addition(opposite(matrix)))


def reflexivity(matrix): #проверка отношения на рефлексивность
    size = len(matrix)
    for i in range(size):
        if matrix[i][i] == 0:
            return False
    return True

def antireflexivity(matrix): #проверка отношения на антирефлексивность
    size = len(matrix)
    for i in range(size):
        if matrix[i][i] == 1:
            return False
    return True

def symmetry(matrix): #проверка отношения на симметриченость
    if (matrix == np.transpose(matrix)).all():
        return True
    else:
        return False


def asymmetry(matrix): #проверка отношения на асимметриченость
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == matrix[j][i] == 1:
                return False
    return True


def antisymmetry(matrix): #проверка отношения на антисимметричность
    size = len(matrix)
    antisymm_matrix = matrix * np.transpose(matrix)
    for i in range(size):
        for j in range(size):
            if antisymm_matrix[i][j] == 1 and i != j:
                return False
    return True

def transitivity(matrix): #проверка отношения на транзитивность
    size = len(matrix)
    trans_matrix = composition(matrix,matrix)
    for i in range(size):
        for j in range(size):
            if trans_matrix[i][j] == 1 and matrix[i][j] == 0:
                return False
    return True

def acyclicity(matrix): #проверка отношения на ацикличность
    size = len(matrix)
    oppos_matrix = opposite(matrix)
    current_matrix = matrix[:]
    print(oppos_matrix)
    print(intersection(matrix, oppos_matrix))
    if intersection(matrix, oppos_matrix).any():
        return False
    compos_matrix=composition(matrix,matrix)
    while((compos_matrix == current_matrix).all()):
        print(matrix)
        print(compos_matrix)
        print('*'*20)
        matrix = compos_matrix[:]
        compos_matrix = composition(compos_matrix,matrix)
        if intersection(matrix,oppos_matrix).any():
            return False
    return True

def acyclicity_graph(matrix): #проверка отношения на ацикличность методом графа
    size = len(matrix)
    E = []
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 1:
                E.append((i+1,j+1))
    graph = {}
    for k, it in groupby(sorted(E), key=lambda x: x[0]):
        graph[k] = {e for _, e in it}

    # отрубаем все вершины которые не могут быть частью цикла (имеющие только входящие или только выходящие ребра)
    sub_graph = {}
    while True:
        vertex_set = set(graph).intersection(chain.from_iterable(graph.values()))
        sub_graph = {k: vertex_set & vs for k, vs in graph.items()
                     if k in vertex_set and vertex_set & vs}

        if sub_graph == graph:
            break
        else:
            graph = sub_graph

    # Если есть подграф то он цикличен
    if graph:
        return False
    else:
        return True










if __name__ == '__main__':
    matr = random_bin_matrix(5)
    # print(matr)
    # print(matr[:])
    # print(composition(matr,matr))
    # print(opposite(matr))
    # print(composition(composition(matr,matr),matr))
    # print(composition(composition(composition(matr,matr),matr),matr))
    # print(inclusion(matr))
    # print(addition(matr))
    # print(opposite(matr))
    # matrix1 = random_bin_matrix(4)
    # print(matrix1)
    # matrix2 = random_bin_matrix(4)
    # print(matrix2)
    # #print(intersection(matrix1,matrix2))
    # #print(union(matrix1,matrix2))
    # print(composition(matrix1,matrix2))
    # print(duality(matr))
    while(True):
       if (symmetry(matr) and acyclicity_graph(matr) and transitivity(matr)):
           break
       matr = random_bin_matrix(5)
       print(matr)

