'''HARI 34'''

# latihan fungsi

import os
def keluar():
    while True:
        pilihan = input("mau lanjut (y/n) = ").strip().lower()
        if pilihan in ["y","n"]  :
            print("Terima kasih sudah menggunakan aplikasi ini!")
            return pilihan == "n"
        else:
            print("input salah!!")        

def header():
    '''header'''
    os.system("cls")
    print(f"{'kalkulator BMI':^30}")
    print("="*30)

def  input_user():
    '''input user'''
    while True:
        nama = input(F"| {'NAMA':<13}: ").title()
        gender = input(f"| {'GENDER':<13}: ").lower().replace(" ","")
        if not gender in ["pria","cowok","lakilaki","cewek","wanita","perempuan"] :
            print("mohon ulangi")
            continue
        tinggi = (input(f"| {'TINGGI (cm)':<13}: "))
        if not tinggi.isnumeric() :
            print("mohon ulangi")
            continue
        berat = (input(f"| {'BERAT (kg)':<13}: "))
        if not berat.isnumeric() :
            print("mohon ulangi")
            continue

        return nama,gender,tinggi,berat
    
def perhitungan(berat,tinggi,nama):
    '''hitung bmi'''
    bmi = berat / ((tinggi/100)**2)
    print("="*30)
    return bmi, print(f"Halo {nama}, BMI anda: {bmi:.1f}")

def kategori_l(bmi):
    if bmi < 18.5: keterangan = "Kurus"
    elif bmi <= 22.9: keterangan = "Ideal"
    else: keterangan = "Obesitas"
    return keterangan

def kategori_p(bmi):
    if bmi < 18.5: keterangan = "Kurus"
    elif bmi <= 24.9: keterangan = "Ideal"
    else: keterangan = "Obesitas"
    return keterangan


while True:
    header()
    nama,gender,tinggi,berat = input_user()
    tinggi_float = float(tinggi)
    berat_float = float(berat)
    bmi,tampilan = perhitungan(berat_float,tinggi_float,nama)

    # Menggunakan 'in' agar lebih efisien
    if gender in ["pria", "lakilaki", "cowok"]:
       keterangan = kategori_l(bmi)
        
    elif gender in ["wanita", "perempuan", "cewek"]:
        keterangan = kategori_p(bmi)
    else:
        keterangan = "Data tidak valid"
        

    print(f"Keterangan: {keterangan.upper()}")
    print("="*30)
    if keluar():
        break