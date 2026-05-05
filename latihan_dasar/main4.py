'''HARI 34'''

# latihan fungsi

import os
def keluar():
    while True:
        pilihan = input("mau lanjut (y/n) =").strip().lower()
        if pilihan == "n" :
            print("Terima kasih sudah menggunakan aplikasi ini!")
            return True
        elif not pilihan in ["y","n"] :
            print("mohon masukan sesaui perintah")
            return False

def header():
    '''header'''
    os.system("cls")
    print(f"{'kalkulator BMI':^30}")
    print("="*30)

def  input_user():
    '''input user'''
    nama = input(F"{'NAMA':<10}=").title()
    while True:
        gender = input("Gender (Pria/Wanita): ").lower().strip()
        if not gender in ["pria","cowok","laki laki","cewek","wanita","perempuan"] :
            print("mohon ulangi")
            continue
        tinggi = (input("Tinggi (cm): "))
        if not tinggi.isnumeric() :
            print("mohon ulangi")
            continue
        berat = (input("Berat (kg): "))
        if not berat.isnumeric() :
            print("mohon ulangi")
            continue

        return nama,gender,tinggi,berat
    
def perhitungan(berat,tinggi,nama):
    '''hitung bmi'''
    bmi = berat / ((tinggi/100)**2)
    return bmi, print(f"\nHalo {nama}, BMI anda: {bmi:.1f}")

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
    if gender in ["pria", "laki laki", "cowok"]:
       keterangan = kategori_l(bmi)
        
    elif gender in ["wanita", "perempuan", "cewek"]:
        keterangan = kategori_p(bmi)
    else:
        keterangan = "Data tidak valid"
        

    print(f"Keterangan: {keterangan}")
    if keluar():
        break

