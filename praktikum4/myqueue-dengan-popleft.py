#fungsi popleft() di queue dengan deque

from collections import deque

#insialisasi queue
myqueue=deque()

#menambah elemen (enqueue)
myqueue.append('a')
myqueue.append('b')
print(myqueue)
print("")

#menghapus elemen (dequeue)
out=myqueue.popleft()
print('data terhapus:',out)
print(myqueue)