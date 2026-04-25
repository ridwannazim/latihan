# PROGRAM ABSENSI
# HARI 21

import datetime as dt
# data anggota
anggota = ["Fadil","Ridwan","Alam","Arya","Fahri","Andi","Agus","Herman","Sisil","Kimmy","Bunga","Dewi"]
data_absen = []


# awal program
while True:
    while True:
        print("="*20)
        print("selamat datang".center(20,"="))
        print("C.V ARIFIN OFFSET".center(20))
        print("="*20)
        print("pilihan : \n\t1. ABSEN KEHADIRAN \n\t2. PENGATURAN \n\t3. AKHIRI PROGRAM")
        user = input("masukan pilihan :")
        if not user.isnumeric() and not ["1","2","3"]:
            print("ulangi")
            continue

        if user == "1" :
            while True :
                print("="*20)
                absensi = input("silakan isi nama :").title().strip()
                if absensi in anggota :
                    waktu_sekarang = dt.datetime.now()
                    jam_absen = waktu_sekarang.strftime("%H:%M:%S")
                    print("selamat datang".center(20,"="))
                    log_absen = f"{absensi} waktu masuk {jam_absen} "
                    print(log_absen)
                    data_absen.append(log_absen)
                    while True:
                        utama = input("kembali ke menu utama y/n :").lower().strip()
                        print("="*20)
                        if utama == "y":
                            break
                        elif utama == "n":
                            print("oke baik")
                            continue
                        else :
                            print("data tidak di temukan. ulangi")
                            continue
                    break
                else:
                    print("ulangi ada kesalah")
                    continue
        if user == "2":
            while True:
                print("pengaturan".center(20,"="))
                print("\tA. tambah anggota \n\tB. data anggota \n\tC. cek absen \n\tD. kembali ke menu")
                pilihan_2 = input("masukan pilihan :").capitalize().strip()
                if pilihan_2 not in ["A","B","C","D"] :
                    print("input salah. ulangi")
                    continue     
                elif pilihan_2 == "A":
                        while True:
                            print("tambah anggota".center(20,"="))
                            nama_baru = input("masukan nama anggota : ").title().strip()
                            anggota.append(nama_baru)
                            while True:
                                kembali = input("ingin kembali y/n :").lower().strip()
                                if kembali == "y":
                                    break
                                elif kembali == "n":
                                    print("oke baik")
                                    continue
                                else :
                                    print("input salah mohon ulangi")
                                    continue
                            break
                elif pilihan_2 == "B":
                    print("data anggota".center(20,"="))
                    print(f"jumlah anggota  saat ini {len(anggota)} \n{anggota}")
                    while True:
                        back = input("ingin kembali y/n :").lower().strip()
                        if back == "y":
                            break
                        elif back == "n":
                            print("oke baik")
                            continue
                        else :
                            print("input salah mohon ulangi")
                            continue
                elif pilihan_2 == "C":
                    print("cek absensi".center(20,"="))
                    print(data_absen)
                    while True:
                        back = input("ingin kembali y/n :").lower().strip()
                        if back == "y":
                            break
                        elif back == "n":
                            print("oke baik")
                            continue
                        else :
                            print("input salah mohon ulangi")
                            continue
                elif pilihan_2 == "D":
                    break
        if user == "3":
            print("terimakasih")
            exit()      
# akhir program