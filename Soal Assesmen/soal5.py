from itertools import permutations

def hitung_kombinasi_username(nama_lengkap):
    nama_lengkap = nama_lengkap.replace(" ", "").lower()
    
    semua_kombinasi = []
    for i in range(1, 7):
        kombinasi = permutations(nama_lengkap, i)
        semua_kombinasi.extend(kombinasi)
    
    # Menghitung jumlah kombinasi yang mungkin
    jumlah_kombinasi = len(set(map(lambda x: ''.join(x), semua_kombinasi)))
    
    return jumlah_kombinasi

# Nama lengkap
nama_lengkap = "Naip Lovyu"

# Memanggil fungsi dan menampilkan hasil
jumlah_kombinasi = hitung_kombinasi_username(nama_lengkap)
print(f"Jumlah kombinasi username yang mungkin adalah: {jumlah_kombinasi}")
