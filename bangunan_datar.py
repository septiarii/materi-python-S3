def luas_persegi(sisi):
    return sisi * sisi

def luas_persegi_panjang(pjg, lbr):
    return pjg * lbr

def luas_segitiga(alas,tinggi):
    return 0.5 * alas * tinggi

import bangunan_datar # cara import 1
print (bangunan_datar. luas_persegi(3))
print (bangunan_datar. luas_persegi_panjang(3,4))

import bangunan_datar as bd # cara import 2
print (bd. luas_segitiga(4,8))

from bangunan_datar import luas_persegi # cara 3
print (luas_persegi(7))

from bangunan_datar import luas_segitiga as l_sgtg # cara 4
print (l_sgtg(6,5))

from bangunan_datar import luas_persegi, luas_persegi_panjang # cara 5
print (luas_persegi(5))
print(luas_persegi_panjang(7,8))
