#bu pergi ke pasar membeli telur sebanyak 5 kilogram untuk membuat kue, 
#harga 1 kilo gram telor adalah 26000 perkilogram.
#Untuk pergi ke pasar ibu harus naik angkot pp (pulang pergi) dengan tarip Rp 3500 sekali naik angkot.
#Pertanyaan: Berapakah sisa uang jika ibu membawa uang sebesar Rp 200.000,- 
#Identifikasi masalah
#input: berat telur(brt), harga telur (hrg), transport(ongkos) uang ibu(uang) 
#Output: sisa uang(sisa)
#Buatlah Programnya dengan Python!

def hitung_sisa_uang(berat_telur, harga_telur, ongkos_transport, uang_ibu):
    total_harga_telur = berat_telur * harga_telur
    total_ongkos_transport = ongkos_transport * 2  # PP (pulang pergi)
    total_biaya = total_harga_telur + total_ongkos_transport
    
    sisa_uang = uang_ibu - total_biaya
    return sisa_uang

berat_telur = 5  # dalam kilogram
harga_telur_per_kg = 26000  # dalam rupiah
ongkos_transport = 3500  # dalam rupiah
uang_ibu = 200000  # dalam rupiah

sisa_uang = hitung_sisa_uang(berat_telur, harga_telur_per_kg, ongkos_transport, uang_ibu)

print("Sisa uang ibu setelah membeli telur adalah Rp", sisa_uang)


