# program dengan isEmpty()
#   akan mengembalikan nilai True jika queue kosong
#   mengembalikan False jika queue jika queue masih 
#       berisi elemen

from collections import deque
#buat list kosong
#set dalam keadaan kosong
queueSaya=deque()

#tambah elemen (enqueue)
queueSaya.append('a')
queueSaya.append('b')
queueSaya.append('c')
print(queueSaya)
print('')

#hapus elemen (dequeue)
out=queueSaya.popleft()
print('data terhapus:', out)
print('')
print(queueSaya)
print('')

def isEmpty():
    return queueSaya==deque()
print('is empty:',isEmpty())