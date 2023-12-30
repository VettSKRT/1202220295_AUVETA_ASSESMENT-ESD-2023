def siapa_yang_mengambil_kue(urutan_kedatangan, foto_kue):
    urutan_kedatangan.index(foto_kue)

    if foto_kue == 'Xiao':
        return "Xiao"
    elif 'air mineral' in urutan_kedatangan[:urutan_kedatangan.index(foto_kue)]:
        return "Childe"
    elif 'memeriksa kue' in urutan_kedatangan[:urutan_kedatangan.index(foto_kue)]:
        return "Ningguang"
    else:
        return "Hutao"

urutan_kedatangan = ['Ningguang', 'Hutao', 'Xiao', 'Childe']
foto_kue = 'Xiao'

pencuri_kue = siapa_yang_mengambil_kue(urutan_kedatangan, foto_kue)
print(f"Menurut logika sederhana, kemungkinan besar kue diambil oleh: {pencuri_kue}")
