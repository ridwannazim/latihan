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


'''hari 34'''

# latihan fungsi menggunakan program kalkulator bmi(projek->kalkulator_BMI.py)

'''hari 35'''

# type hints untul fungsi

# bentuk standar fungsi yang kita pelajari
'''
def sapa(nama,pesan):
    print(f"{nama},{pesan}.")

sapa("ucup","selamat pagi")

def hitung(a,b):
    hasil = a * b
    print(hasil)

hitung(3,4)
hitung(4,4)
'''

# penggunaan type hints
                                        # -> float artinya output yang dihasilkan akan dirubah ke float
def tambah(angka,angka2:float) -> float:# :float merupakan type nya jadi akan membatasi pada type tersebut saja
    hasil = angka + angka2
    return hasil

total = tambah(3.4,5.4)
print(total)
total = tambah(4,5)
print(total)

import string
def display(argument:string):
    print(argument)

display("ucup")
display(88)


'''hari 36'''

# *args pada fungsi

# fungsi biasa 
def data(nama,tinggi,berat):
    print(f"{nama}, tinggi : {tinggi}, berat : {berat}")

data("ridwan",181,64)

def data_list(list_):
    data = list_.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]

    print(f"{nama}, tinggi : {tinggi}, berat : {berat}")

data_list(['tito',177,70])

# menggunakan *args
def sapa(*sapa):
    print(f"nama : {sapa[0]}, tinggi : {sapa[1]}, berat : {sapa[2]}")

sapa("otong",167,65)

# studi kasus

def tambah(*tambah):
    hasil = 0
    for angka in tambah:
        hasil += angka
    
    return hasil

jumlah = tambah(1,2,4,4,5,4)
print(jumlah)


'''HARI 37'''

# **kwargs pada fungsi

# contoh fungsi biasa

def alamat(nama,desa,rt,rw):
    '''fungsi biasa'''
    print(f"nama = {nama}")
    print(f"desa = {desa} RT = {rt} RW = {rw}")

alamat("rudi","panggung","04","02")

# menggunakan **kwargs
def alamat(**alamat):
    '''fungsi **kwargs'''
    nama = alamat['nama']
    desa = alamat['desa']
    rt = alamat['rt']
    rw = alamat['rw']
    print(f"nama = {nama}")
    print(f"desa = {desa} RT = {rt} RW = {rw}")

alamat(nama="ardi",desa="maospati",rt="03",rw="02")

# studi kasus

def perhitungan(*angka,**operasi):
    '''fungsi hitung'''
    hasil = angka[1]
    if operasi['hitung'] == "tambah":
        for number in angka :
            hasil += number

    elif operasi['hitung'] == "kurang":
        for number in angka :
            hasil -= number

    elif operasi['hitung'] == "kali":
        #hasil = 1
        for number in angka :
            hasil *= number

    else:
        print("jenis operasi tidak ditemukan")

    return hasil

hasil = perhitungan(1,3,4,2,hitung="tambah")
print(hasil)
hasil = perhitungan(1,3,4,2,hitung="kurang")
print(hasil)
hasil = perhitungan(1,3,4,2,hitung="kali")
print(hasil)