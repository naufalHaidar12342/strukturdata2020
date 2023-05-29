#bagian ini akan memanggil hasil pengolahan di library.py

#langkah pertama, import dulu file sebelumnya

from library import *

def main():
    contoh1=Variabel(3,4)
    contoh2=Variabel(5,6)
    print('angka pertama dari contoh1:',contoh1.angka1)
    print('angka kedua dari contoh1:',contoh1.angka2)
    print(contoh1)
    print('angka pertama dari contoh2:',contoh2.angka1)
    print('angka kedua dari contoh2:',contoh2.angka2)
    print(contoh2)
    print('==========================================')
    print('gravitasi dari contoh1:',Variabel.gravitasi(contoh1))
    print('gravitasi dari contoh2:',Variabel.gravitasi(contoh2))
    print('')
    print('energi kinetik dari contoh1:',Variabel.kinetik(contoh1))
    print('energi kinetik dari contoh1:',Variabel.kinetik(contoh2))
    print('')
    print('berat dari contoh1:', Variabel.berat(contoh1))

if __name__ == '__main__':
    main()