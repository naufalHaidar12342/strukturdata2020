Q = []
def is_empty(): #cek kosong
    return len(Q) == 0

Q.append('a')
Q.append('b')
Q.append('c')

if not is_empty():
     tail=len(Q)-1


print("Tail:", Q[tail])