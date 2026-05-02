# pengenalan fungsi/function dan fungsi dengan argument

def sapa():
    print("hallo")
    print("selamat menikmati hari")

sapa() # fungsi hanya bisa dipanggil setelah dibuat jadi berurutan, fungsi dibuat diatas, dipanggil dibawah

# fungsi dengan argumen

# def sapa(argument):
#     badan fungsi

def sapa_teman(teman):
    '''sapa teman''' # docstring untuk menjelaskan fungsi
    print(f"Hallo {teman}, bagaimana kabarmu hari ini?")

sapa_teman("ridwan")

nama_teman = input("siapa nama kamu? = ")
sapa_teman(nama_teman)

# program tambah
def tambah(angka1,angka2):
    print(F"{angka1} + {angka2} = {angka1 + angka2}")

tambah(2,4)

angka_1 = int(input("masukan angka pertama = "))
angka_2 = int(input("masukan angka kedua = "))

tambah(angka_1,angka_2)

# program sapa list
def halo(nama):
    '''sapa nama'''
    nama_1 = nama.copy() # kenapa perlu do copy? karena agar jika ada perubahan di dalam fungsi, list yang sebenarnya tidak ikut berubah
    for namanya in nama:
        print(f"hallo {namanya}")
        print("selamat datang\n")

nama_siswa = ['rudi','iwan','amat','edwin']

halo(nama_siswa)


'''hari 33'''

# function dengan return

# def nama_fungsi(argument):
#     badan_fungsi
#     return output

def kuadrat(angka):
    hasil_kuadrat = angka**2
    return hasil_kuadrat 

y = kuadrat(3)
print(y)

print(kuadrat(7))

a = 20 + kuadrat(3)
print(a)

# fungsi tambah
def tambah(angka1,angka2):#fungsi dengan multiple input
    hasil = angka1 + angka2
    return hasil 

print(tambah(3,4))

# fungsi dengan return banyak
def kalkulator(a,b):
    tambah = a+b
    kurang = a-b
    kali = a*b
    bagi = a/b
    pangkat = a**b
    floor = a//b
    modulus = a%b
    return tambah,kurang,kali,bagi,pangkat,floor,modulus

tambah,kurang,kali,bagi,pangkat,floor,modulus = kalkulator(3,5)

print(f"hasil tambah = {tambah}")
print(f"hasil kurang = {kurang}")
print(f"hasil kali =  {kali}")
print(f"hasil bagi = {bagi}")
print(f"hasil pangkat = {pangkat}")
print(f"hasil floor =  {floor}")
print(f"hasil modulus =  {modulus}")

# default argument 

# def fungsi(argument = default argument)
# digunakan untuk memnberi nilai bawaan pada argument

# contoh paling sederhana
def sapa(nama = "guys"):
    '''fungsi sapa'''
    print(f"halo {nama}")

sapa("ridwan")
sapa()

# contoh 2
def say_hi(nama,pesan = "selamat pagi"):
    print(F"hai {nama}, {pesan}")

say_hi("fadil","selamat sore")
say_hi("fadil")

# contoh 3
def hitung(angka,pangkat=2):
    hasil = angka**pangkat
    return hasil

print(hitung(3,4))
print(hitung(3))
print(hitung(angka=5,pangkat=3))
print(hitung(pangkat=4,angka=2))

# contoh 4
def tambah(input1=2,input2=3,input3=4,input4=5):
    jumlah = input1+input2+input3+input4
    return jumlah

print(tambah())
print(tambah(input1=5))
print(tambah(input3=1,input2=1))