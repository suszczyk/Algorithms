import time
import numpy as np
import matplotlib.pyplot as plt
import random
import math

def shell_generator():
    gap = len(a)//2
    k = 2
    while gap != 1:
        yield gap
        gap = gap/k
        # print(gap)
        gap = math.floor(gap)


def shell():
    shell = []
    for el in shell_generator():
        shell.append(el)
    shell.append(1)
    return shell


def threesmooth_generator():
    S = [1]
    i2 = 0
    i3 = 0
    while True:
        yield S[-1]
        n2 = 2 * S[i2]
        n3 = 3 * S[i3]
        S.append(min(n2, n3))
        i2 += n2 <= n3
        i3 += n2 >= n3


def smooth():
    smooth_inc = []
    smooth_dec = []
    for el in threesmooth_generator():
        # print(el)
        if el > len(a):
            break
        smooth_inc.append(el)

    for i in range(len(smooth_inc)-1, -1, -1):
        smooth_dec.append(smooth_inc[i])
    return smooth_dec


def sedgewick_generator():
    yield 1
    n = 0
    while True:
        yield pow(4, n+1)+3*pow(2, n)+1
        n = n+1


def sedgewick():
    sedgewick_inc = []
    sedgewick_dec = []
    for el in sedgewick_generator():
        if el > len(a):
            break
        sedgewick_inc.append(el)
        # print(el)

    for i in range(len(sedgewick_inc)-1, -1, -1):
        sedgewick_dec.append(sedgewick_inc[i])
    return sedgewick_dec


def tokuda_generator():
    yield 1
    n = 0
    while True:
        yield math.ceil((9 * (9/4)**n - 4) / 5)
        n = n+1


def tokuda():
    tokuda_inc = []
    tokuda_dec = []
    for el in tokuda_generator():
        if el > len(a):
            break
        tokuda_inc.append(el)

    for i in range(len(tokuda_inc)-1, -1, -1):
        tokuda_dec.append(tokuda_inc[i])
    return tokuda_dec


def prime_generator(N):
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False
    return True


def prime():
    prime_inc = []
    prime_dec = []
    for i in range(2, len(a)):
        if prime_generator(i) == True:
            prime_inc.append(i)

    for i in range(len(prime_inc)-1, -1, -1):
        prime_dec.append(prime_inc[i])
    prime_dec.append(1)
    return prime_dec


def tribonacci_generator():
    yield 0
    yield 1
    yield 1
    seq = [0, 1, 1]
    while True:
        sum = seq[-1] + seq[-2] + seq[-3]
        yield sum
        seq.append(sum)
        # print(seq)


def tribonacci():
    tribonacci_inc = []
    tribonacci_dec = []
    for el in tribonacci_generator():
        # print(el)
        if el > len(a):
            break
        tribonacci_inc.append(el)

    for i in range(len(tribonacci_inc)-1, -1, -1):
        tribonacci_dec.append(tribonacci_inc[i])
    return tribonacci_dec


def InsertSortStep(tab, step):
    for i in range(1, len(tab)):
        a = tab[i]
        k = i-step
        while(a < tab[k] and k >= 0):
            tab[k+step] = tab[k]
            k = k-step
        tab[k+step] = a
    return tab


def comb_sort(arr, shrink):
    length = len(arr)
    gap = length
    sorted = False

    while not sorted:
        gap = int(gap/shrink)
        if gap <= 1:
            sorted = True
            gap = 1

        for i in range(length-gap):
            sm = gap + i
            if arr[i] > arr[sm]:
                arr[i], arr[sm] = arr[sm], arr[i]
                sorted = False


def comb():
    lista = []
    lista.append(1.3)
    return lista


def isSorted(l):
    i = 1
    while i < len(l):
        if l[i] < l[i-1]:
            return False
        i = i+1
    return True


sorts = [
    {
        "name": "Shell",
        "sort": lambda arr: InsertSortStep(arr, gap),
        "gap": shell
    },

    {
        "name": "Smooth",
        "sort": lambda arr: InsertSortStep(arr, gap),
        "gap": smooth
    },
    {
        "name": "Sedgewick",
        "sort": lambda arr: InsertSortStep(arr, gap),
        "gap": sedgewick
    },
    {
        "name": "Tokuda",
        "sort": lambda arr: InsertSortStep(arr, gap),
        "gap": tokuda
    },
    {
        "name": "Liczby pierwsze",
        "sort": lambda arr: InsertSortStep(arr, gap),
        "gap": prime
    },
    {
        "name": "Tribonacci",
        "sort": lambda arr: InsertSortStep(arr, gap),
        "gap": tribonacci
    },
    {
        "name": "Sortowanie grzebieniowe",
        "sort": lambda arr: comb_sort(arr, gap),
        "gap": comb
    }
]


k_thousands = 100

elements = np.array([i*k_thousands*100 for i in range(1, 11)])
plt.xlabel('List length')
plt.ylabel('Time (s)')

for sort in sorts:
    # print(sort)
    times = list()
    start_all = time.time()
    for i in range(1, 11):
        a = []
        for n in range(i*k_thousands*100):
            a.append(random.randrange(1, i*k_thousands*100))
        gaps = sort["gap"]()
        print(gaps)
        start = time.time()
        for gap in gaps:
            sort["sort"](a)
        end = time.time()
        times.append(end - start)
        # print(times)
        print(sort["name"], "Sorted", i*k_thousands*100, "Elements in", end - start, "s")
        end_all = time.time()
        print(sort["name"], "Sorted Elements in", end_all - start_all, "s")

        isSorted(a)
        if isSorted(a) == True:
            print("Sorted")
        else:
            print("Not sorted")
            print(a)
            break

    # print(tab)
    plt.plot(elements, times, label=sort["name"])

plt.grid()
plt.legend()
plt.show()