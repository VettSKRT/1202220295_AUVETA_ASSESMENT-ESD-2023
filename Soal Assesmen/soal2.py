def cek_palindrom(kalimat):
    kalimat = kalimat.lower().replace(" ", "")
    reversed_kalimat = kalimat[::-1]

    if kalimat == reversed_kalimat:
        return "eureeka!"
    else:
        return "suka blyat"

output_1 = cek_palindrom("Angsa")
print(output_1) 

output_2 = cek_palindrom("KataK")
print(output_2) 

output_3 = cek_palindrom("kasur empuk")
print(output_3) 

output_4 = cek_palindrom("Aku Suka Kamu")
print(output_4)

output_5 = cek_palindrom("Ibu Ratna antar ubi.")
print(output_5)