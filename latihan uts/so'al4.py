'''
Buatlah deklarasi sebuah variabel berisi daftar riwayat sekolah anda (SD sampai SMA/sederajat), 
dimana setiap riwayat sekolah (elemen pada daftar) disimpan dalam struktur data dictionary dengan kandungan informasi berupa: 
nama sekolah, alamat sekolah, dan tahun lulus. 
'''
riwayat_sekolah = [
    {
        "nama_sekolah": "SDN 3 GRENENG",
        "alamat_sekolah": "GRENENG TIMUR",
        "tahun_lulus": 2016
    },
    {
        "nama_sekolah": "MTS NW TIBU JORONG",
        "alamat_sekolah": "GREMENG TIMUR",
        "tahun_lulus": 2019
    },
    {
        "nama_sekolah": "SMK NW RENCO",
        "alamat_sekolah": "KELAYU JORONG",
        "tahun_lulus": 2022
    }
]

# Menampilkan riwayat sekolah
for riwayat in riwayat_sekolah:
    print(f"Nama Sekolah: {riwayat['nama_sekolah']}")
    print(f"Alamat Sekolah: {riwayat['alamat_sekolah']}")
    print(f"Tahun Lulus: {riwayat['tahun_lulus']}")
    print("="*35)





