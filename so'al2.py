'''
body mas index (indeks masa tubuh), atau BMI di hitung dengan rumus sebagai beikut:
BMI : bb / tb2
bb : berat badan dalam satuan kilogram
tb : tinggi badan dalam satuan meter
buatlah sebuah program yang menerima input nama,
tinggi badan dalam satuan cm, dan berat badan seseorang dalam satuan kg,
kemudian menghitung BMI dan mencetak nilainya ke layar.
catatan : 1 meter = 100 cm
'''
bb = int(input("masukan berat badan (kg) : "))
tb = int(input("masukan tinggi badan (cm) : "))

tb_m = tb / 100
bmi = bb / (tb_m ** 2)
print(f"BMI = {bmi}")

if bmi < 17 :
    print ("tergolong kurus")
elif bmi <25:
    print ("tergolong normal")
elif bmi <30:
    print ("tergolong gemuk")
else :
    print ("tergolong obsesitas")