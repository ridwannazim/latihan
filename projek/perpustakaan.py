# HARI 22
# kembali setalah hampir 2 minggu 

import datetime as dt

# daftar gudang
gudang_={
    'pkn':10,
    'seni':8
}
# daftar pinjam
pinjam = []

# awal program
while True:
    print("="*25)
    print("selamat datang".center(25,"="))
    print("PERPUSTAKAAN CENDIKIA".center(25,"="))
    print("="*25)
    print("\t1.pinjam buku \n\t2.cek gudang \n\t3.riwayat pinjaman \n\t4.keluar")
    user = input("pilihanmu = ").strip()
    if user not in ["1","2","3","4"]:
        print("pilihan tidak tersedia! mohon ulangi!")
        continue

    elif user == "4":
        break

    elif user == "1":
        while True:
            print("\n")
            print("PINJAM BUKU".center(25,"="))
            print("ketik (k) untuk keluar")
            input_judul = input("judul buku = ").lower()
            if input_judul == "k":
                break
            elif input_judul not in gudang_ :
                print("maaf barang tidak tersedia")
                continue
            jumlah_pinjaman = input("jumlah \t= ")
            if not jumlah_pinjaman.isnumeric():
                print("silakan isi dengan benar")
                continue
            jumlah_pinjaman = int(jumlah_pinjaman)
            if jumlah_pinjaman > gudang_[input_judul]:
                print(f"maaf jumlah stok tidak memadai. stok saat ini = {gudang_[input_judul]} ")
                continue   
            #elif input_judul in gudang_ and gudang_[input_judul] >= jumlah_pinjaman :
            gudang_[input_judul] -= jumlah_pinjaman
            waktu_sekarang = dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            riwayat_pinjaman = {
                "buku" : (input_judul),
                "jumlah" : (jumlah_pinjaman),
                "waktu pinjam" : (waktu_sekarang)}
            pinjam.append(riwayat_pinjaman)
            print("data berhasil disimpan. semangat membaca.")
    
            user = input("pinjam lagi? (y/n) = ").lower().strip()
            if user not in ["y","n"]:
                print("maaf ulangi dengan benar")
                continue
            if user == "y":
                continue
            elif user == "n":
                break
                
        
    if user == "2":
        while True:
            print("\n")
            print("CEK GUDANG".center(25,"="))
            pilihan = input("\t1.cek stok \n\t2.tambah barang \n\t3.keluar  \npilihan = ")
            if pilihan not in ["1","2","3"]:
                print("maaf input salah, mohon ulangi")
                continue
            elif pilihan == "1":
                print("\nstok saat ini")
                print(gudang_)
                while True:
                    user = input("keluar (y/n) = ").lower().strip()
                    if user not in ["y","n"]:
                        print("maaf ualangi dengan benar")
                        continue
                    if user == "n":
                        continue
                    elif user == "y":
                        break
                
            elif pilihan == "2":
                while True:
                    print("TAMBAH BARANG".center(25,"="))
                    tambah_buku = input("judul buku = ").title()
                    jumlah_buku = input("masukan jumlah = ")
                    gudang_[tambah_buku] = jumlah_buku
                    if not jumlah_buku.isnumeric():
                        print("error")
                        continue
                    keluar = input("tambah barang lagi? (y/n) = ").lower().strip()
                    if keluar not in ["y","n"]:
                        print("error, ulangi")
                        continue
                    elif keluar == "n":
                        break
                    elif keluar == "y":
                        continue
            elif pilihan == "3":
                break

    elif user == "3":
        print(pinjam)
        while True:
            keluar = input("keluar (y/n) = ").lower()
            if keluar not in ["y","n"]:
                print("error, ulangi")
                continue
            elif keluar == "y":
                break
            elif keluar == "n":
                continue