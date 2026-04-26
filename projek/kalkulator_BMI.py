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