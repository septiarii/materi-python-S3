import json
import random

file = open("surat_alquran.json",encoding="utf") #load file
daftar_surat = json.load(file) # kompersi isi file (json) ke dictionary

daftar_surat = list(daftar_surat.values()) # komperasi dictionary menjadi list
surat_10 = random.sample(daftar_surat,k=10) # ambil sample 10 surat secara acak

pilih_salah = []
for surat in surat_10:
    pilih_salah.append(surat['arti_nama'])

skor = 0
for surat in surat_10 :
    print(f"arti nama dari surat {surat['nama']} adalah? :") # cetak pertanyaan
    # siapkan pilihan jawaban
    jawaban_benar = surat['arti_nama']
    pilihan_jawaban = random.sample(pilih_salah,k=2)
    pilihan_jawaban.append(jawaban_benar)
    random.shuffle(pilihan_jawaban)
    peta_jawaban = {"a" :pilihan_jawaban[0],"b" :pilihan_jawaban[1], "c" :pilihan_jawaban[2]}
    # cetak pilihan
    print(f"pilih a. {pilihan_jawaban[0]} b. {pilihan_jawaban[1]} c. {pilihan_jawaban[2]} ")

    respon_user = input("a/b/c: ")
    jawaban_user = peta_jawaban[respon_user]

    if jawaban_user == jawaban_benar: 
        skor += 1
        print(f"benar !")
    else:
        print(f"salah ! jawaban yang bener adalah : {jawaban_benar}")
        
print(f"permainan berakhir, anda mendapatkan sekor akhir {skor}")
