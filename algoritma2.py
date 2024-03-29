#Seorang pedagang mangga menjual dagangannya yang setiap kg mangga dihargai dengan harga tertentu.
#Setiap pembeli membayar harga mangga yang dibeli nya berdasarkan berat.
#Buatlah algoritma untuk menentukan harga yang harus dibayar pembeli.
#• Identifikasi masalah
#Input: harga per kg(hrg), berat pembelian (brt)
#• Output: harga yang dibayar pembeli(byr)

def hitung_harga(hrg, brt):
    byr = hrg * brt
    return byr

# Input harga per kilogram dan berat pembelian
hrg_per_kg = float(input("Masukkan harga per kilogram mangga: "))
berat_pembelian = float(input("Masukkan berat pembelian dalam kg: "))

# Hitung harga yang harus dibayar oleh pembeli
harga_bayar = hitung_harga(hrg_per_kg, berat_pembelian)

print("Harga yang harus dibayar pembeli adalah:", harga_bayar)
 