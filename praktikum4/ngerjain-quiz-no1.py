Q = []
def is_empty(): #cek kosong
     return len(Q) == 0

Q.append('a')
Q.append('b')
Q.append('c')
out = Q.pop(0)
out = Q.pop(0)
out = Q.pop(0)
print(Q)