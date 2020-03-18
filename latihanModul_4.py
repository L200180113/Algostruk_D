## Latihan 1 hal 40
def cariLurus(wadah,target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
    return False

# Run
A = [10,51,2,18,4,31,13,5,23,64,29]
cariLurus(A,31)
True
cariLurus(A,8)
False


## Latihan 2 hal 41
class MhsTIF(object):
    def __init__(self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilKota(self):
        return self.kota
    def ambilUangSaku(self):
        return self.uangSaku

c0 = MhsTIF('Ika',10,'Sukoharjo',240000)
c1 = MhsTIF('Budi',51,'Sragen', 230000)
c2 = MhsTIF('Ahmad',2,'Surakarta',250000)
c3 = MhsTIF('Chandra',18,'Surakarta',235000)
c4 = MhsTIF('Eka',4,'Boyolali',240000)
c5 = MhsTIF('Fandi',31,'Salatiga',250000)
c6 = MhsTIF('Deni',13,'Klaten', 240000)
c7 = MhsTIF('Galuh',5,'Wonogiri',245000)
c8 = MhsTIF('Janto',23,'Klaten',245000)
c9 = MhsTIF('Hasan',64,'Karanganyar',270000)
c10 = MhsTIF('Khalid',29,'Purwodadi',265000)

Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

target = 'Klaten'
for i in Daftar:
    if i.kotaTinggal == target:
        print(i.nama + ' tinggal di ' + target)

def cariTerkecil(list):
    terkecil = list[0].uangSaku
    for i in list[1:]:
        if i.uangSaku < terkecil:
            nama = i.nama
            terkecil = i.uangSaku
    return nama
ck=cariTerkecil(Daftar)
print("Uang saku terkecil : "+ck)

def cariTerbesar(list):
    terbesar = c0.ambilUangSaku()
    for i in Daftar:
        if i.ambilUangSaku() > terbesar:
            terbesar = i.ambilUangSaku()
            nama=i.nama
    return nama
cb=cariTerbesar(Daftar)
print("Uang saku terbesar : "+cb)

def cariKurang250(list):
    print("kurang dari 250rb : ")
    batas = 250000
    for i in Daftar:
        if i.ambilUangSaku() < batas:
            print(i.ambilNama())
ck=cariKurang250(Daftar)
print(ck)

def cariLebih250(list):
    print("Lebih dari 250rb : ")
    batas = 250000
    for i in Daftar:
        if i.ambilUangSaku() > batas:
            print(i.ambilNama())
cl=cariLebih250(Daftar)
print(cl)

#Run
"""Deni tinggal di Klaten
Janto tinggal di Klaten
Uang saku terkecil : Budi
Uang saku terbesar : Hasan
kurang dari 250rb : 
Ika
Budi
Chandra
Eka
Deni
Galuh
Janto
None
Lebih dari 250rb : 
Hasan
Khalid
None"""

#Latihan 3 hal 43
def binSe(kumpulan,target):
    low = 0
    high = len(kumpulan) - 1

    while low <= high:
        mid = (high + low) // 2
        if kumpulan[mid] == target:
            return "Ada di index ke-" + str(mid)
            break
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
List = [1,3,5,7,9,11,13,15,17,19,114,121]
target1 = 45
target2 = 1

print("\nlistnya adalah ",List)
print("nilai target adalah ", target1)
print(binSe(List, target1))

print("\nlistnya adalah ",List)
print("nilai target adalah ", target2)
print(binSe(List, target2))

#Run
listnya adalah  [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 114, 121]
nilai target adalah  45
False

listnya adalah  [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 114, 121]
nilai target adalah  1
Ada di index ke-0




