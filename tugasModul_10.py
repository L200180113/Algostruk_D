#No 1
from timeit import timeit
import random
#a)
def jumlahkan_cara_1(n):
    hasilnya = 0
    for i in range(1, n+1):
        hasilnya += i
    return hasilnya
#b)
def jumlahkan_cara_2(n):
    return (n*(n+1))/2
#c)
def insertionsort(a):
    for i in range(1, len(a)):
        nilai = a[i]
        b = i
        while b > 0 and nilai < a[b - 1]:
            a[b] = a[b-1]
            b -= 1
        a[b] = nilai

x = 1000
y = [3, 4, 2, 1, 2, 5, 9, 3]

def jml1():
    jumlahkan_cara_1(x)
def jml2():
    jumlahkan_cara_2(x)
def inst():
    insertionsort(y)

if __name__ == '__main__':
    import timeit
    print("jumlahkan cara 1 timeit")
    print(timeit.timeit("jml1()", setup="from __main__ import jml1"))
    print("jumlahkan cara 2 timeit")
    print(timeit.timeit("jml2()", setup="from __main__ import jml2"))
    print("insertionSort timeit")
    print(timeit.timeit("inst()", setup="from __main__ import inst"))

No 2
import random
import time
RUN = 32

def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []

    for i in range(0, len1):
        left.append(arr[l + i])

    for i in range(0, len2):
        right.append(arr[m + 1 + i])
    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1
def insertionSort(arr, left, right):
    for i in range(left + 1, right+1):
        temp = arr[i]
        j = i - 1
        while j >= left and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
def timSort(arr, n):
    for i in range(0, n, RUN):
        insertionSort(arr, i, min((i+31), (n-1)))

    size = RUN
    while size < n:
        for left in range(0, n, 2*size):
            mid = left + size - 1
            right = min((left + 2*size - 1), (n-1))
            merge(arr, left, mid, right)
        size = 2*size
g = [5, 21, 7, 23, 19]
n = len(g)
print("g = ", g)
z = [5, 21, 7, 23, 19]
print("z = ", z)
a = [9, 5, 4, 6, 8, 1, 2]
print("a=", a)
# timsort
timSort(g, len(g))
print("timsort")
print("g = ", g)
# a.sort()
print("a.sort()")
a.sort()
print("a=", a)
# Sorted
z = [5, 21, 7, 23, 19]
print("sorted")
sorted(z)
print("z = ", z)
# Bestcase
for i in range(3):
        L = list(range(3000))
        awal = time.time()
        U = sorted(L)
        akhir = time.time()
        print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik"
              %(len(L), akhir - awal))
print("\n")
# Average Case
for i in range(3):
        L = list(range(3000))
        random.shuffle(L)
        awal = time.time()
        U = sorted(L)
        akhir = time.time()
        print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik"
              % (len(L), akhir - awal))
print("\n")
# worst case
for i in range(3):
        L=list(range(3000))
        L=L[::-1]
        awal=time.time()
        U=sorted(L)
        akhir=time.time()
        print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik"
              %(len(L), akhir - awal))

#No 3
import timeit
import matplotlib.pyplot as plt

#a)
def soal_tiga(n):
    test = 0
    for i in range(n):
        for j in range(n):
            test = test + i * j
#b)
def soal_tiga(n):
    test = 0
    for i in range(n):
        for j in range(i):
            test = test + i * j
#c)
def soal_tiga(n):
    test = 0
    for i in range(n):
        test = test+1
    for j in range(n):
        test = test - 1
#d)
def soal_tiga(n):
    i = n
    while i > 0:
        k = 2 + 2
        i = i // 2
#e)
def soal_tiga(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                m = i + j + k + 2019
#f)
def soal_tiga(n):
    for i in range(n):
        for j in range(i):
            for k in range(j):
                m = i + j + k + 2019
#g)
def soal_tiga(n):
    for i in range(n):
        if i % 3 == 0:
            for j in range(n // 2):
                j+=j
        elif i % 2 == 0:
            for j in range(5):
                j+=j
        else:
            for j in range(n):
                j+=j

# No 7
import timeit
import matplotlib.pyplot as plt

def soal_tujuh(n):
    L = list(range(30))
    L = L[::-1]
    for i in range(n):
        L.append(n)
            

def uji_soal_tujuh(n):
    ls = []
    jangkauan = range(1, n+1)
    siap = "from __main__ import soal_tujuh"
    for i in jangkauan:
        t = timeit.timeit("soal_tujuh(" + str(i) + ")",
                          setup=siap, number=1)
        ls.append(t)
    return ls


n = 10
LS = uji_soal_tujuh(n)
plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()

#No 8
import timeit
import matplotlib.pyplot as plt

def soal_tujuh(n):
    L = list(range(30))
    L = L[::-1]
    for i in range(n):
        for b in range(n):
            L.insert(i,b)


def uji_soal_tujuh(n):
    ls = []
    jangkauan = range(1, n+1)
    siap = "from __main__ import soal_tujuh"
    for i in jangkauan:
        ##print('i = ',i)
        t = timeit.timeit("soal_tujuh(" + str(i) + ")", setup=siap, number=1)
        ls.append(t)
    return ls


n = 10
LS = uji_soal_tujuh(n)
plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()


#No 9
import timeit
import matplotlib.pyplot as plt

def carilurus(wadah, target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
    return False

def tim_matlib(n):
    z=100
    a = [8, 7, 2, 1, 3, 2, 10]
    U = carilurus(a, n)



def uji_soal_sembilan(n):
    ls = []
    jangkauan = range(1, n+1)
    siap = "from __main__ import tim_matlib"
    for i in jangkauan:
        t = timeit.timeit("tim_matlib(" + str(i) + ")",
                          setup=siap, number=1)
        ls.append(t)
    return ls

n = 10
LS = uji_soal_sembilan(n)
plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()



























