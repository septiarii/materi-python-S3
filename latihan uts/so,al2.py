'''
Buatlah sebuah fungsi yang menerima sebuah input parameter dengan tipe data integer, 
yang bila dipanggil akan mencetak bunyi sila pancasila sesuai input tersebut 
'''

def cetak_sila_pancasila(sila):
    pancasila = [
        "Ketuhanan Yang Maha Esa",
        "Kemanusiaan yang adil dan beradab",
        "Persatuan Indonesia",
        "Kerakyatan yang dipimpin oleh hikmat kebijaksanaan dalam permusyawaratan/perwakilan",
        "Keadilan sosial bagi seluruh rakyat Indonesia"
    ]

    if sila >= 1 and sila <= 5:
        print(f"Sila {sila}: {pancasila[sila-1]}")
    else:
        print("Input tidak valid. Silakan masukkan angka antara 1 dan 5.")

cetak_sila_pancasila(3)