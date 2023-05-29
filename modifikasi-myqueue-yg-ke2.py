# modifikasi dari myqueue.py
# ->gunakan fungsi insert()
# ->gunakan pop() 
# ->tampilkan panjang antrian/queue setelah menjalankan pop()
# 1)apa perbedaan input elemen dengan insert() dan append()
# 2) apa perbedaan implementasi queue dengan collections.deque

from collections import deque
#buat list Q dengan keadaan awal kosong
myqueue=deque()
#menambahkan elemen (enqueue)
myqueue.append('a')
myqueue.append('b')
myqueue.append('c')
print(myqueue)

#mengahapus elemen (dequeue)
out=myqueue.popleft()
print('data terhapus:',out)

#menghapus elemen dengan pop()
out=myqueue.pop()
print('data terhapus:',out)
print('panjang queue:',len(myqueue))
print('')
# myqueue.insert('d') #note: insert harus disertai index didepannya
                        # misal myqueue.insert(0,'tes')
myqueue.insert(0,'d')
print(myqueue)


#fungsi isEmpty untuk mengecek list sudah kosong/belum
def isEmpty():
    # return myqueue==deque()
    return len(myqueue)==0
print('is empty?:',isEmpty())