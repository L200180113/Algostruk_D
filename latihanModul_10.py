import time

##def jumlahkan_cara_1(n):
##    hasilnya = 0
##    for i in range(1, n+1):
##        hasilnya = hasilnya + i
##    return hasilnya
##
##for i in range(5):
##    awal = time.time()
##    h = jumlahkan_cara_1(1000000)
##    akhir = time.time()
##    print("Jumlah adalah %d, memerlukan %9.8fdetik"
##          %(h, akhir-awal))
##    
##def jumlahkan_cara_2(n):
##    return (n*(n+1))/2

##for i in range(5):
##    awal = time.time()
##    h = jumlahkan_cara_2(10000)
##    akhir = time.time()
##    print("Jumlah adalah %d, memerlukan %9.8f detik" % (h, akhir-awal))

##def insertionSort(a):
##    n = len(a)
##    for i in range(1, n):
##        nilai = a[i]
##        pos = i
##        while pos > 0 and nilai < a[pos - 1]:
##            a[pos] = a[pos -1]
##            pos = pos - 1
##        a[pos] = nilai
##
##for i in range(5):
##    L = list(range(3000))
##    random.shuffle(L)
##    awal = time.time()
##    U = insertionSort(L)
##    akhir = time.time()
##    print("Mengurutkan %d bilangan, memerlukan %8.7f detik"
##          % (len(L), akhir-awal))
##import random
##def insertionSort(a):
##    n = len(a)
##    for i in range(1, n):
##        nilai = a[i]
##        pos = i
##        while pos > 0 and nilai < a[pos - 1]:
##            a[pos] = a[pos -1]
##            pos = pos - 1
##        a[pos] = nilai
##
##for i in range(5):
##    L = list(range(3000))
##    L = L[::-1]
##    awal = time.time()
##    U = insertionSort(L)
##    akhir = time.time()
##    print("Mengurutkan %d bilangan, memerlukan %8.7f detik"
##          % (len(L), akhir-awal))
##import random
##def insertionSort(a):
##    n = len(a)
##    for i in range(1, n):
##        nilai = a[i]
##        pos = i
##        while pos > 0 and nilai < a[pos - 1]:
##            a[pos] = a[pos -1]
##            pos = pos - 1
##        a[pos] = nilai
##        
##for i in range(5):
##    L = list(range(3000))
##    awal = time.time()
##    U = insertionSort(L)
##    akhir = time.time()
##    print("Mengurutkan %d bilangan, memerlukan %8.7f detik"
##          % (len(L), akhir-awal))

##>>> from timeit import timeit
##>>> timeit('sqrt(2)','from math import sqrt',number=10000)
##0.00270520000000829
##>>> timeit('sqrt(2)','from math import sqrt',number=100000)
##0.013396200000002523
##>>> timeit('sqrt(2)','from math import sqrt',number=1000000)
##0.13340699999999117
##>>> timeit('1+2')
##0.013718899999986434
##>>> timeit('sin(pi/3)', setup='from math import sin, pi')
##0.18840679999999566
##>>> timeit('sin(1.047)', setup='from math import sin')
##0.1256601000000046
##>>> 


import timeit
import matplotlib.pyplot as plt 

def kalangBersusuh(n):
    for i in range(n):
        for j in range(n):
            i+j

def ujiKalangBersusuh(n):
    ls=[]
    jangkauan =  range(1, n+1)
    siap = "from __main__ import kalangBersusuh"
    for i in jangkauan:
        print('i =',i)
        t = timeit.timeit("kalangBersusuh(" + str(i) + ")"
                          , setup=siap, number=1)
        ls.append(t)
    return ls

n = 1000
LS = ujiKalangBersusuh(n)

plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1,n+1)])
plt.show()















