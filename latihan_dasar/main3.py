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

'''HARI 38'''

# filter 
# ini experimen dan hasi dibawah hasil buat dan debug sendiri
data = {
    '001':{
        'nama':'rudi',
        'umur':13
        },
    '002':{
        'nama':'parman',
        'umur':45
        },
    '003':{
        'nama':'rahma',
        'umur':20
        },
    '004':{
        'nama':'ucup',
        'umur':9
        },
    '005':{
        'nama':'tono',
        'umur':15
        },
}

def cek_umur(data):
    return data[1]['umur'] <17    
    
    
dibawah_17tahun = list(filter(cek_umur,data.items()))
no=1
for orang in dibawah_17tahun:
        print(f"{no} nama = {orang[1]['nama']:^10} | umur = {orang[1]['umur']:^5}")
        no+=1
        

'''HARI 39'''

# lambda funtion

# fungsi biasa 
def kuadrat(angka):
    return angka**2

print(f"hasil dari 5 kuadrat = {kuadrat(5)}")

# menggunakan lambda
# output = lambda argument : expression

kuadrat = lambda angka : angka ** 2
print(f"hasil dari 3 kuadrat = {kuadrat(3)}")

pangkat =  lambda angka,pangkat : angka**pangkat
print(f"hasil dari 5 dipangkatkan 3 = {pangkat(5,3)}")

bagi =  lambda angka,pembagi : angka / pembagi
print(f"hasil dari 21 dibagi 3 = {bagi(21,3)}")

# lambda berguna untuk mem filter
# contoh sederhana

nama = ["arman","ujang","kampret","sarimin"]

nama.sort()
print(f"data nama short = {nama}")

def panjang_nama(nama):
    return len(nama)

nama.sort(key=panjang_nama)
print(F"sort berdasar kan pannjang nama = {nama}")

# menggunakan lambda
nama = ["arman","ujang","kampret","sarimin"]
nama.sort(key=lambda nama:len(nama))
print(f"sort menggunakan lambda = {nama}")

# filter 
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def lebih_dari_10(angka):
    return angka>10

data_angka_baru = list(filter(lebih_dari_10,data_angka))
print(f"angka lebih dari 10 = {data_angka_baru}")
#menggunkan lambda
data_angka_baru = list(filter(lambda x:x<10,data_angka))
print(f"angka kurang dari 10 = {data_angka_baru}")

# genap
print(f"angka genap = {list(filter(lambda x:x%2==0,data_angka))}")
# ganjil
print(f"angka ganjil = {list(filter(lambda x:x%2!=0,data_angka))}")
# keliapat 5
print(f"angka kelipatan 5 = {list(filter(lambda x:x%5==0,data_angka))}")
# angka 4 > 10 (lebih dari 4 kurang dari 10)
print(f"angka lebih dari 4 kurang dari 10  = {list(filter(lambda x:x>4 and x<10 ,data_angka))}")
print(f"angka lebih dari 4 kurang dari 10  = {list(filter(lambda x:4 < x <10 ,data_angka))}")


# anonymous function
# currying <- haskell curry

def pangkat(angka,n):
    hasil = angka**n
    return hasil

print(f"hasil dari 3 dipangkatkan 3 = {pangkat(3,3)}")

def pangkat(n):
    return lambda angka : angka ** n

pangkat7 = pangkat(7)
print(f"hasil dari 3 dipangkatkan 7 = {pangkat7(3)}")
pangkat2 = pangkat(2)
print(f"hasil dari 3 dipangkatkan 2 = {pangkat2(3)}")

print(f"hasil dari 2 dipangkatkan 2 = {pangkat(2)(2)}")


'''HARI 40'''

# global dan local scope

nama_global = "nazim"  # <-- ini merupakan variabel global

# mengakses variabel global menggunakan fungsi
def sapa():
    print(f"Halo {nama_global}")

sapa()

# mengakses variabel global menggunakan for
for i in range(1,6):
    print(f"{i}. Halo {nama_global}")

# mengakses variabel global menggunakan if
if True:
    print(f"Halo {nama_global}")

## variabel local atau local scope

def fungsi():
    nama_local = "ucup"  # <-- ini merupakan variabel local(hanya bisa diakses didalam fungsi)

fungsi()
# print(nama_local)  <-- tidak akan bisa diakses

## contoh 1 : penggunaan akses variabel

def sapa_teman():
    print(f"HALO {nama}")

nama = "udin"
sapa_teman()

## contoh 2 : merubah variabel global 

angka = 1
nama = "arip"

def ubah_isi(angka_baru,nama_baru):
    global angka   # " global " <-- membuat fungsi memiliki akses untuk mengubah nilai global
    global nama
    angka = angka_baru
    nama = nama_baru

print(f"angka = {angka} | nama = {nama}")
ubah_isi(25,"nazim")
print(f"angka = {angka} | nama = {nama}")

# contoh 3 :
angka = 0

for i in range(0,5):
    angka += i
    dummy = 5

print(angka)
print(dummy)

if True:
    angka_baru = 3
    dummy = 2

print(angka_baru)
print(dummy)

# local hanya ada dalam fungsi 


'''HARI 41'''

# import

#cara melakuakn import
import coba_import as cb  # mengimmport keseleruhan file coba_import lalu menggunkan cb sebagai nama alias
from coba_import import tambah, sapa # hanya mengimport fungsi tambah dan sapa dari file coba import




print(cb.data)
print(cb.nama)

hitung = cb.tambah(12,5)
print(hitung)
hitung = cb.tambah(12.5,5)
print(hitung)

cb.sapa("rido")
print(tambah(5,6))
print(sapa("ridwan"))

data = 20
print(data)

print(cb.data)
cb.data = 20
print(cb.data)