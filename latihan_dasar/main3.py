'''HARI 30'''

# Looping Dictionary

data = {
    "awan":"pelajar",
    "imron":"bekerja",
    "ilham":"pelajar",
    "aldi":"mahasiswa",
    "oki":"pelajar"
}

# looping biasa
for nama in data:
    print(nama) # hanya akan menampilkan key nya saja

# operator untuk mengambil
## untuk mengambil key nya saja
print(data)
keys = data.keys()
print(keys)

for kunci in data.keys():
    print(kunci)
    # atau
    print(data.get(kunci)) # value akan diambil  karena kunnci berisi key yang artinya ini disuruh menampilkan value nya

## untuk mengambil value
nilai = data.values()
print(nilai)

for isi in data.values():
    print(isi)

## mengambil keduanya
key_value = data.items()
print(key_value)

for item in data.items():
    print(item)

for key,value in data.items():
    print(f"key = {key} | value = {value}") # akan pisah tidak  jadi satu seperti yang diatas


'''CONTOH'''
data_umur = {
    "suroso": "65",
    "ijah":"70",
    "roso":"45",
    "pakem":"60"
}

for nama,umur in data_umur.items():
    print(f"nama : {nama}")
    print(f"umur : {umur}\n")