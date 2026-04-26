'''hari 13 - hari 15'''

# DIBAWAH INI MERUPAKAN PROYEK YANG KUKERJAKAN DI HARI KE 13 
# DILANJUT HARI KE 14 DENGAN PENAMBAHAN FOR LOOP (HARI KE14 MERUPAKAN MATERI FOR LOOP)
# DILANJUT HARI KE 15 PERBAIKAN DAN PENGEFISIENSI CODE DAN PENAMBAHAN WHILE 

# HARI KE 13 DAN 14 V
# for kal_bmi in range(3) :
#     nama = input("masukan nama = ")
#     gender = input("masukan jenis kelamin = ")
#     tinggi = float(input(f"masukan tinggi badan (cm) = "))
#     berat = float(input(f"masukan berat badan (kg) = "))

#     if gender=="laki laki" or gender=="pria" or gender=="cowok":
#         tinggi2 = tinggi / 100
#         bmi = berat / (tinggi2 * tinggi2)
#         if bmi < 18.5 :
#             print(f"BMI = {bmi:.1f}")
#             print("berat badan kamu kurang/kurus")
#         elif (18.5 <= bmi <= 22.9) :
#             print(f"BMI = {bmi:.1f}")
#             print("berat badan kamu ideal")
#         elif (23 <= bmi <= 29.9) :
#             print(f"BMI = {bmi:.1f}")
#             print("berat badan kamu berlebih")
#         elif bmi >= 30.0 :
#             print(f"BMI = {bmi:.1f}")
#             print("berat badan kamu tergolong obesitas")
#     elif gender=="perempuan" or gender=="wanita" or gender=="cewek":
#         tinggi2 = tinggi / 100
#         bmi = berat / (tinggi2 * tinggi2)
#         if bmi < 18.5 :
#             print(f"BMI = {bmi:.1f}")
#             print("berat badan kamu kurang/kurus")
#         elif (18.5 <= bmi <= 22.9) :
#             print(f"BMI = {bmi:.1f}")
#             print("berat badan kamu ideal")
#         elif (23 <= bmi <= 24.9) :
#             print(f"BMI = {bmi:.1f}")
#             print("berat badan kamu berlebih")
#         elif bmi >= 25.0 :
#             print(f"BMI = {bmi:.1f}")
#             print("kamu tergolong obesitas")
#     else:
#         print("error")
#         print("mohon isi  dengan benar")

#     print("="*30)

# HARI 15: Perbaikan Logika BMI & String Method
def keluar():
    while True:
        pilihan = input("mau lanjut (y/n) =").strip().lower()
        if pilihan == "n" :
            print("Terima kasih sudah menggunakan aplikasi ini!")
            return True
        elif not pilihan in ["y","n"] :
            print("mohon masukan sesaui perintah")
            return False

while True: # Program berjalan terus sampai disuruh berhenti
    print("\n" + "="*30)
    nama = input("Nama: ").strip() # Nama otomatis rapi (Andi Ganteng)
    if nama.lower() == "selesai" :
        print("Terima kasih sudah menggunakan aplikasi ini!")
        break

    nama_input = nama.title()

    # Input dibersihkan dulu (lowercase dan hapus spasi)
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

    tinggi_float = float(tinggi)
    berat_float = float(berat)

    bmi = berat_float / ((tinggi_float/100)**2)
    print(f"\nHalo {nama_input}, BMI anda: {bmi:.1f}")

    # Menggunakan 'in' agar lebih efisien
    if gender in ["pria", "laki laki", "cowok"]:
        # Logika kategori pria
        if bmi < 18.5: keterangan = "Kurus"
        elif bmi <= 22.9: keterangan = "Ideal"
        else: keterangan = "Obesitas"
        
    elif gender in ["wanita", "perempuan", "cewek"]:
        # Logika kategori wanita
        if bmi < 18.5: keterangan = "Kurus"
        elif bmi <= 24.9: keterangan = "Ideal"
        else: keterangan = "Obesitas"
    else:
        keterangan = "Data tidak valid"
        

    print(f"Keterangan: {keterangan}")
    if keluar():
        break