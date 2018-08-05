#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

The occurrence of all integer natural divisors of getting number N, faster than usual
                                                                    -----------------
The module is intended for importing
##################################################################################

Модуль предназначен для нахождения всех целых натуральных делителей
заданного числа N

В модуле определены вспомогающие функции, которые можно импортировать,
но на которых можно забить и зделать просто так:
############################################
# listAllDivisors = makeListAllDivisors(N) #
############################################
где N - натуральеое число, делители которого нужно найти
--------------------------

Здесь задействован более производительный алгоритм нахождения
делителей числа, где вместо обычного перебора цикла от 1 до N(или до N//2 + 1)
применяются математические формулы, которые я нашёл на просторах
интернета

Например, если ввести большое число 2000000, то его делители
НАМОГО БЫСТРЕЕ посчитаются, чем обычный перебор
"""


from functools import reduce

def isPrime(n):
    """
    Логическая функция (возвращает True or False)
    Является ли число n - простым 
    """
    k = 2
    while k*k < n and n%k != 0:
        k+=1
    return n > 1 and  k*k > n
    
def genPrime(n):
    """
    Генерирует простые числа, расположенные на отрезке  [2, n]
    """
    for num in range(2, n+1):
        if isPrime(num): yield num

def genPrimeDivisors(n):
    """
    Возвращает итеррируемый объект
    Функция генерирует за раз простые делители числа n
    """
    for primeDivader in genPrime(n):

        while n % primeDivader == 0:
            yield primeDivader
            n //= primeDivader

        if isPrime(n):
            yield n
            n = 1

        if n == 1:
            break

def makeDictPrimeDivisors(n):
    """
    Возвращает словарь ПРОСТЫХ делителй чилса n
    где ключи - это уникальные простые делители,
    а значения - это количество таких делителей в числе
    """

    # итеррируемый оъект ПРОСТЫХ делителей числа n 
    #---------------------------------------------
    divisors = list(genPrimeDivisors(n))
    # print(*divisors)
    #---------------------------------------------

    # множество уникальных простых делитель
    #---------------------------------------------
    unic = set(divisors)
    # print(unic, len(unic))
    #---------------------------------------------

    # словарь, где ключи - это уникальные простые делители,
    # а значения - это количество таких делителей в числе
    #---------------------------------------------
    d = {num : divisors.count(num) for num in unic}
    # print(d)
    #---------------------------------------------
    return d

def genSeqSeqs(d : dict):
    for num in d:
        temp = []
        for i in range(d[num] + 1):
            temp.append(num**i)
        # print(temp)
        yield temp
    

def multiplySeqs(seqBase, seqNext):
    k = []
    for i in seqBase:
        for j in seqNext:
            k.append(i*j)
    return k

def makeListAllDivisors(n : int):
    """
    Функция возвращает список всех натуральный делителей числа n
    """
    if n == 1:
        return [1]
    d = makeDictPrimeDivisors(n)
    m = genSeqSeqs(d)
    listAllDivisors = reduce(multiplySeqs, m)
    return sorted(listAllDivisors)

def main():
    n = int(input("Enter your natural number: "))
    print('-'*40)
    listAllDivisors = makeListAllDivisors(n)
    print('List of all natural integer divisors of the number', str(n) + ':')
    print(*listAllDivisors)

if __name__ == "__main__":
    main()