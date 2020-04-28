#nomor 1
class stack():
    def __init__ (self) :
        self.list = []
    def Empty (self) :
        return len(self.list) == 0
    def __len__ (self) :
        return len(self.list)
    def pop(self) :
        assert not self.Empty()
        return self.list.pop()
    def push(self, data) :
        self.list.append(data)

def cetakHexa(d) :
    f = stack()
    if d==0: f.push(0);
    while d !=0:
        sisa = d%16
        d = d//16
        f.push(sisa)
    hexa = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    st = ''
    for i in range(len(f)):
        st += str(hexa[f.pop()])
    return st

#nomor 2
class stack():
    def __init__ (self) :   #membuat stack kosong
        self.list = []
    def Empty (self) :      #mengembalikan nilai boolean yang menunjukkan apakah stack itu kosong
        return len(self.list) == 0
    def __len__ (self) :    #mengembalikan banyaknya item di stack
        return len(self.list)
    def pop(self) :         #mengembalikan nilai posisi atas lalu menghapus, stack kosong tidak dapat kosong
        assert not self.Empty()
        return self.list.pop()
    def push(self, data) :  #mendorong item ke stack, menambah item ke puncak stack
        self.list.append(data)

nilai = stack()
for i in range(16) :
    if i % 3 == 0 :
        nilai.push(i)
st = ''
for i in range(len(nilai)):
        st = st +""+ str(nilai.pop())
        print (st)

    
#nomor 3
class stack():
    def __init__ (self) :    #membuat stack kosong
        self.list = []
    def Empty (self) :       #mengembalikan nilai boolean yang menunjukkan apakah stack itu kosong
        return len(self.list) == 0
    def __len__ (self) :     #mengembalikan banyaknya item di stack
        return len(self.list)
    def pop(self) :          #mengembalikan nilai posisi atas lalu menghapus, stack kosong tidak dapat kosong
        assert not self.Empty()
        return self.list.pop()
    def push(self, data) :   #mendorong item ke stack, menambah item ke puncak stack
        self.list.append(data)

nilai = stack ()
for i in range(16):
    if i % 3 == 0:
        nilai.push(i)
    elif i % 4 == 0:
        nilai.pop()
st = ''
for i in range(len(nilai)):
        st = st+""+ str(nilai.pop())
        print (st)

#nomer 4

class Queue(object) :
    
    def __init__(self):
        self.qlist = []
        
    def __len__(self) :
        return len(self.qlist)
    
    def is_Empty(self) :
        return len(self) == 0
    
    def enqueue(self, data) :
        self.qlist.append(data)
        
    def dequeue(self) :
        assert not self.is_Empty()
        return self.qlist.pop(0)
    
    def getFrontMost(self) :
        assert not self.is_Empty()
        return self.qlist[0]
    
    def getRearMost(self) :
        assert not self.is_Empty()
        return self.qlist[-1]

class PriorityQueue(object) :
    
    def __init__(self):
        self.qlist = []
        
    def __len__(self) :
        return len(self.qlist)
    
    def is_Empty(self) :
        return len(self) == 0
    
    def enqueue(self, data, priority) :
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)
        
    def dequeue(self) :
        A = []
        for i in self.qlist:
            A.append(i)
        b = 0
        for i in range(1, len(self.qlist)) :
            if A[i].priority < A[b].priority :
                b = i
        hasil = self.qlist.pop(b)
        return hasil.item
a = Queue ()
a.enqueue(28)
a.enqueue(45)
a.enqueue(13)
a.enqueue(7)

print (a.dequeue())
print (a.dequeue())

print (a.getFrontMost())
print (a.getRearMost())

#nomer 5
    
class _PriorityQEntry() :
    def __init__ (self, data, priority) :
        self.item = data
        self.priority = priority
    
S = PriorityQueue()
S.enqueue("Jeruk",2)
S.enqueue("Tomat",4)
S.enqueue("Mangga",0)
S.enqueue("Duku",5)
S.enqueue("Pepaya",2)

print (S.dequeue())
print (S.dequeue())
print (S.dequeue())
print (S.dequeue())
print (S.dequeue())























