#menghapus elemen di depan list
# ingat: index dimulai dari 0, seperti di pertamina xd

#membuat sebuah list Q dengan kondisi
#   berisi a,b,c
Q=['a','b','c'] 
out=Q.pop(0)   #by default/ standarnya, pop() akan menghapus 
            #element dari list yang paling belakang, 
            #KECUALI jika diberi angka yang menandakan index 
            #dari element dalam list tersebut
print(Q)