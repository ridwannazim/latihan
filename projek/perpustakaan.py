# HARI 22
# kembali setalah hampir 2 minggu 

import datetime as dt

# daftar gudang
gudang = ["Pkn","Seni"]
jumlah_g = [4,8]
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
            peminjam = input("judul buku = ").title()
            #dipinjam -= peminjam2
            if peminjam == "K":
                break
            elif peminjam not in gudang :
                print("maaf barang tidak tersedia")
                continue
            peminjam2 = input("jumlah \t= ")
            urutan = gudang.index(peminjam)
            urutan_j = jumlah_g[urutan]
            urutan_j1 = (urutan_j)
            if not peminjam2.isnumeric():
                print("silakan isi dengan benar")
                continue
            elif peminjam not in gudang :
                print("maaf stok tidak tersedia")
                continue
            peminjam2 = int(peminjam2)
            if peminjam2 > urutan_j1:
                print(f"maaf jumlah stok tidak memadai. stok saat ini = {urutan_j1} ")
                continue
            
            elif peminjam in gudang and peminjam2 <= urutan_j1 :
                jumlah_g[urutan] -= peminjam2
                waktu_sekarang = dt.datetime.now()
        
                riwayat_pinjaman = f"| buku = {peminjam} jumalah = {peminjam2} waktu pinjam = {waktu_sekarang} |"
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
            if not pilihan.isnumeric() and not ["1","2","3"]:
                print("maaf input salah, mohon ulangi")
                continue
            elif pilihan == "1":
                print("\nstok saat ini")
                for g,j in zip(gudang,jumlah_g):
                    print(f"\tjudul buku = {g} \tjumlah = {j}") 
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
                    user = input("judul buku = ").title()
                    gudang.append(user)
                    user2 = input("masukan jumlah = ")
                    if not user2.isnumeric():
                        print("error")
                        continue
                    jumlah_g.append(int(user2))
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
            keluar = input("keluar (y/n)")
            if keluar not in ["y","n"]:
                print("error, ulangi")
                continue
            elif keluar == "y":
                break
            elif keluar == "n":
                continue
                
                

