'''
Buatlah sebuah fungsi yang menerima input parameter berupa usia (int), dan status perkawinan (boolean). Jika fungsi dipanggil, 
ia akan mengembalikan nilai boolean true jika boleh memilih dan sebaliknya.
Catatan:
Aturan untuk dapat memilih pada pemilu di Indonesia adalah telah berusia 17 tahun atau sudah menikah
'''

def aturan_pemilu(usia , status_perkawinan):
    if usia >= 17 or status_perkawinan:
        return True
    else:
        return False
   
print(aturan_pemilu(17 , True))