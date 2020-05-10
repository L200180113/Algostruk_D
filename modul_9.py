class _SimpulPohonBiner(object) :
    def __init__(self, data) :
        self.data = data
        self.kiri = None
        self.kanan = None

A = _SimpulPohonBiner('Ambarawa')
B = _SimpulPohonBiner('Bantul')
C = _SimpulPohonBiner('Cimahi')
D = _SimpulPohonBiner('Denpasar')
E = _SimpulPohonBiner('Enrekang')
F = _SimpulPohonBiner('Flores')
G = _SimpulPohonBiner('Garut')
H = _SimpulPohonBiner('Halmahera timur')
I = _SimpulPohonBiner('Indramayu')
J = _SimpulPohonBiner('Jakarta')

A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; C.kanan = G
E.kiri = H
G.kanan = I

###No 6
def ukuranPohon(akar) :
    ukuran = 0
    if akar is not None :
        if akar.kiri is None and akar.kanan is None:
            ukuran += 1
        else :
            hasil = ukuranPohon(akar.kiri)
            ukuran += hasil
            hasil = ukuranPohon(akar.kanan)
            ukuran += hasil
    return ukuran
print(ukuranPohon(A))


#No 7
def tinggiPohon(akar):
    if akar is None :
        return 0
    else :
        kiri = tinggiPohon(akar.kiri)
        kanan = tinggiPohon(akar.kanan)
        if kiri > kanan :
            return kiri+1
        else :
            return kanan+1
print(tinggiPohon(A))

#No 8
def cetakDataLevel(akar, level = -1):
    level +=1
    if akar is not None:
        print (akar.data, "Level", level)
        cetakDataLevel (akar.kiri,level)
        cetakDataLevel (akar.kanan,level)
print(cetakDataLevel(A))



































