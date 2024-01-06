#https://koding.alza.web.id/menggunakan-modul-datetime/
import random as rnd

# menghasilkan bil. acak pada rentang 1 s.d 100
bil_acak = rnd.randint (1,100)
print(bil_acak)

# mensimulasikan lemparan dadu
dadu_1 = rnd.randint (1,6)
print(dadu_1)

# memilih sebuah elemen dari list 
l_siswa = ["upin","ipin","mail","mei-mei","jarjit","devi","susanti","ehsan"]
siswa_terpilih = rnd.choice(l_siswa)
print(siswa_terpilih)

#memilih beberapa elemen sekaligus 
siswa_terpilih = rnd.sample(l_siswa,k=3)
print(siswa_terpilih)

# mengecek urutan 
rnd.shuffle(l_siswa)
print(l_siswa)