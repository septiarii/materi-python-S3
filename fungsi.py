'''
contoh fungsi tanpa masukan 
'''
def say_hello():
    print ("hello")

'''
contoh fungsi dengan masukan, tanpa keluaran 
'''
def say_hello_to(nama):
    print ("hello", nama )

'''
contoh fungsi dengan beberapa masukan 
'''
def say_selamat(nama, event):
    print (f"selamat {event}, {nama}")

say_hello_to("upin")
say_selamat("upin", "ulanga tahun")
say_selamat("jarjit", "wisuda")
