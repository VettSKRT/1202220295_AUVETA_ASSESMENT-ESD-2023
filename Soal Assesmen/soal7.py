def dekripsi_pesan(pesan_terenkripsi):
    pesan_terdekripsi = ""
    for huruf in pesan_terenkripsi:
        if huruf.isalpha():
            huruf_terdekripsi = chr(((ord(huruf) - 97 - 5) % 26) + 97) if huruf.islower() else chr(((ord(huruf) - 65 - 5) % 26) + 65)
            pesan_terdekripsi += huruf_terdekripsi
        else:
            pesan_terdekripsi += huruf
    return pesan_terdekripsi

pesan_terenkripsi = [
    "xfqfr bfmdz",
    "gjxtp lzj rfz ifkyfw jxi snm",
    "gwt, gjxtp qz rfz rfpfs in bfwlty lfp?",
    "fpz xfdfsl pfrz, rfz lfp ofin ufhfwpz",
    "dfsl pnwnr xynhpjw otrtp pz pnhp ifwn lwzu"
]

for index, pesan in enumerate(pesan_terenkripsi):
    pesan_terdekripsi = dekripsi_pesan(pesan)
    print(f"Pesan {index + 1}: {pesan_terdekripsi}")
