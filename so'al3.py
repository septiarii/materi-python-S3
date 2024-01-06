'''
buatlah program yang meminta user memasukan sebuah nilai integrar terus menerus,
sampe user memasukan nilai 0.
di akhir program, tampilkan rata-rata nilai yang di imput oleh user
'''
4
lanjut = True
jumlah_nilai = 0
banyak_nilai = 0 

while lanjut :
    nilai = int(input("masukan nilai : "))
    if nilai == 0:
        lanjut = False
    else :
        jumlah_nilai += nilai
        banyak_nilai += 1

rerata = jumlah_nilai / banyak_nilai

print (f"rata-rata nilai : {rerata}")
