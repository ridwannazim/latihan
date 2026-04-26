""" PELAJARAN PYTHON 2 """
""" HARI 11-"""
# DATE AND TIME (DATETIME)
# IF DAN ELSE STATEMENT
# ELIF STATEMENT
# FOR LOOP
# WHILE LOOP
# CONTINUE==PASS==BREAK
# LATIHAN MEMBUAT SEGITIGA DENGAN PERULANGAN
# LIST
# OPERASI LIST

'''HARI 11'''

''' DATE AND TIME (LATIHAN)'''
# datetime 
import datetime as dt # mengubah pemanggilan datetime menjadi dt (penamaan alias)

print("isi tanggal lahir\n")
tanggal = int(input("tanggal \t= "))
bulan = int(input("bulan \t\t= "))
tahun = int(input("tahun \t\t= "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir = {tanggal_lahir}")
print(f"kamu lahir hari = {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini = {hari_ini}")

umur_hari = hari_ini - tanggal_lahir
tahun_now = umur_hari.days // 365
bulan_now = (umur_hari.days % 365) // 30
hari_now = (umur_hari.days % 365) % 30
print(f"{tahun_now} tahun, \n{bulan_now} bulan, \n{hari_now} hari")


'''hari 12'''

''' IF DAN ELSE STATEMENT '''
# if dan else 

# dari vidio tutorial pembelajaran
# # 1. if nya
# # 2. kondisinya
# # 3. aksinya

# nama = input("sebutkan nama = ")

# # program sebelumnya
# # if kondisi : aksi
# # program selanjutnya

# # program if inline
# if nama=="ridwan" : print(f"semoga {nama} sukses")
# print(f"haii {nama}")

# # program if indentation
# if nama=="ridwan" : 
#     print(f"semoga {nama} lolos snbp ")
#     print(f"semoga cita cita {nama} tercapai")
# print(f"haii {nama}, terimakasih")    

# # else statement
# if nama=="ridwan" :
#     print(f"semangat terus {nama}")
# else:
#     print(f"siapa kamu")
# print("akhir dari program atau program selanjutnya")  

# hasil mencoba ku

total_belanja = float(input("masukan total belanja mu ="))

if ( 200000 < total_belanja < 300000)  :
    print("kamu mendapat diskon 20%")
    harga_diskon = total_belanja - ((20 / 100) * total_belanja)
    print(f"total yang harus dibayar sebesar = {harga_diskon}")
else:
    print("mendapat potongan 20.000")
    harga_potong = total_belanja - 20000
    print(f"total belanja yang harus dibayar = {harga_potong}") 
print("terimakasih")    

''' elif statement'''
# elif statement

# dari vidio tutorial
# nama = input("ridwan")

# # elif
# if nama== "ridwan" : # kondisi 1
#     print(f"selamat malam {nama}") # aksi true 1
# elif nama== "fadil" : # kondisi 2
#     print(f"hai apa kabar {nama}") # aksi  true 2
# elif nama== "nazim" : # kondisi 3
#     print(f"sukses terus {nama}") # aksi true 3
# else:
#     print(f"maaf kamu siapa?")    # aksi false
# print("ini adalah program selanjutnya") 

# hasil percobaan 

angka1 = float(input("masukan angka pertama = "))
operasi = input("masukan operasi = ")
angka2 = float(input("masukan angka kedua = "))

if operasi== "+" :
    print(f"{angka1} + {angka2} = {angka1 + angka2}")
elif operasi== "-" :
    print(f"{angka1} - {angka2} = {angka1 - angka2}")
elif operasi== "*" :
    print(f"{angka1} * {angka2} = {angka1 * angka2}")
elif operasi== "/" :
    if angka2 ==0 : # dalam matematika tidak boleh dibagi dengan angka nol
        print("gabisa dibagi nol nih boss")
    else:
        print(f"{angka1} / {angka2} = {angka1 / angka2}")
elif operasi== "**" :
    print(f"{angka1} ** {angka2} = {angka1 ** angka2}")
elif operasi== "//" :
    print(f"{angka1} // {angka2} = {angka1 // angka2}")
elif operasi== "%" :
    print(f"{angka1} % {angka2} = {angka1 % angka2}")
else:
    print("error boosss!!!")


'''HARI 14'''

''' PERULANGAN / LOOP '''

# for kondisi :
#      aksi

# perulangan dengan list
list_angka = [2,4,6,8,10]
print(list_angka)

for list_ in list_angka :
    print(f"list ==> {list_}")

print("="*10)

# perulangan dengan range
for i in range(5) :   # (i) adalah variabel sementara.
    print(f"i berubah =>{i}")

print("="*10)

for angka in range(1,11,2) :  # (1) strart. (11) angka batas/berhenti sebelum. (2) merupakan step/langkah
    print(f"angka ={angka}")

print("="*10)

# perulangan dengan string

uhuy = "saya kece abis"

for kata in uhuy : # akan ditampilkan per huruf 
    print(kata)    # kecuali jika kamu menaruh range maka hasil kata yang diulang 

print("="*10)

for ulang in range(6) :
    print("saya kece abis")


'''HARI 15'''
# MEMPERBAIKI PROYEKK KALKULATOR BMI
# MEMBUAT MINI GAME TEBAK ANGKA 



'''HARI 16'''

'''WHILE LOOP'''
# while loop

# while kondisi :
#       aksi

# akhir program


angka = 10  
print(f"angka sekarang ={angka}")

while angka > 7 :   
    angka -= 1
    print(f"angka sekarang {angka}")
    print("kece baday")   

print("selesai")

# nilai variabel awal = 10
# while kondisi angka > 7 , karna angka = 10 maka benar
# masuk ke proses awal 10-1=9
# melanjutkan print
# balik lagi ke proses while
# karena 9 > 7 = true 
# lanjut lagi, sampai
# 7 > 7 = false , program berhenti

'''CONTINUE==PASS==BREAK'''
# continue==pass==break

# pass => dia berfunngsi menjadi dummy,tidak dijjalankan/akan dilewati
# ini hanya pengenalan pass belum mendalam

angka = 0
print(f"percobaan {angka}")

while angka < 6 :
    angka += 1
    
    if angka == 5 :
        pass # pass digunakan sebagai pengisi agar code tetap berjalan 
             # walau masih kosong
    print(angka)

# continue

angka = 0

while angka < 6 :
    angka += 1
    print(f"percobaan {angka}")  # aksi 1
    if angka == 5 :
        print("masih kurang nih lagi ah")
        continue # akan langsung melompat ke awal tanpa memproses "ayo lagi"

    print("ayo lagi") # aksi 2

# break 

angka = 0 

while angka < 10 :
    angka += 1
    print(f"angka => {angka}")
    if angka == 7 :
        print("cukup")
        break  # dipaksa berhenti
    print("oke lanjut")
print("selesai")        

data = int(input("mari berhitung = "))
angka = 0

while True :
    angka += 1
    print(f'angka {angka}')

    if angka == data :
        print('selesai berhitung')
        break
print("selesai deh")  

''' LATIHAN PERULANGAN MEMBUAT SEGITIGA '''
# latihan perulangan membuat segitiga

tinggi = 7
 
# 1. menggunakan for

jumlah = 1
print("="*20)
for i in range(tinggi) :
    print("*"*jumlah)

    jumlah += 1

print("="*20)

# 2. menggunakan while 

jumlah = 1

print("="*20)
while True:
    print("*"*jumlah)
    jumlah += 1

    if jumlah >= tinggi :
        break # berhenti jika jumlah bintang di baris sudah lebih dari sama dengan tinggi(7)
print("="*20)

#  3. menggunakan while hanya ganjil

jumlah = 1
                           # kenapa di modulus dengan 2
print("="*20)              # agar mendapat hasil 1 dan 0 (true / false)
while True:                # kondisi benar 
    if (jumlah%2):         # kenapa 2 karena ketika jumlah genap maka hasil modulus adalah 0
        print("*"*jumlah)  # jika nol lanjut ke else jumlah ditambah 1
        jumlah += 1        # balik lagi ke atas karena jumlah menjadi ganjil maka hasilnya 1
    else:                  # dan di print 
        jumlah +=1
        continue
    if jumlah >= tinggi:
        break
print("="*20)

# 4. menggunakan while untuk membuat segitiga

jumlah = 1
spasi = int(tinggi/2)    # menggunakan integer agar dibulatkan ke bawah

print("="*20)
while True:
    if (jumlah%2):
        print(" "*spasi,"*"*jumlah)
        jumlah += 1
        spasi -=1
    else:
        jumlah += 1
        continue
    if jumlah >= tinggi :
        break
print("="*20)

# 4. menggunakan while untuk membuat segitiga # PR

jumlah = 1
spasi = int(tinggi/2)

print("="*20)
while True:
    if (jumlah%2):
        print(" "*spasi,"*"*jumlah)
        jumlah += 1
        spasi -=1
    else:
        jumlah += 1
        continue
    if jumlah >= tinggi:
        break
spasi = 0
jumlah -= 2
while True:
    if (jumlah%2):
        spasi +=1
        print(" "*spasi,"*"*jumlah)
        jumlah -= 1
    else:
        jumlah -= 1
        continue
    if jumlah == 0:
        break
print("="*20)

'''HARI 17'''
# MENGUPGRADE KAKULATOOR SEDERHANA

'''HARI 18'''
# MEMBUAT PROYEK DI FILE ORDE_END.PY

'''HARI 19'''
# LIST

##  list kumpulan angka
data_angka = [1,2,3,4,5]
print(data_angka)
## list kumpulan string
data_str = ["satu","dua","tiga","empat"]
print(data_str)
## list kumpulan boolean
data_bool = [True,False,False,True]
print(data_bool)
## list campuran
data_campuran = ["satu",2,3,False,True,"empat"]
print(data_campuran)
## cara alternatif membuat list
data_range = range(1,11,2) # start-stop-step 
print(data_range) 
data_range = list(data_range)
print(data_range)

# membuat list dengan for loop , list comprehension
pake_for = [i*2 for i in range(1,11)]
print(pake_for)
# pake for if
pake_for_if = [i*3 for i in range(1,11,2) if i != 9]
print(pake_for_if)
coba = [ i for i in range(1,20,2) if i == 9]
print(coba)

'''HARI 20'''
''' OPERASI LIST'''
# OPERASI LIST

# indeks 0/-3  |  1/-2  |   3/-1
data = ["Fadil","Saadi","Zahid"] 
# mengabil data dari list
print(f"data ke 0 \tadalah \t{data[0]}")
data_1 = data[1]
print(f'data ke 1 \tadalah \t{data_1}')
print(f"data terakhir \tadalah \t{data[-1]}")
# mengambil atau mengetahui jumlah data dalam list
jum_data = len(data)
print(f'jumlah data list \tadalah \t{jum_data}')

## memanipulasi data
print('='*15)
print(f"data sebelumnnya {data}")
print('='*15)
# menambah data list
data.insert(2,"Ridwan")
print(f"data setelah {data}")
# menambah data di akhir
data.append("Nazim")
print(f"data terbaru {data}")

# menggabungakn list
data_2 = ["Alesha","Indah","Kimmy"]
data_3 = ["Freya","Virgi"]
data.extend(data_2)
print(f"data gabungan \n{data}")
data_2.extend(data_3+data)
print(f"data gabungan \n{data_2}")

# merubah data list
data[2] = "Bunga"
print(data)

# menghapus data
data_2.remove("Ridwan")
print(data_2)
# data_2.remove("ridwan") # akan error karena beda dengan yang ada di list

# menghapus data terakhir
data_2.pop()
print(data_2)
# mengambil data terakhir saja
data_2 = data_2.pop()
print(data_2)

# coba coba
user = ["ujang","ikbal"]
user.append(input("masukan nama = ").title())
print(user)

'''HARI 21'''
''' OPERASI LIST '''
# operasi list

data_angka = [1,3,5,7,9,4,6,4,7,9] 
data_string = ["Ucup","Parto","Ujang","Komeng","Usep","Edi"]
print("="*20)
print(f"data angka \t= \t{data_angka} \ndata string \t= \t{data_string}")
print("="*20)

# count data (menghitung jumlah)
angka9 = data_angka.count(9)
print(f"jumlah angka 9 pada data = {angka9}")
angka2 = data_angka.count(2)
print(f"jumlah angka 2 pada data = {angka2}") # nol karena tidak ada angka 2 dalam data

# mengetahui posisi/indeks data
data1 = data_string.index("Ujang")
print(f"Ujang ber indeks = {data1}")
# data2 = data_string.index("ujang") # akan error karena tidak sama dengan yang di data
# data3 = data_string.index("Ridwan") # akan error karena tidak ada dalam data

# mengurutkan list (sort) dari awal a-z/0-9
print(f"sebelum = {data_angka}")
data_angka.sort()
print(f"sesudah = {data_angka}")

print(f"sebelum = {data_string}")
data_string.sort()
print(f"sesudah = {data_string}")

# mengurutkan list (reverse) dari akhir z-a/9-0
print(f"sebelum = {data_angka}")
data_angka.reverse()
print(f"sesudah = {data_angka}")

print(f"sebelum = {data_string}")
data_string.reverse()
print(f"sesudah = {data_string}")

'''hari 22'''
'''memubuat  program perpustakaan.py'''

'''HARI 23'''
## SENIN 30 MARET 2026

'''Teknik menduplikat list'''
#list a
a = ["ari","ara","ira"]
print(f"list A = {a}")

b = a  # hal ini hanya akan menjadikan nya nama panggilan lain
print(f"list B = {b}")

# coba mengubah isi list a = maka list b akan ikut  berubah mengikuti a
a[1] = "eri" 
print("="*15)
print(f"list A = {a}")
print(f"list B = {b}")
a.sort()
print("="*15)
print(f"list A = {a}")
print(f"list B = {b}")

# kenapa hal tersebut bisa terjadi?
print("="*15)
print(f"address a ={hex(id(a))}")
print(f"address b ={hex(id(b))}")
# keduanya memiliki addres/alamat/tempat yang sama jadi bila salah satu dirubah maka sisanya akan ikut berubah

# cara menduplikat list yang benar
print("="*15)
c = a.copy()
print(f"address a ={hex(id(a))}")
print(f"address b ={hex(id(b))}")
print(f"address c ={hex(id(c))}")
# disini terlihat address c berbeda dengan a jadi bisa dianggap ini list baru dengan isi yang sama
print("="*15)
print(f"list A = {a}")
print(f"list B = {b}")
print(f"list C = {c}")

# mencoba mengganti isi list
c[1] = "iwan"
print("="*15)
print(f"list A = {a}")
print(f"list B = {b}")
print(f"list C = {c}")

c[2] = "bunga"
print("="*15)
print(f"list A = {a}")
print(f"list B = {b}")
print(f"list C = {c}")

'''HARI 24'''
# SELASA 31 MARET 2026

'''pengenalan nasted list/list bersarang'''

# list biasa
data1 = [1,2,3,4,5]
data2 = [6,7,8,9]
data3 = [10,11,12,13]
print(f"list biasa = {data1+data2+data3}\n")

# nasted list
list_nasted = [data1,data2,data3,14,15,"satu"]
print(f"nasted list = {list_nasted}\n")

# contoh pengggunaan
peserta1 = ["dadang",30,"laki-laki"]
peserta2 = ["irma",40,"perempuan"]
peserta3 = ["parmo",55,"laki-laki"]

list_peserta = [peserta1,peserta2,peserta3]
print(f"peserta = {list_peserta}\n")

for peserta in list_peserta :
    print(f"nama \t\t: {peserta[0]}")
    print(f"umur \t\t: {peserta[1]} tahun")
    print(f"jenis kelamin \t: {peserta[2]}\n")

# dengan reference
list_copy = list_peserta.copy()
print(f"peserta = {list_copy}\n")
peserta1[0] = "alam"
print(f"peserta = {list_copy}\n")
print(f"peserta = {list_peserta}\n")

print(f"alamat : {hex(id(list_peserta))}")
print(f"alamat : {hex(id(list_copy))}")
## hal tersebut bisa terjadi karena data yang dicopy merupakan data bersama  sedangkan adta yang ditambhak kan atau  dikurangi adalah data sendiri
### mengapa hal ini bisa terjadi akan dijelaskan di tutorial selanjutnya


'''hari 25'''
# RABU 1 APRIL 2026

''' lanjutan mengenai nasted list --> deep copy'''

data1 = [1,3,5]
data2 = [6,8,10]

data_gabungan = [data1,data2,20]
data_copy = data_gabungan.copy()

print(f"data asli = {data_gabungan}")
print(f"data copy = {data_copy}\n")

# mengambil data dari nasted list
data = data_gabungan[1][2] # akan mengambil data ke 1 di "data_gabungan" yaitu "data2" lalu mengambil data ke 2 di "data2"
print(f"pengambilan data = {data}\n")

# address list
print(f"address asli = {hex(id(data_gabungan))}")
print(f"address copy = {hex(id(data_copy))}\n")

#address member ke 1
print(f"address asli = {hex(id(data_gabungan[1]))}")
print(f"address copy = {hex(id(data_copy[1]))}\n")

data_gabungan[1][0] = 23
data_gabungan[2] = 2

print(f"data asli = {data_gabungan}")
print(f"data copy = {data_copy}\n")
# kenapa data_copy indeks ke 2 tidak ikut berubah? karena data tersebut berada di dalam list data_gabungan bukan data1/data2

from copy import deepcopy

data_deepcopy = deepcopy(data_gabungan)
print(f"address asli \t\t= {hex(id(data_gabungan))}")
print(f"address copy \t\t= {hex(id(data_copy))}")
print(f"address deepcopy \t= {hex(id(data_deepcopy))}\n")

data1[0] = 100
print(f"data asli = {data_gabungan}")
print(f"data copy = {data_copy}")
print(f"data deepcopy = {data_deepcopy}\n")

print(hex(id(data_gabungan[0])) == hex(id(data_deepcopy[0])))


'''HARI 26'''
# KAMIS 2 APRIL 2026

'''LOOPING DARI LIST'''

# for loop
print("for loop")
angka = [2,4,6,8,]
for i in angka :
    print(f"angka = {i}")

peserta = ["bayu","bunga","saad"]
for o in peserta :
    print(f"nama = {o}")

# for loop dan range
print("\nfor loop dan range")
digit = [2,3,4,5,6]
panjang = len(digit)
for  i  in range(panjang):
    print(f"angka = {digit[i]}")

# while loop
print("\nwhile loop")
jumlah = [2,3,4,5,6]
panjang = len(jumlah)
i = 0

while i < panjang:
    print(f"angka = {jumlah[i]}")
    i += 1

# list comprehension
print("\nlist comprehension")
gabung = ["ijat",4,5,"ipul"]
[print(f"data = {i}") for i in gabung]

kuadrat = [i**2 for i in jumlah]
print(kuadrat)

# enumerate
print("enumerate")
gabung = ["ijat",4,5,"ipul"]
for i,a in enumerate(gabung):
    print(f"indeks : {i} \tdata : {a}")
for x in enumerate(gabung):
    print(f"data = {x}")


'''HARI 27'''
# 16 APRIL 2026

'''LATIHAN LIST'''

# program sederhana pencatat judul dan penulis buku
buku = []
print("="*10,"program dimulai","="*10)
while True:
    judul = input("\n\nmasukan judul buku(1=selesai) \t: ").title()
    if judul == "1":
        print("="*10,"program selesai","="*10)  
        break
    penulis = input("masukan penulis \t: ").title()
    pustaka = [judul,penulis]
    buku.append(pustaka)

    print("\ndaftar buku")
    for no,book in enumerate(buku):
        print(f"{no+1}| judul : {book[0]} | penulis : {book[1]}" )

    
'''HARI 28'''
# 17 APRIL 2026

'''TUPLES DAN SET'''

# list biasa
data = [1,1,2,3]
print(data)

# tuples
# list tetap dan tidak bisa diubah
data1 = (1,2,3,4,5)
print(data1)
print(data1[0])
# yanng tidak bisa dilakuakn oleh tuples
# data1.append(1)
# data1[3] = "2"

# set
data2 ={1,1,3,4,4}
print(data2)
# yanng tidak bisa dilakuakn oleh tuples
# print(data2[2])
# data2.append(3)
# data2[0] = "10"

# DICTIONARY

# list -> array, mengakses dengan menggubakab indeks
list_ = ['ajib','ijab','ijub']
print(list_[1])

# dictionary (dict) -> associative array
# identifier -> key

data_dict ={
    'key':'value',
    'ai':'ajib',
    'ia':'ijab',
    'iu':'ijub',
    'ank':20,
    'list':list_,
}

print(data_dict['ai'])
print(data_dict['ank'])
print(data_dict['list'])