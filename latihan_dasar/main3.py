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