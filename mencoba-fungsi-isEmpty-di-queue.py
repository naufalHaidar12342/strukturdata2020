Q=[]
Q.append('a')
Q.append('b')
Q.append('c')
print(Q)
print('')
def isEmpty():
    return len(Q)==[]

#menghapus elemen 
out=Q.pop(0)
print('data terhapus:',out)
print('is empty:',isEmpty())
print(Q)
