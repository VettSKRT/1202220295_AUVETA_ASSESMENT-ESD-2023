def hitung_kembalian(total_pembayaran, total_belanja):
    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    kembalian = total_pembayaran - total_belanja
    hasil = {}
    
    for nilai in pecahan:
        if kembalian >= nilai:
            jumlah = kembalian // nilai
            hasil[str(nilai)] = jumlah
            kembalian -= nilai * jumlah
    
    return hasil

# Contoh penggunaan
hasil_1 = hitung_kembalian(10000, 7500)
hasil_2 = hitung_kembalian(5000, 1100)
hasil_3 = hitung_kembalian(178000, 90500)

print(hasil_1)
print(hasil_2)
print(hasil_3)
