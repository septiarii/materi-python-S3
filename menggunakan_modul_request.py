import requests

api_url = 'https://api.exchangerate-api.com/v4/latest/IDR' # alamat api
rslt = requests.get(api_url) # mengirimkan request ke alamat api

print(rslt)

if rslt.status_code == requests.codes.ok :
    hasil = rslt.json()
    nilai_tukar_all = hasil ['rates']
    mata_uang_l = ["USD","GBP","JPY","IRR","VND","THB"]
    for mata_uang in mata_uang_l:
        nilai_1IDR = nilai_tukar_all[mata_uang]
        nilai_ke1IDR = 1 /nilai_1IDR
        print(f"nilai tukar 1 {mata_uang} adalah {nilai_ke1IDR:.2f} IDR")
    else :
        print('gagal mendapatkan respon yang di inginkan dari server')
