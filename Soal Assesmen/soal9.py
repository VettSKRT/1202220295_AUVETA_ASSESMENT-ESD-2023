from collections import Counter

def cek_anak_nakal(nama_anak):
    counter_nama = Counter(nama_anak)
    max_kemunculan = max(counter_nama.values())
    
    if max_kemunculan == 1:
        return "Semuanya anak baik"
    else:
        anak_nakal = [nama for nama, kemunculan in counter_nama.items() if kemunculan == max_kemunculan]
        return ' dan '.join(anak_nakal) + " Nakal"

# Data nama-nama anak dari beberapa percakapan
percakapan_1 = ["Bagas", "Dimas", "Bagas", "Bagas", "Indra", "Gilang", "Gilang", "Hana", "Fajar", "Fajar"]
percakapan_2 = ["Bagas", "Dimas", "Fajar", "Bagas", "Indra", "Gilang", "Gilang", "Bagas", "Fajar", "Fajar"]
percakapan_3 = ["Aisyah", "Bagas", "Dewi", "Dimas", "Eka", "Fajar", "Gilang", "Hana", "Indra", "Jihan"]

# Menampilkan hasil
hasil_1 = cek_anak_nakal(percakapan_1)
hasil_2 = cek_anak_nakal(percakapan_2)
hasil_3 = cek_anak_nakal(percakapan_3)

print(hasil_1)  # Output yang diharapkan: Bagas Nakal
print(hasil_2)  # Output yang diharapkan: Bagas dan Fajar Nakal
print(hasil_3)  # Output yang diharapkan: Semuanya anak baik
