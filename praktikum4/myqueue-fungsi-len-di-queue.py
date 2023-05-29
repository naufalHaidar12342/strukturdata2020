#fungsi len di queue
# membuat list Q

#Q dalam keadaan kosong
Q=[]
#tambah elemen (enqueue)
Q.append('a')
Q.append('b')
Q.append('c')
print(Q)

#hapus elemen (dequeue)
out=Q.pop(0)
print('data terhapus:',out)
print(Q)

def isEmpty():
    return len(Q)==[]
print('is empty:',isEmpty())