import matplotlib.pyplot as plt
import numpy as np
from random import*
import time
import math

#SelectionSort
def SelectionSort(a):
    for i in range(0, len(a) - 1):
        min = i
        for j in range (i, len(a)):
            if a[j] < a[min]:
                min = j
        z = a[i]
        a[i] = a[min]
        a[min] = z

#InsertionSort
def InsertionSort(a):
    for i in range(1, len(a)):
        j = i 
        while (j > 0 and a[j - 1] > a[j]):
            tmp = a[j]
            a[j] = a[j - 1]
            a[j - 1] = tmp
            j = j - 1

#BubbleSort
def BubbleSort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if(a[j] > a[j + 1]):
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp

#MergeSort
def MergeList(a, b):
    m = len(a)
    n = len(b)
    c = []
    i = 0
    j = 0
    while(i < m and j < n):
        if(a[i] < b[j]):
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j = j + 1
    c = c + a[i:] + b[j:]
    return c

def MergeSort(a):
    n = len(a) // 2
    a1 = a[:n]
    a2 = a[n:]
    if (len(a1) > 1):
        a1 = MergeSort(a1)
    if (len(a2) > 1):
        a2 = MergeSort(a2)
    return MergeList(a1, a2)


#ShellSort
def ShellSort(a, gaps):
    n = len(a)
    for gap in gaps:
        for i in range(gap, n):
            j = i
            while(j >= gap and a[j - gap] > a[j]):
                a[j],a[j - gap] = a[j - gap],a[j]
                j = j - gap
    return a

def HibbardGaps(n):
    gaps = []
    k = 1
    i = 1
    while(i <= n):
        gaps.append(i)
        i = 2 ** k - 1
        k = k + 1
    gaps.reverse()
    return gaps

def ShellGaps(n):
    gaps = []
    i = n // 2
    while(i > 1):
        gaps.append(i)
        i = i // 2
    return gaps

def PrattGaps(n):
    gaps = []
    i = n
    for i in range(0, math.ceil(math.log(n, 2))):
        for j in range(0, math.ceil(math.log(n, 2))):
            if ((3 ** i) * (2 ** i) > n / 2):
                break
            else:
                gaps.append((3 ** i) * (2 ** j))
    gaps.sort(reverse=True)
    return gaps

#QuickSort
def QuickSort(a, left, right):
    if (left > right):
        return 
    p = a[(left + right) // 2]
    i = left
    j = right
    while(i <= j):
        while(a[i] < p):
            i = i + 1
        while(a[j] > p):
            j = j - 1
        if (i <= j):
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
            i = i + 1
            j = j - 1
    QuickSort(a, left, j)
    QuickSort(a, i, right)

#HeapSort
def Heap(a, n, i):
    maxi = i
    left = 2 * i + 1
    right = 2 * i + 2
    if (left < n and a[i] < a[left]):
        maxi = left
    if (right < n and a[i] < a[right]):
        maxi = right
    if(maxi != i):
        tmp = a[i]
        a[i] = a[maxi]
        a[maxi] = tmp
        Heap(a, n, maxi)
    
def HeapSort(a):
    n = len(a) 
    for i in range(n, -1, -1):
        Heap(a, n, i)
    for i in range(n - 1, 0, -1):
        tmp = a[i]
        a[i] = a[0]
        a[0] = tmp 
        Heap(a, i, 0)
