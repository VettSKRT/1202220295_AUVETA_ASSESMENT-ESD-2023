def cek_duplikat(angka):
    angka_set = set()
    
    for num in angka:
        if num in angka_set:
            return True
        angka_set.add(num)
    
    return False

# Input yang diberikan
input_data = [20, 1, 3, 2, 4, 6, 8, 5, 7, 9, 11, 13, 15, 10, 12, 14, 16, 18, 20, 17, 19]

# Memanggil fungsi dan menampilkan hasil
output = cek_duplikat(input_data)
print(output)  # Output yang diharapkan: True
