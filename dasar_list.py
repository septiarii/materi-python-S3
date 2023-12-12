# dekralasi
siswa = ["upin","ipin","jarjit"]
tinggi_siswa = [110,110,112]
berat_badan = [17,18,19]
# akan di gunakan indeks mulai dari 0
print(siswa[1])
# tambah data
siswa.append("melani")
tinggi_siswa.append(114)
berat_badan.insert(2,20)
print(berat_badan)
# assignment/update date
siswa[2] = "ehsan"
print(siswa)
# hapus data
siswa.pop()
print(siswa)
siswa.append("melani")
# loop dgn indeks
for i in range(len(siswa)):
    print(siswa[i])

# loop for each
for s in siswa:
    print(s)