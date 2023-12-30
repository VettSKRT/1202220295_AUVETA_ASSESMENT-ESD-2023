menu = [
    {"Nama": "Ayam Goreng Krispi", "Tipe": "Makanan", "Harga": 15000},
    {"Nama": "Ayam Puk Puk (Bukan digeprek)", "Tipe": "Makanan", "Harga": 13000},
    {"Nama": "Ayam Bakar", "Tipe": "Makanan", "Harga": 20000},
    {"Nama": "Es teh", "Tipe": "Minuman", "Harga": 5000},
    {"Nama": "Es Jeruk", "Tipe": "Minuman", "Harga": 7000}
]

def hitung_biaya(pesanan):
    subtotal = 0
    for item in pesanan:
        for m in menu:
            if m["Nama"] == item:
                subtotal += m["Harga"]
                if m["Tipe"] == "Makanan":
                    subtotal += m["Harga"] * 0.05 
                else:
                    subtotal += m["Harga"] * 0.03 
                break
    return subtotal

pesanan_rehan = ["Ayam Bakar", "Ayam Bakar", "Es teh"]
pesanan_amba = ["Ayam Puk Puk (Bukan digeprek)", "Es teh", "Es teh", "Es teh"]
pesanan_faiz = ["Ayam Goreng Krispi", "Ayam Puk Puk (Bukan digeprek)", "Ayam Bakar", "Es teh", "Es Jeruk"]

biaya_rehan = hitung_biaya(pesanan_rehan)
biaya_amba = hitung_biaya(pesanan_amba)
biaya_faiz = hitung_biaya(pesanan_faiz)

print(f"Rehan Whangsap harus membayar: Rp {biaya_rehan}")
print(f"Amba Roni harus membayar: Rp {biaya_amba}")
print(f"Faiz Ngawi harus membayar: Rp {biaya_faiz}")
