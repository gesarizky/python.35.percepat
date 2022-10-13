# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput
cepat1 = float(input("Tuliskan Berapa Kecepatan Awal : "))
cepat2 = float(input("Tuliskan Berapa Kecepatan AKhir: "))
waktu1 = float(input("Tuliskan Berapa Waktu Awal : "))
waktu2 = float(input("Tuliskan Berapa Waktu Akhir: "))

# Mengkonversi
ubahcepat = cepat2 - cepat1
selwaktu = waktu2 - waktu1
percepat =  ubahcepat / selwaktu 

# Menampilkan Hasil
print('==========================================================')
print('Maka Perubahan Kecepatan = %0.2f kilometer/Jam'  %(ubahcepat))
print('Maka Selang Waktu  = %0.2f Jam'  %(selwaktu))
print('Maka Percepatan = %0.2f kilometer/Jam'  %(percepat))
print('==========================================================')
