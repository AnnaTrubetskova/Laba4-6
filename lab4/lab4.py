from math import floor, ceil
from random import randint

class Matrix:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.__createMatrixA()
        self.__createMatrixF()

    def __createMatrixA(self):
        self.matrixA = []
        for i in range(self.n):
            self.matrixA.append([0] * self.n)
        for i in range(self.n):
            for j in range(self.n):
                self.matrixA[i][j] = randint(-10, 11)
    
    def createMatrixA(self, matrix):
        self.matrixA = []
        for i in range(self.n):
            self.matrixA.append([0] * self.n)
        for i in range(self.n):
            for j in range(self.n):
                self.matrixA[i][j] = matrix[i][j]
        self.__createMatrixF()
                
    def __createMatrixF(self):
        self.matrixF = []
        for i in range(self.n):
            self.matrixF.append([0] * self.n)
        for i in range(self.n):
            for j in range(self.n):
                self.matrixF[i][j] = self.matrixA[i][j]

    def __checkCondition1(self):
        counterNumber = 0
        sumNumbers = 0
        for i in range(0, ceil(self.n / 2)):
            for j in range(0, ceil(self.n / 2)):
                if (j >= i and j % 2 == 1 and self.matrixF[i][j] < self.k and j >= self.n - 1 - i - floor(self.n / 2)):
                    counterNumber += 1
                if (j >= i and i % 2 == 0 and j <= self.n - 1 - i - floor(self.n / 2)):
                    sumNumbers += self.matrixF[i][j]
        return (counterNumber > sumNumbers)
    
    def __swap23(self):
        for i in range(floor(self.n / 2), self.n):
            for j in range(floor(self.n / 2), self.n):
                if j >= i:
                    self.matrixF[i][j],self.matrixF[j][i] = self.matrixF[j][i],self.matrixF[i][j]
    
    def changeMatrixF(self):
        if self.__checkCondition1 == False:
            self.__swap23()
        else:
            self.__swapBE()
    
    def __swapBE(self):
        for i in range(0, ceil(self.n / 2)):
            for j in range(0, ceil(self.n / 2)):
                temp = self.matrixF[i][j]
                self.matrixF[i][j] = self.matrixF[i + floor(self.n / 2)][j + floor(self.n / 2)]
                self.matrixF[i + floor(self.n / 2)][j + floor(self.n / 2)] = temp

    def __transposeMatrix(self, matrix):
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    
    def __matrixMultiplication(self, matrix1, matrix2):
        length = len(matrix1) 
        resultMatrix = [[0 for i in range(length)] for i in range(length)]
        for i in range(length):
          for j in range(length):
            for k in range(length):
               resultMatrix[i][j] += matrix1[i][k] * matrix2[k][j]
        return resultMatrix
    
    def __multiplyNumberMatrix(self, k, matrix):
        for i in range(self.n):
            for j in range(self.n):
                matrix[i][j] *= k
        return matrix
    
    def __sumMatrix(self, matrix1, matrix2):
        result = [[matrix1[i][j] + matrix2[i][j]  for j in range
        (len(matrix1[0]))] for i in range(len(matrix1))] 
        return result
                
    def calculateResult(self):
        KA = self.__multiplyNumberMatrix(self.k, self.matrixA)
        KAF = self.__matrixMultiplication(KA, self.matrixF)
        At = self.__transposeMatrix(self.matrixA)
        KAt = self.__multiplyNumberMatrix(-self.k, At)
        result = self.__sumMatrix(KAF, KAt)
        return result

try:
    N = int(input('Введите N: '))
    K = int(input('Введите K: '))    
    matrix = Matrix(K, N)
    print('==========A==========')
    print(matrix.matrixA)
    print('==========F==========')
    print(matrix.matrixF)
    matrix.changeMatrixF()
    print('==========NEW F==========')
    print(matrix.matrixF)
    print('==========RESULT==========')
    print(matrix.calculateResult())
except:
    pass