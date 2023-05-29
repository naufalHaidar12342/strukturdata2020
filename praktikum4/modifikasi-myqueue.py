#modifikasi program myqueue.py dalam list Q
# 1) bagaimana cara menampilkan jumlah elemen list Q?
# 2) bagaimana menampilkan head dan tail dari list Q?


#buat list Q
#set/ atur dalam keadaan kosong, berarti Q=[]
Q=[]
#menambahkan elemen (enqueue)
Q.append('a')
Q.append('b')
Q.append('c')

#fungsi isEmpty, mengecek apakah list sudah kosong
def isEmpty():
    return len(Q)==0

#fungsi kustomPop, menghapus elemen (dequeue) sesuai jumlah
#                   isinya
def kustomPop():
    if not isEmpty():   #jika kondisinya tidak memenuhi isEmpty(),
        out=Q.pop(0)    #   jalankan perintah berikut:
        print('data terhapus:',out)
        print(Q)
        print('panjang list:', len(Q))
        #karena jumlah elemen berarti panjang list nya,
           #kita ubah saja kalimatnya
        print('jumlah elemen',len(Q))
        tampilkanHead_Tail()
    else:
        print("queue empty cannot pop")

#untuk menampilkan head dan tail:
#   dalam list yang tidak kosong,
#   head berada di index 0 , sedangkan tail
#   posisinya dicari dengan panjang list dikurangi 1
def tampilkanHead_Tail():
    if not isEmpty():
        tail=len(Q)-1
        print('bagian head:',Q[0])  #Q[0] berarti menunjuk ke
        print('bagian tail:',Q[tail])#  elemen dengan index 0. jika 
    else:                            # di dalam kurung siku diisi
        print("queue empty")         #variabel lain, berarti variabel
                                      # tsb berfungsi sebagai index
                                      
#memanggil kustomPop()
kustomPop()
print('')   #mencetak baris kosong, hanya digunakan untuk pemberian
kustomPop() #jarak antara baris atas dengan bawahnya
print('')
kustomPop()

#mengecek apakah list sudah kosong
print('is empty:',isEmpty())

#memanggil tampilkanHead_Tail
# tampilkanHead_Tail()
     