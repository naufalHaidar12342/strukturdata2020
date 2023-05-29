#contoh class / adt , menggunakan python
#haidar12342-dinus

#inisialisasi dengan fungsi class

class Variabel:
    def __init__ (self,angka1,angka2):
        self.angka1=angka1
        self.angka2=angka2
        
    #fungsi menghitung gravitasi
    def gravitasi(self):
        earthGrav=9.8
        grav=self.angka1*earthGrav*self.angka2
        return grav
        
    #fungsi menghitung energi kinetik
    def kinetik(self):
        ek=0.5*self.angka1*(self.angka2*self.angka2)
        return ek
    
    #fungsi menghitung berat di bumi
    def berat(self):
        earthGrav=9.8
        totalBerat=self.angka1*earthGrav
        return totalBerat
        
    #mencetak isi angka yang di masukkan. akan dipanggil di print(contoh1)
    #  atau print(contoh2)
    def __str__(self):
        return '<'+str(self.angka1)+','+str(self.angka2)+'>'