# Data produk yang tersedia
produk = [
    {"Nama": "TV", "Kategori": "elektronik", "Harga": 1000},
    {"Nama": "headphone", "Kategori": "elektronik", "Harga": 200},
    {"Nama": "baju", "Kategori": "fashion", "Harga": 50},
    {"Nama": "gitar", "Kategori": "musik", "Harga": 300},
    {"Nama": "sepatu", "Kategori": "olahraga", "Harga": 80},
    {"Nama": "kamera", "Kategori": "elektronik", "Harga": 600}
]

# Data minat dan pembelian pelanggan
data_pelanggan = {
    "Rina": {"Minat": ["elektronik", "musik"], "Beli": ["TV", "headphone"]},
    "Budi": {"Minat": ["fashion", "musik"], "Beli": ["baju", "gitar"]},
    "Hartono": {"Minat": ["olahraga", "elektronik"], "Beli": ["sepatu", "kamera"]}
}

# Fungsi untuk memberikan rekomendasi produk berdasarkan minat pelanggan
def rekomendasi_produk(nama_pelanggan):
    minat_pelanggan = data_pelanggan[nama_pelanggan]["Minat"]
    
    rekomendasi = []
    for p in produk:
        if p["Kategori"] in minat_pelanggan:
            rekomendasi.append(p["Nama"])
    
    return rekomendasi


# Memberikan rekomendasi produk untuk pelanggan Rina
rekomendasi_rina = rekomendasi_produk("Rina")
print(f"Rina {rekomendasi_rina}")  # Output yang diharapkan: ['gitar', 'kamera']