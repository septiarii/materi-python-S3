'''
body mas index (index masa tahun), atau BMI di hitung dengan rumus sebagai berikut :
BMI = bb/tb2
bb = berat badan dalam satuan kilo gram
tb = tinggi bada dalam satuan meter 
buatla sebuah program yang menerima input nama,
tinggi badan dalam satuan cm, dan berat badan dalam satuan kg,
hitung BMI dan klapikasikan jenis badan orang di maksud, di mana
<17 kurus
17 s.d 25 nurmal
25 s.d 30 gemuk
>30 obesitas
catatan : 1 meter 100 cm

gunakan fungsi dalam menyelsaikan so'al di atas
'''
def htg_bmi(bb,tb):
    tb = tb / 100
    bmi = bb / (tb ** 2)
    return bmi

def kateg_bmi (bmi):
    jenis_badan = "obesitas"
    if bmi < 17:
        jenis_badan("tergolong kurus") 
    elif bmi < 25:
        jenis_badan("tergolong normal")
    elif bmi < 30:
        jenis_badan("tergolong gemuk")
    return jenis_badan

bb = int(input("berat badan ? : "))
tb = int(input("tinggi badan ? :"))
bmi = htg_bmi (bb,tb)
jenis_badan = kateg_bmi (bmi)
print(f"BMI : {bmi}, jenis {jenis_badan}")