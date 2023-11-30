i_nilai = [30,70,82,45,80,76,88,54]

# cari nilai maksimum
def cari_maks (nilai):
    maks = 0 
    for nilai in i_nilai:
        if nilai > maks:
            maks = nilai 
    return maks 

print (cari_maks(i_nilai))