produk = [
    {"Nama": "TV", "Kategori": "elektronik", "Harga": 1000},
    {"Nama": "headphone", "Kategori": "elektronik", "Harga": 200},
    {"Nama": "baju", "Kategori": "fashion", "Harga": 50},
    {"Nama": "gitar", "Kategori": "musik", "Harga": 300},
    {"Nama": "sepatu", "Kategori": "olahraga", "Harga": 80},
    {"Nama": "kamera", "Kategori": "elektronik", "Harga": 600}
]

data_pelanggan = {
    "Rina": {"Minat": ["elektronik", "musik"], "Beli": ["TV", "headphone"]},
    "Budi": {"Minat": ["fashion", "musik"], "Beli": ["baju", "gitar"]},
    "Hartono": {"Minat": ["olahraga", "elektronik"], "Beli": ["sepatu", "kamera"]}
}

def rekomendasi_produk(nama_pelanggan):
    minat_pelanggan = data_pelanggan[nama_pelanggan]["Minat"]
    
    rekomendasi = []
    for p in produk:
        if p["Kategori"] in minat_pelanggan:
            rekomendasi.append(p["Nama"])
    
    return rekomendasi

rekomendasi_rina = rekomendasi_produk("Rina")
print(f"Rina {rekomendasi_rina}")