# dekralasi
upin = {
    "nama lengkap" : "ngga jelas",
    "tinggi" : 110,
    "berat" : 17
}
 
mhs = {
  "nim" : "123456789",
  "nama" : "kurang tau",
  "prodi" : "teknik informatika",
  "thn masuk" : 2023,
  "cuti" : False
 }

proglanj = {
 "kode" : "TI789",
 "nama" : "pemegraman lanjut",
 "sks" : 3
}
# akses elemen pada dictonary menggunakan key
print(upin["nama lengkap"], upin ["tinggi"])
print(mhs["nim"],mhs["nama"],mhs["prodi"],mhs["thn masuk"],mhs["cuti"])
print(f"mata kuliah{proglanj['nama']} memiliki bobot{proglanj['sks']} SKS")

# update elemen 
mhs["prodi"] = "ilmu komputer"
print(mhs)

# tambahan elemen
mhs["asal"] = "pancor"
print(mhs)

# loop
for k in mhs:
    print(k, ":", mhs[k])

for k,v in mhs.items():
    print(k,v)