##### No 1
class MhsTIF(object):
    def __init__(self,nama,NIM,kota,us):
        self.nama=nama
        self.nim=NIM
        self.kota=kota
        self.uang=us
    def __str__(self):
        s=self.nama+',NIM '+str(self.NIM)\
           +'. tinggal di '+self.kota\
           +'. uang saku Rp '+str(self.uang)\
           +'. tiap bulan'
        return s
c0 = MhsTIF('Ika', 10, 'Sukoharjo', 240000)
c1 = MhsTIF('Budi', 51, 'Sragen', 230000)
c2 = MhsTIF('Ahmad', 2, 'Surakarta', 250000)
c3 = MhsTIF('Chandra', 18, 'Surakarta', 235000)
c4 = MhsTIF('Eka', 4, 'Boyolali', 240000)
c5 = MhsTIF('Fandi', 31, 'Salatiga', 250000)
c6 = MhsTIF('Deni', 13, 'Klaten', 245000)
c7 = MhsTIF('Galuh', 5, 'Wonogiri', 245000)
c8 = MhsTIF('Janto', 23, 'Klaten', 245000)
c9 = MhsTIF('Hasan', 64, 'Karanganyar', 270000)
c10 = MhsTIF('Khalid', 29, 'Purwodadi', 265000)
x = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

def swap(x,a,b):
    temp=x[a]
    x[a]=x[b]
    x[b]=temp

def sort(x):
    n=len(x)
    for i in range(n-1):
        for j in range(n-i-1):
            if x[j].nim>x[j+1].nim:
                swap(x,j,j+1)
    for i in x:
        print(i.nama)
##### No 2
def swap(x,a,b):
    temp=x[a]
    x[a]=x[b]
    x[b]=temp

def gabungkan(x,y):
    a=[]
    m=len(y)
    for i in range(m):
        a.append(y[i])
    n=len(x)
    for i in range(n):
        a.append(x[i])
    o=len(a)
    for i in range(o-1):
        for j in range(o-i-1):
            if a[j]>a[j+1]:
                swap(a,j,j+1)
    print(a)
##### No 3
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
                
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp
    
def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)
            
def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[1] < A[posisiTerkecil]:
            posisiTerkecil = 1
    return posisiTerkecil

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
from time import time as detak
from random import shuffle as kocok
k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub);ak=detak();print("Bubble    : %g detik"%
                                                (ak-aw));
aw = detak();selectionSort(u_sel);ak=detak();print("Selection : %g detik"%
                                                   (ak-aw));
aw = detak();insertionSort(u_ins);ak=detak();print("Insertion : %g detik"%
                                                   (ak-aw));




















    
