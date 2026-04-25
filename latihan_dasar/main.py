""" PEMBELAJARAN PYTHON 1 """
""" HARI 1-10 """
    # VARIABEL
    # TIPE DATA
    # INPUT USER
    # OPERASI ARITMATIKA
    # KONVERSI SUHU
    # OPERASI KOMPARASI
    # OPERASI LOGIKA BOOLEAN
    # LATIHAN LOGIKA DAN KOMPARASI
    # OPERASI BITWISE, BINER, BINARY
    # OPERASI PENYINGKATAN 
    # PENGENALAN STRING
    # OPERASI DAN MANIPULASI STRING
    # OPERASI DALAM BENTUK METHODS
    # FORMAT STRING 
    # WIDTH DAN MULTILINE


'''HARI 1'''

#prin hallo dunia
print ("halo bos")
print("selamat pagi")

'''HARI 2'''

#variabel
d = 8     # A merupakan variabel. (=)merupakan assigment/tugas. 8 adalah nilainya
b = 2
c = 3
d = b

#pemanggilan
print(d)
print(b)
print("nilai d =",d)

#tips menggunakan VSCOdE
#COPY = alt+shif+bawah
#MENGGESER = alt+bawah/atas
#MENGGANTI KATA SAMA = ctrl d+pencet setelahnya


#penamaan 
umur = 18
tinggi_badan = 180 #tidak boleh menggunaakan spasi harus (_)

#tipe data

#angka / bilangan bulat (integer)
data_integer = 10 #tanpa koma
print("data1 :",data_integer)
#angka / bilangan desimal (float)
data_float = 91.5
print("data2 :",data_float)
#kumpulan karakter / huruf (string)
data_string = "ridwan 18"
print("data3 :",data_string)
#biner true/false (boolean)
data_bool = True
data_bool_2 = False
print("data4 :",data_bool)
print("data5 :",data_bool_2)

#cara mengetahui tipe data
print("data1 bertipe :",type(data_integer))
print("data2 bertipe :",type(data_float))
print("data3 bertipe :",type(data_string))
print("data4 bertipe :",type(data_bool))
##TIPE dATA KHUSUS##

#data complex
data_complex = complex((5.5),(20))
print("data khusus :",data_complex)

#tipe data dari bahasa c
from ctypes import c_double

data_c_double = c_double(20.2)
print("data c char :",data_c_double)
print("data c char bertipe :",type(data_c_double))

#CASTING (MERUBAH TIPE DATA MENJADI TIPE DATA YANG LAIN)
#TIPE DATA : int, float, str, bool


#INTEGER
print("=====INTEGER=====")
data_int = 10
print("data :",data_int,"bertipe :",type(data_int))

data_float =float(data_int)
data_str   =str(data_int)
data_bool  =bool(data_int) # false jika nilai : 0
print("data :",data_float,"tipe :",type(data_float))
print("data :",data_str,"tipe :",type(data_str))
print("data :",data_bool,"tipe :",type(data_bool))

#FLOAT
print("=====FLOAT=====")
data_float = 10.8
print("data :",data_float,"bertipe :",type(data_float))

data_int =int(data_float)  #dibulatkan ke bawah
data_str   =str(data_float)
data_bool  =bool(data_float)
print("data :",data_int,"tipe :",type(data_int))
print("data :",data_str,"tipe :",type(data_str))
print("data :",data_bool,"tipe :",type(data_bool))

#STRING
print("=====STRING=====")
data_str = "203"
print("data :",data_str,"bertipe :",type(data_str))

data_int   =int(data_str) #str harus angka
data_float =float(data_str) #str harus angka dan tidak boleh koma
data_bool  =bool(data_str) #false jika str kosong
print("data :",data_int,"tipe :",type(data_int))
print("data :",data_float,"tipe :",type(data_float))
print("data :",data_bool,"tipe :",type(data_bool))

#BOOLEAN
print("=====BOOLEAN=====")
data_bool = False
print("data :",data_bool,"bertipe :",type(data_bool))

data_int  =int(data_bool)
data_float =float(data_bool)
data_str   =str(data_bool)
print("data :",data_int,"tipe :",type(data_int))
print("data :",data_float,"tipe :",type(data_float))
print("data :",data_str,"tipe :",type(data_str))

'''HARI 3'''

#INPUT USER
data = input("masukian nama :")
print("data :",data,"tipe data :",type(data)) #data pasti string

#jika ingin mengambil nilai angka : int/float
angka = float(input("masukan desimal :"))
angka = int(input("masukan bilangan bulat :"))
print("data :",angka,"tipe :",type(angka))

#boolean
biner1 = bool(input("masukan bool :")) #akan selalu true
print("data :",biner1,"tipe :",type(biner1))
biner = bool(int(input("masukan data bool :")))
print("data :",biner,"tipe :",type(biner)) #false jika 0 dan tidak bisa karakter

#OPERASI ARITMATIKA 

a = 3
b = 2

#tambah (+)
hasil = a + b
print(a,"+",b,"=",hasil)
#kurang (-)
hasil = a - b
print(a,"-",b,"=",hasil)
#kali (*)
hasil = a * b
print(a,"*",b,"=",hasil)
#bagi (/)
hasil = a / b
print(a,"/",b,"=",hasil)

#eksponen / pangkat (**)
hasil = a ** b
print(a,"**",b,"=",hasil)

 #modulus / sisa bagi (%)
hasil = a % b
print(a,"%",b,"=",hasil)

#floor division (//) #membagi tetapi di bulatkan ke bawah
hasil = a // b
print(a,"//",b,"=",hasil)

'''PRIORITAS OPERASI'''
'''
1. kurung ()
2. eksponen **
3. perkalian/pembagian/modulus/floor division * / % //
4. pertambahan pengurangan + -
'''
x = 10
y = 5
z = 3
# cintoh rumitnya
hasil = x - y / x // z * y + y % z
print(x,'-',y,'/',x,'//',z,'*',y,'+',y,'%',z,'=',hasil)

#contoh sederhana
hasil = x / (y + y) * z
print( x,'/','(',y,'+',y,')','*',z,'=',hasil)
print(type(hasil))

hasil = x // z
print(x,'//',z,'=',hasil)
print(type(hasil))

#hasil akan bertipe float jika dibagi / selain itu bertipe int

'''HARI 4'''

#konversi satuan suhu
'''latihan konversi satuan temperatur'''
#mengkonversi satuan suhu ke satuan suhu yang lain

#celcius
'''celcius'''
celcius = float(input('masukan celcius :'))
print('suhu :',celcius,'C')
#reamur
reamur = (4/5)*celcius
print('reamur :',reamur,'RE')
#fahrenheit
fahrenheit = ((9/5)*celcius)+32
print('fahrenheit :',fahrenheit,'F')
#kelvin
kelvin = celcius + 273
print('kelvin :',kelvin,'K')

#reamur
'''reamur'''
reamur = float(input('masukan reamur :'))
print('suhu :',reamur,'RE')
#celcius
celcius = (5/4)*reamur
print('celcius :',celcius,'C')
#fahrenheit
fahrenheit = ((9/4)*reamur)+32
print('fahrenheit :',fahrenheit,'F')
#kelvin
kelvin = ((5/4)*reamur)+273
print('kelvin :',kelvin,'K')

#fahrenheit
'''fahrenheit'''
fahrenheit = float(input('masukan fahrenheit :'))
print('suhu :',fahrenheit,'F')
#celcius
celcius = 5/9*(fahrenheit-32)
print('celcius :',celcius,'C')
#reamur
remaur = 4/9*(fahrenheit-32)
print('fahrenheit :',fahrenheit,'F')
#kelvin
kelvin = ((5/9*(fahrenheit-32))+273)  #PR 
print('kelvin :',kelvin,'K')

#kelvin
'''kelvin'''
kelvin = float(input('masukan kelvin :'))
print('suhu :',kelvin,'K')
#celcius
celcius = kelvin-273
print('celcius :',celcius,'C')
#reamur
reamur = 4/5*(kelvin-273)
print('reamur :',reamur,'RE')
#fahrenheit
fahrenheit = (9/5*(kelvin-273))+32    #PR
print('fahrenheit :',fahrenheit,'F')



'''OPERASI KOMPARASI / PERBANDINGAN'''
# operasi komparasi / perbandingan
# hasil operasi komparasi adalah bool (true/false)
''' < , > , <= , >= , == , !='''



a = 5
b = 7

# kurang dari <
print("------------ <")
hasil = a < 8
print(a,'<',8,'=',hasil)
hasil = a < 4
print(a,'<',4,'=',hasil)
hasil = b < a 
print(b,'<',a,'=',hasil)
hasil = a < b
print(a,'<',b,'=',hasil)

# lebih dari >
print("------------ >")
hasil = a > 8
print(a,'>',8,'=',hasil)
hasil = a > 4
print(a,'>',4,'=',hasil)
hasil = b > a 
print(b,'>',a,'=',hasil)
hasil = a > b
print(a,'>',b,'=',hasil)

# kurang dari sama dengan <=
print("------------ <=")
hasil = a <= 8
print(a,'<=',8,'=',hasil)
hasil = a <= 5
print(a,'<=',5,'=',hasil)
hasil = b <= a 
print(b,'<=',a,'=',hasil)
hasil = a <= b
print(a,'<=',b,'=',hasil)

# lebih dari sama dengan >=
print("------------ >=")
hasil = a >= 8
print(a,'>=',8,'=',hasil)
hasil = a >= 5
print(a,'>=',5,'=',hasil)
hasil = b >= a 
print(b,'>=',a,'=',hasil)
hasil = a >= b
print(a,'>=',b,'=',hasil)

# sama dengan ==
print("------------ ==")
hasil = a == 8
print(a,'==',8,'=',hasil)
hasil = a == 5
print(a,'==',5,'=',hasil)
hasil = b == a 
print(b,'==',a,'=',hasil)

# tidak sama dengan !=
print("------------ !=")
hasil = a != 8
print(a,'!=',8,'=',hasil)
hasil = a != 5
print(a,'!=',5,'=',hasil)
hasil = b != a 
print(b,'!=',a,'=',hasil)

# 'is dan is not' sebagai komparasi objek identity
x = 3  # ini adalah assigment membuat object
y = 3
print("object identity (is)")
print('x =',x,'id =',hex(id(x))) # jika dua variabel atau object memiliki nilai yang sama
print('y =',y,'id =',hex(id(y))) # maka akan di taruh di tempat yang sama

hasil = x is y
print('x is y =',hasil)
hasil = x is 3 
print('x is 3 =',hasil)
hasil = x is 4 
print('x is 4 =',hasil)

x = 3  # ini adalah assigment membuat object
y = 5
print("object identity (is not)")
print('x =',x,'id =',hex(id(x))) # jika dua variabel atau object memiliki nilai yang sama
print('y =',y,'id =',hex(id(y))) # maka akan di taruh di tempat yang sama

hasil = x is not y
print('x is y =',hasil)
hasil = x is not 3 
print('x is 3 =',hasil)
hasil = x is not 4 
print('x is 3 =',hasil)

# percobaan is dan is not
c = 2000
d = 2000

print('c =',c,'id =',hex(id(c)))
print('d =',d,'id =',hex(id(d)))

hasil = c is d
print('c is d =',hasil)

a = 2000
b = int("2000") # Kita buat b dari string agar Python tidak tahu isinya 2000 sejak awal

print(f"Nilai a: {a}, Nilai b: {b}")
print(f"Apakah a == b? {a == b}") # Pasti True (Nilainya sama)
print(f"Apakah a is b? {a is b}") # Kemungkinan besar False!

'''HARI 5'''

'''OPERASI LOGIKA ATAU BOOLEAN'''

#operasi logika atau  boolean
# NOT, OR, AND, XOR
# ururtan penyelesaian not -> and -> xor -> or
# NOT
print('===not===')
a = True
b = False
c = not a  # data c bukan a(true) yang berarti false
print('data a =',a)
print('data b =',b)
print('---------------not')
print('data c =',c)

# OR   (jika ada nilai true maka true)
print('===or===')
a = True
b = True
c = a or b
print(a,' or',b,' =',c)
a = True
b = False
c = a or b
print(a,' or',b,'=',c)
a = False
b = True
c = a or b
print(a,'or',b,' =',c)
a = False
b = False
c = a or b
print(a,'or',b,'=',c)

# AND   (jika ada nilai false maka false)
print('===and===')
a = True
b = True
c = a and b
print(a,' and',b,' =',c)
a = True
b = False
c = a and b
print(a,' and',b,'=',c)
a = False
b = True
c = a and b
print(a,'and',b,' =',c)
a = False
b = False
c = a and b
print(a,'and',b,'=',c)

# XOR  
# true berjumlah ganjil maka hasil true
# true berjumlah genap maka hasil false
print('===xor===')
a = True
b = True
c = a ^ b
print(a,' xor',b,' =',c)
a = True
b = False
c = a ^ b
print(a,' xor',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'xor',b,' =',c)
a = False
b = False
c = a ^ b
print(a,'xor',b,'=',c)

#coba coba
# true berjumlah ganjil maka hasil true
# true berjumlah genap maka hasil false
print('===xor===')
a = True
b = True
c = True
d = a ^ b ^ c
print(a,' xor',b,'xor',c,' =',d)
a = True
b = False
c = True
d = a ^ b ^ c
print(a,' xor',b,'xor',c,' =',d)
a = False
b = True
c = False
d = a ^ b ^ c
print(a,'xor',b,'xor',c,' =',d)
a = False
b = False
c = False
d = a ^ b ^ c
print(a,'xor',b,'xor',c,'=',d)
a = False
b = False
c = False
d = True
e = a ^ b ^ c ^ d
print(a,'xor',b,'xor',c,'xor',d,'=',e)
a = True
b = True
c = True
d = False
e = a ^ b ^ c ^ d
print(a,'xor',b,'xor',c,'xor',d,'=',e)

''' LATIHAN LOGIKA DAN KOMPARASI'''

 # latihan logika dan koparasi 
 # MEMBUAT GABUNGAN AREA DARI RENTANG ANGKA
 #++++4--------12++++
In_USER = float(input('masukan angka \nkurang dari 4 \natau \nlebih dari 12 \nnilai :'))

# ++++4 (membenarkan angka <4 )
kurang_dari = In_USER < 4
print("hasil <4:",kurang_dari)
# 12+++ (membenarkan angka >12 )
lebih_dari = In_USER > 12
print("hasil >12:",lebih_dari)
# membenarkan nilai keduannya 
hasil_jadi = kurang_dari or lebih_dari
print("hasil input :",hasil_jadi)


 # MEMBUAT IRISAN AREA DARI RENTANG ANGKA
 #----4++++++12-----
In_USER = float(input('masukan angka \nlebih dari 4 \natau \nkurang dari 12 \nnilai :'))

# 4++++ (membenarkan angka >4 )
lebih_dari = In_USER > 4
print("hasil >4:",lebih_dari)
# ----12 (membenarkan angka <12 )
kurang_dari = In_USER < 12
print("hasil <12:",kurang_dari)
# membenarkan nilai keduannya 
hasil_jadi = lebih_dari and kurang_dari
print("hasil input :",hasil_jadi)

# PR MENCARI NILAI (TRUE OR FALSE) DARI SOAL
# 1. ---0+++5---8+++11---
# 2. +++0---5+++8---11+++
''' PR'''


print(20*'=')

# 1. ---0+++5---8+++11---
# nilai lebih dari 0 kurang dari 5 lebih dari 8 kurang dari 11
In_USER = float(input('masukan angka \nlebih dari 0 \ndan \nkurang dari 5' \
' \natau \nlebih dari 8 \ndan\nkurang dari 11 \nnilai :'))
# > 0 (lebih dari 0) dan < 5(kurang dari 5)
lebih_0 = In_USER > 0
kurang_5 = In_USER < 5
#hasil_1 = lebih_0 and kurang_5
#print("hasil 0+++5 :",hasil_1)
# > 8 (lebih dari 8) dan < 11 (kurang dari 11)
lebih_8 = In_USER > 8
kurang_11 = In_USER < 11
#hasil_2 = lebih_8 and kurang_11
#print("hasil 8+++11 :",hasil_2)
# mencari true/false sebenarnya
#hasil_akhir = hasil_1 or hasil_2
hasil_baru = (0 < In_USER < 5) or (8 < In_USER < 11)
print("hasil akhir :",hasil_baru)



print(20*'=')

# 2. +++0---5+++8---11+++
# nilai kurang dari 0 lebih dari 5 kurang dari 8 lebih dari 11
In_USER = float(input('masukan angka \nkurang dari 0 \natau \nlebih dari 5' \
' \ndan \nkurang dari 8 \natau \nlebih dari 11 \nnilai :'))
# < 0 (kurang dari 0)
kurang_0 = In_USER < 0
#print("hasil < 0 :",kurang_0)
# > 5 (lebih dari 5) dan < 8 (kurang dari 8)
lebih_5 = In_USER > 5
kurang_8 = In_USER < 8
##hasil_1 = lebih_5 and kurang_8 # ATAU (hasil_1 =5 < In_USER < 8)
##print("hasil 5+++8 :",hasil_1)
# > 11 (lebih dari 11)
lebih_11 = In_USER > 11
##print("hasil > 11 :",lebih_11)
# mencari true/false sebenarnya
##hasil_akhir = kurang_0 or hasil_1 or lebih_11 
hasil_baru = (In_USER < 0) or (5 < In_USER < 8) or (In_USER > 11)
print("hasil akhir :",hasil_baru)

# # bentuk lain dari kolom coment youtube
# inputUser = float(input("masukkan angka:"))
# a = (inputUser > 0)
# b = (inputUser < 5)
# c = (inputUser > 8)
# d = (inputUser < 11)

# isCorrect = a and b or  c and d
# print("angka yang anda masukkan :", isCorrect)

# print("\n",20*"=","\n")
# inputUser = float(input("masukkan angka:"))

# a = (inputUser > 5)
# b = (inputUser < 0)
# c = (inputUser > 11)
# d = (inputUser < 8)

# isCorrect = b or a and d or c
# print("angka yang anda masukkan :", isCorrect)


'''HARI 6'''

# OPERASI BITWISE ,OPERASI BINER , BINERY
''' OPERASI BITWISE-OPERASI BINER-BINERY '''
a = 4
b = 7
# or(|) and(&) xor(^) not(~)
# bitwise or (|)
c = a | b 
print(8*"=","OR",8*"=")
print('nilai :',a,'binary :',format(a,'08b'))
print('nilai :',b,'binary :',format(b,'08b'))
print(28*'-','(|)')
print('nilai :',c,'binary :',format(c,'08b'))
# bitwise and (&)
c = a & b 
print(8*"=","AND",8*"=")
print('nilai :',a,'binary :',format(a,'08b'))
print('nilai :',b,'binary :',format(b,'08b'))
print(28*'-','(&)')
print('nilai :',c,'binary :',format(c,'08b'))
# bitwise xor (^)
c = a ^ b 
print(8*"=","XOR",8*"=")
print('nilai :',a,'binary :',format(a,'08b'))
print('nilai :',b,'binary :',format(b,'08b'))
print(28*'-','(^)')
print('nilai :',c,'binary :',format(c,'08b'))
# bitwise not (~)
c = ~a 
print(8*"=","not",8*"=")
print('nilai :',a,'binary :',format(a,'08b'))
print(28*'-','(not)')
print('nilai :',c,'binary :',format(c,'08b')) # 0 di ikutkan bagian kanan jadi 5 satuan ke kanan
d = 0b00000100 # merupakan binary dari 4
e = 0b11111111 # mencari kebalikan yang sebenarnya
print(28*'-','(^)')
print('nilai :',e ^ d,'binary :',format(e ^ d,'08b'))

# shifting (menggeser)
# shif right (menggeser ke kanan) (>>)
#c = a >> 2
print(8*'=','>>',8*'=')
print('nilai :',a,'binary :',format(a,'08b'))
print(28*'-','(>>)')
print('nilai :',a >> 2,'binary :',format(a >> 2,'08b'))
# shif left (menggeser ke kanan) (<<)
#c = a << 2
print(8*'=','<<',8*'=')
print('nilai :',a,'binary :',format(a,'08b'))
print(28*'-','(<<)')
print('nilai :',a << 2,'binary :',format(a << 2,'08b'))

# OPERASI YANNG DAPAT DILAKUKAN DENGAN PENYINGKATAN
''' OPERASI PENYINGKATAN '''

# operasi ditambah dengan assigment

a = 7 # ini adalah assigment
print('nilai a :',a)

# operasi (penjumlahan, pengurangan, pembagian, perkalian)
a += 1 # artinya a = a + 1 
print('\nnilai a += 1 :',a)
a -= 2 # artinya a = a - 2
print('nilai a -= 2 :',a)   # operasi berikutnya akan mengambil nilai a yang baru
a *= 2 # artinya a = a * 2 
print('nilai a *= 2 :',a)
a /= 2 # artinya a = a / 2
print('nilai a /= 2 :',a)

b = 5
print('\nnilai b :',b)
# operasi (pangkat, modulus, floor division)
b **= 2 # artinya b = b ^ 2
print('\nnilai b **= 2 :',b)
b //= 3 # artinya b = b // 3
print('nilai b //= 3 :',b)
b %= 3 # artinya b = b % 3
print('nilai b %= 3 :',b)

# operasi bitwise
# or
c = True
print('\nnilai c :',c)
c |= False
print('nilai c "c |= false" menjadi :',c)
c = False
print('nilai c :',c)
c |= False
print('nilai c "c |= false" menjadi :',c)
# and
c = True
print('\nnilai c :',c)
c &= False
print('nilai c "c &= false" menjadi :',c)
c = True
print('nilai c :',c)
c &= True
print('nilai c "c &= true" menjadi :',c)
# xor
c = True
print('\nnilai c :',c)
c ^= False
print('nilai c "c ^= false" menjadi :',c)
c = True
print('nilai c :',c)
c ^= True
print('nilai c "c ^= true" menjadi :',c)

# shif right/left (<<>>)
d = 0b0010
print('\nnilai d :',d,format(d,'05b'))
d >>= 1
print('nilai d >>= 1 :',d,'menjadi :',format(d,'05b'))
d <<= 3
print('nilai d <<= 3 :',d,'menjadi :',format(d,'05b'))


'''HARI 7'''

# pengenalan string
''' PENGENALAN STRING '''
str = "anak bagus"
print(str)
print(type(str))

# 1. cara membuat string
'''
   1. menggunakan single quote '...'
   2. menggunakan double quote "..."
'''
# keduanya bisa digunakan, kegunaan sebenarnya ketika diharuskan ada tanda petik di dalam kalimat
# contoh : jum'at, "halo apa kabar?"
print(10*"=")
print("jum'at")
print('"halo apa kabar?"')

# 2. menggunakan tanda \ untuk membuat tanda ' dan \ masuk dalam string
print(10*"=")
print("hari ini adalah hari jum\'at") # \ menegaskan bahwa ' termasuk dalam srting
print("tap MPR\\NO.IV\\2000")

# backlash (menggeser kekanan) \t
print(10*"=")
print('aku \tdia,menjauh')
print('aku \t\tdia,semakin menjauh')
#backspace (menghapus jarak di kiri) \b
print(10*"=")
print('aku   \bdia,mendekat')
print('aku   \b\b\bdia,semakin mendekat')

# new line 
# \n memindahkan ke baris baru
# \r menggeser kusor ke paling kiri
# \r\n menggeser kusor ke paling kiri dan memindahkan ke baris baru
print(10*"=")
print('satu \ndua') # lf : unix, macos, linux
print('satu \rdua') # akan menggeser kusor ke paling kiri dan menimpa teks sebelumnya
print('sepuluh \rdua') # cr : commodore, acorn, lips
print('satu \r\ndua') # hasilnya sama seperti \n  # crlf : dipakai di windows

# string lateral atau raw
print(10*"=")
print('a:\new folde') # \n akan dibaca sebagai perintah bukan string
# menggunakan raw string
print(r'a:\new folder') # \n akan dibaca sebagai string
print(r'a:\n\t\n\bew folder') # \n akan tetap dibaca sebagai string
# multipleline literal string
print("""
nama \t: ucup
kelas \t: 2      
""")
# gabungan multiple lateral string dan raw
print(r"""
nama \t: ucup # \t akan dibaca sebagai string
kelas \t: 2      
""")

# operasi dan manipulasi string
''' operasi dan manipulasi string'''
nama_depan = "fadil"
nama_tengah = "saadi" 
nama_belakang = "zahid"

nama_lengkap = nama_depan + nama_tengah + nama_belakang
print(nama_lengkap)
nama_lengkap = nama_depan +" "+ nama_tengah +" "+ nama_belakang
print(nama_lengkap)  # untuk  memberi spasi atau karakter lain 

# menghitung panjang string
panjang = len(nama_lengkap)
#print("pangjang" + nama_lengkap +"adalah :"+ panjang) # akan masalah karena tipe int harus menggunakan (,) atau
print("pangjang" + nama_lengkap +"adalah :"+ str(panjang)) #diubah menjadi string

# operator string

# mengecek apakah ada karakter atau string di dalam string
d = "d"
status = d in nama_lengkap # d didalam nama lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))
D = "D"
status = D in nama_lengkap # D didalam nama lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status))
D = "D"
status = D not in nama_lengkap # D tidak ada didalam nama lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print(8*"=") # menaruh kali di depan atau dibelakang sama saja

# indexing
 # ketika panjang tadi di mulai dari 1 makan index dimulai dari 0
print('index ke-1 = '+ nama_lengkap[0]) 
print('index ke-5 = '+ nama_lengkap[5]) 
print('index ke-(-3) = '+ nama_lengkap[-3]) # maka diambil dari belakang
print('index ke-(-2) = '+ nama_lengkap[-2]) # maka diambil adri belakang
print('index ke-[0-4] = '+ nama_lengkap[0:4]) # : artinya sampai # 0 : 4 artinya sebelum 4
print('index ke-1,4,7,10,13,16 = '+ nama_lengkap[0:17:3]) # 3 artinya melompat 3 kali

# ascii code (kamus rahasia komputer)
 # kamus yang mengubah angka huruf, angka, dan simbol yang kita ketahui menjadi angka

# item paling kecil (di nama_lengkap)
print('item terkecil : '+ min(nama_lengkap))
# item paling besar (di nama_lengkap)
print('item terbesar : '+ max(nama_lengkap))

kamus_rahasia = ord(" ")
print("assci code dari spasi = "+ str(kamus_rahasia))
kamus_rahasia = ord("a")
print("assci code dari a = "+ str(kamus_rahasia))

# 4. operasi dalam bentuk method
nama = "iin sarimin"
jumlah = nama.count("i")
print("jumalah i pada "+ nama +"adalah : "+ str(jumlah))

nama = "iin sarimin"
jumlah = nama.count("a")
print("jumalah a pada "+ nama +"adalah : "+ str(jumlah))


'''HARI 8'''

# pengenalan string part 2
''' PENGENALAN STRING PART 2 '''

# operator dalam bentuk methods

# mengubah case dari string
 ## merubah semua ke upper case(HURUF BESAR) dan lower case(huruf kecil) 
nama = "ujang"
print('normal = '+ nama)
print('upper = '+ nama.upper()) # hasil : UJANG
print('upper = '+ nama.lower()) # hasil : ujang

# pengecekan dengan isX methods
  # capitalize() | Mengubah huruf pertama menjadi huruf besar
  # casefold() | Mengubah string menjadi huruf kecil semua
  # center() | Mengembalikan string yang diposisikan di tengah
  # count() | Mengembalikan jumlah kemunculan nilai tertentu dalam string
  # encode() | Mengembalikan versi encoded dari string
  # endswith() | Mengembalikan True jika string diakhiri dengan nilai tertentu
  # expandtabs() | Mengatur ukuran tab dalam string
  # find() | Mencari nilai tertentu dalam string dan mengembalikan posisi kemunculannya
  # format() | Memformat nilai-nilai ke dalam string
  # format_map() | Memformat nilai-nilai yang ditentukan ke dalam string
  # index() | Mencari nilai dalam string dan mengembalikan posisi kemunculannya
  # isalnum() | Mengembalikan True jika semua karakter dalam string adalah alfanumerik
  # isalpha() | Mengembalikan True jika semua karakter dalam string adalah huruf
  # isdecimal() | Mengembalikan True jika semua karakter dalam string adalah desimal
  # isdigit() | Mengembalikan True jika semua karakter dalam string adalah digit
  # isidentifier() | Mengembalikan True jika string merupakan identifier yang valid
  # islower() | Mengembalikan True jika semua huruf dalam string adalah huruf kecil
  # isnumeric() | Mengembalikan True jika semua karakter dalam string adalah angka
  # isprintable() | Mengembalikan True jika semua karakter dalam string dapat dicetak
  # isspace() | Mengembalikan True jika semua karakter dalam string adalah spasi
  # istitle() | Mengembalikan True jika string mengikuti format title (huruf kapital di awal kata)
  # isupper() | Mengembalikan True jika semua huruf dalam string adalah huruf besar
  # join() | Menggabungkan elemen-elemen dari iterable ke akhir string
  # ljust() | Mengembalikan versi string yang diratakan ke kiri
 
## islower/isupper
kita = "bersama"
print('kita = '+ kita) # hasil akan bool maka harus di rubah ke str
print('kita apakah besar = '+str(kita.islower()))
print('kita apakah besar = '+str(kita.isupper()))
print('"JAMBU ALAS" apakah besar = '+str("JAMBU ALAS".isupper()))
## istitle()
print("kita Pasti Bisa istitle = " + str("Kita Pasti Bisa".istitle()))

# mengecek komponen startswith() endswith()
cek_awal = "Kita Pasti Bisa".startswith("Kita") 
print('start = '+ str(cek_awal))
cek_akhir = "Kita Pasti Bisa".endswith("Bisa")
print('akhiran = '+ str(cek_akhir))

## penggabungan komponen join() split()
pisah = ["aku","pasti","bisa"]
gabung = " ".join(pisah) # " " komponen penggabung dan (tempat nilainya)
print(pisah)
print(gabung)
pecah = gabung.split(" ") # (" ") komponen yang akan dihapus  
print(pisah)              # dan akan kembali kebentuk awal
print(pecah)              # kebalikan dari join yaitu tempat nilainya di depan dan yang akan dihapus di belakang

## alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(20) # (20) adalah rentang yang akan digunakan
print("|"+kanan+"|")
print("|"+"kiri".ljust(20)+"|")
print("|"+"tengah".center(20)+"|")
print("|"+"tengah".center(20,"=")+"|") # ("=") adalah komponen yang akan mengisi tempat kosong

# kebalikannya --> strip()
tengah = "tengah".center(20,"=")
print("|"+tengah+"|")
tengah = "tengah".strip("=") # menghilangkan tanda ("=")
print("|"+tengah+"|")


'''HARI 9'''

# format string
''' FORMAT STRING '''

# contoh generic

# string
nama = "fadhil"
#format_str = f"hallo {nama}"
print(f"hallo {nama}")
# boolean
boolean = False
print(f"boolean = {boolean}")
# angka
angka = 750.35
print(f"angka = {angka}")
## angka bilangan bulat
bulat = 7
print(f"bilangan bulat = {bulat:d}") # :d digunakan untuk belangan bulat/int jika mengguanakn float akan eror 

# bilangan ordo ribuan
mahal  = 1000000
print(f"mahal = {mahal:,}") # menggunakn , untuk menempatkan koma di ribuan
# bilangan desimal
desimal = 234.4567
print(f"desimal = {desimal:.2f}") 

# menampilkan leading zero
jumlah = 300.205
print(f"berjumlah = {jumlah:08.2f}") # 0(pengisi tempat kosong),8(jumlah karakter/tempat),.(lihat setelah),2(mengabil 2 setelah .),f(tipe)

# menampilkan tanda +/-
plus = 20.2
mins = -10.33330
print(f"plus = {plus:+.1f}") # + jika ingin menampilkan +
print(f"minus = {mins:.2f}")

# menformat persen
kemungkinan = 0.034
print(f"berkemungkinan = {kemungkinan:.1%}") # 1 digunakan agar angka yang muncul di belakang koma hanya 1

# melakukan operasi aritmatika di format
diskon = 100000
harga = 750000
jumlah = 4
print(f"total belanja = Rp.{(harga-diskon)*jumlah:,}")

# format angka lain(binary, octal , hexadecimal) --> belum dibahas lengkap hanya pengantar
angka = 50
print(f"binary = {bin(angka)}")
print(f"octal = {oct(angka)}") 
print(f"hexadecimal = {hex(angka)}")
# atau
angka = 255
print(f"Desimal: {angka}")
print(f"Biner  : {angka:b}") # b untuk binary
print(f"Oktal  : {angka:o}") # o untuk octal
print(f"Hexa   : {angka:x}") # x untuk hex (kecil)
print(f"HEXA   : {angka:X}") # X untuk HEX (KAPITAL)

'''HARI 10'''

# width dan multilane
''' WIDTH DAN MULTILINE'''

# data 
d_nama = "parno"
d_umur = 33
d_tinggi = 163.5
d_ukuran_sepatu = 41

# string biasa
data_diri = f"nama = {d_nama}, umur = {d_umur}, tinggi = {d_tinggi}, sepatu = {d_ukuran_sepatu}"
print(8*"="+"STR"+8*"=")
print(data_diri)
# data string mmultiline (menggunakan enter, newline, \n)
data_diri = f"\nnama \t= {d_nama} \numur \t= {d_umur} \ntinggi \t= {d_tinggi} \nsepatu \t= {d_ukuran_sepatu}"
print(8*"="+"STR"+8*"=")
print(data_diri)
# string multi line (tiga petik)
data = f"""
nama = {d_nama}
umur = {d_umur}  
""" # akan ditampilkan sesuai tempatnya
print(8*"="+"STR"+8*"=")
print(data)
# string multi line (tiga petik)
## mengatur lebar tempat karakter
data = f"""
nama = {d_nama:>10} 
umur = {d_umur:>8}  
""" # akan ditampilkan sesuai tempatnya
    #:>5 (menggeser str ke kanan dan berjumlah total 5 karakter)
    # jika karakter memiliki lebih dari yang diminta misal (suprapti) :>5 maka tidak akan terjadi apa apa dan akan tetap di tulis sama
print(8*"="+"STR"+8*"=")
print(data)