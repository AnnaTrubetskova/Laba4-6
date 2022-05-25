# Author: Anna Trubetskova.
# Group: ISTbd-11.
# Option: 14.
# B   C
# D   E
# Task: Формируется матрица F следующим образом: скопировать в нее А и 
# если в В количество чисел, меньших К в нечетных столбцах больше, чем 
# сумма чисел в четных строках, то поменять местами С и Е симметрично, 
# иначе В и Е поменять местами несимметрично. При этом матрица А не 
# меняется. После чего если определитель матрицы А больше суммы 
# диагональных элементов матрицы F, то вычисляется выражение: 
# A-1*AT – K * F, иначе вычисляется выражение (A-1 +G-FТ)*K,
# где G-нижняя треугольная матрица, полученная из А.
# Выводятся по мере формирования А,
# F и все матричные операции последовательно.
from math import floor, ceil
import numpy as np

class Matrix:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.__createMatrix()
        self.printMatrixA()
        self.printMatrixF()
        
    def __createMatrix(self):
        self.matrixA = np.random.randint(-10, 11, size=(self.n, self.n)) # [-10; 11)
        self.matrixF = np.copy(self.matrixA)
    
    def changeMatrix(self, matrixA):
        self.matrixA = np.copy(matrixA)
        self.matrixF = np.copy(self.matrixA)
    
    def __checkCondition1(self):
        counterNumbers = 0
        sumNumbers = 0
        for i in range(0, ceil(self.n / 2)):
            for j in range(0, ceil(self.n / 2)):
                if (j % 2 == 1 and self.matrixF[i][j] < self.k):
                    counterNumbers += 1
                if (i % 2 == 0):
                    sumNumbers += self.matrixF[i][j]
                    
    def __checkCondition2(self):
        detA = np.linalg.det(self.matrixA)
        sumDiagonalElements = np.trace(self.matrixF)
        return (detA > sumDiagonalElements)   
                        
    def __swapCE(self):
        for i in range(0, ceil(self.n / 2)):
            for j in range(floor(self.n / 2), self.n):
                if (j > self.n - 1 - i):
                    temp = self.matrixF[i][j]
                    self.matrixF[i][j] = self.matrixF[self.n - 1 - i][self.n - 1 - j + floor(self.n / 2)]
                    self.matrixF[self.n - 1 - i][self.n - 1 - j + floor(self.n / 2)] = temp
    
    def __swapBE(self):
        for i in range(0, ceil(self.n / 2)):
            for j in range(0, ceil(self.n / 2)):
                temp = self.matrixF[i][j]
                self.matrixF[i][j] = self.matrixF[i + floor(self.n / 2)][j + floor(self.n / 2)]
                self.matrixF[i + floor(self.n / 2)][j + floor(self.n / 2)] = temp

    def run(self):
        if (self.__checkCondition1()):
            self.__swapCE()
            self.printMatrixF()
        else:
            self.__swapBE()
            self.printMatrixF()
        if (self.__checkCondition2()):
            self.result = np.linalg.matrix_power(self.matrixA, -1) * self.matrixA.transpose() - self.k * self.matrixF
        else:
            self.result = (np.linalg.matrix_power(self.matrixA, -1) + np.tril(self.matrixA) - np.linalg.matrix_power(self.matrixF, -1)) * self.k
        self.printResult()
            
    def printMatrixA(self):
        print('Matrix A:')
        print(self.matrixA)
        print('=========')
    
    def printMatrixF(self):
        print('Matrix F:')
        print(self.matrixF)
        print('=========')
            
    def printResult(self):
        print('Result:')
        print(self.result)
        print('=========')
        
K = int(input('Введите K: '))
N = int(input('Введите N: '))
matrix = Matrix(K, N)
matrix.run()