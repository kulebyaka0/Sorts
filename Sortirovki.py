import matplotlib.pyplot as plt

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

#ComparisonSort
# def ComparisonSort(a)

#InsertionSort
def InsertionSort(a):
    for i in range(1, len(a)):
        j = i 
        while (j > 0 and a[j - 1] > a[j]):
            z = a[j]
            a[j] = a[j - 1]
            a[j - 1] = z
            j = j - 1

#BubbleSort
def BubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a) - i):
            if(a[j] > a[j + 1]):
                tmp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = tmp
        

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

#ShellSort
def ShellSort(a, gaps):
    n = len(a)
    for gap in gaps:
        for i in range(gap, n):
            j = i
            a1 = a[i]
            while(j >= 1 and a[j - 1] > a1):
                a[j] = a[j - 1]
                j = j - 1
            a[j] = a1
    return a

def ShellGaps(n):
    gaps = []
    i = n // 2
    gaps.append(i)
    while(i > 1):
        i = i // 2
        gaps.append(i)
    return gaps


n = [8, 4, 6, 1, 4, 0]

#InsertionSort(n)

#SelectionSort(n)

#n = MergeSort(n)

# left = 0
# right = len(n) - 1
# QuickSort(n, left, right)

#ShellSort(n, ShellGaps(len(n)))

BubbleSort(n)

print(n)