 
import datetime as dt

# daftar gudang
gudang_={
    'Mata Pelajaran':{
        'Pkn':10,
        'Seni':8
    },
    'Novel':{
        'Sisa Kata':8,
        'Ujung Doa':12
    },
    'Dongeng':{
        'Si Kancil':8,
        'Roro Jonggrang':5
    }
}
# daftar pinjam
pinjam = {}

# awal program
while True:
    print("="*25)
    print("selamat datang".center(25,"="))
    print("PERPUSTAKAAN CENDIKIA".center(25,"="))
    print("="*25)
    print("\t1.pinjam buku \n\t2.cek gudang \n\t3.riwayat pinjaman \n\t4.keluar")
    menu_utama = input("pilihanmu = ").strip()
    if menu_utama not in ["1","2","3","4"]:
        print("pilihan tidak tersedia! mohon ulangi!")
        continue

    elif menu_utama == "4":
        break

    elif menu_utama == "1":
        while True:
            print("\n")
            print("PINJAM BUKU".center(25,"="))
            print("ketik (k) untuk keluar")
            input_kategori = input(f"{"kategori buku":<15}= ").title()
            if input_kategori == "K":
                break
            elif input_kategori not in gudang_:
                print("maaf kategori tidak ditemukan")
                continue
            input_judul = input(f"{"judul buku":<15}= ").title()
            if input_judul not in gudang_[input_kategori] :
                print("maaf barang tidak tersedia")
                continue
            jumlah_pinjaman = input(f"{"jumlah":<15}= ")
            if not jumlah_pinjaman.isnumeric():
                print("silakan isi dengan benar")
                continue
            jumlah_pinjaman = int(jumlah_pinjaman)
            if jumlah_pinjaman > gudang_[input_kategori][input_judul]:
                print(f"maaf jumlah stok tidak memadai. stok saat ini = {gudang_[input_kategori][input_judul]} ")
                continue   
            #elif input_judul in gudang_ and gudang_[input_judul] >= jumlah_pinjaman :
            gudang_[input_kategori][input_judul] -= jumlah_pinjaman
            waktu_sekarang = dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            riwayat_pinjaman = {
                'judul':input_judul,
                'jumlah':jumlah_pinjaman,
                'waktu':waktu_sekarang
                }
            if input_kategori not in pinjam:
                pinjam[input_kategori] = [riwayat_pinjaman]
            elif input_kategori in pinjam :
                pinjam[input_kategori].append(riwayat_pinjaman)
            print("data berhasil disimpan. semangat membaca.")
    
            pinjam_lagi = input("pinjam lagi? (y/n) = ").lower().strip()
            if pinjam_lagi not in ["y","n"]:
                print("maaf ulangi dengan benar")
                continue
            if pinjam_lagi == "y":
                continue
            elif pinjam_lagi == "n":
                break
                
        
    elif menu_utama == "2":
        while True:
            print("\n")
            print("CEK GUDANG".center(25,"="))
            menu_cek_gudang = input("\t1.cek stok \n\t2.tambah barang \n\t3.keluar  \npilihan = ")
            if menu_cek_gudang not in ["1","2","3"]:
                print("maaf input salah, mohon ulangi")
                continue
            elif menu_cek_gudang == "1":
                print("\nstok saat ini")
                no=1
                for kategori,isi in gudang_.items():
                    print(f"{no}. kategori = {kategori.upper()}")
                    no+=1
                    nosub=1     
                    for judul,stok in isi.items():
                        print(f"  {nosub}. judul \t= {judul:20} stok = {stok}")
                        nosub+=1
                while True:
                    keluar_stok = input("keluar (y/n) = ").lower().strip()
                    if keluar_stok not in ["y","n"]:
                        print("maaf ualangi dengan benar")
                        continue
                    if keluar_stok == "n":
                        continue
                    elif keluar_stok == "y":
                        break
                
            elif menu_cek_gudang == "2":
                while True:
                    print("TAMBAH BARANG".center(25,"="))
                    tambah_kategori = input(f"{"kategori":<15}= ").title()
                    tambah_buku = input(f"{"judul buku":<15}= ").title()
                    jumlah_buku = input(f"{"masukan jumlah":<15}= ")
                    if not jumlah_buku.isnumeric():
                        print("error")
                        continue
                    jumlah_buku=int(jumlah_buku)
                    if tambah_kategori in gudang_ and tambah_buku in gudang_[tambah_kategori]:
                        gudang_[tambah_kategori][tambah_buku] += jumlah_buku
                    elif tambah_kategori in gudang_ and not tambah_buku in gudang_[tambah_kategori]:
                       gudang_[tambah_kategori][tambah_buku] = jumlah_buku
                    elif tambah_kategori not in gudang_:
                        gudang_[tambah_kategori] = {}
                        gudang_[tambah_kategori][tambah_buku] = jumlah_buku
                    keluar_input_barang = input("tambah barang lagi? (y/n) = ").lower().strip()
                    if keluar_input_barang not in ["y","n"]:
                        print("error, ulangi")
                        continue
                    elif keluar_input_barang == "n":
                        break
                    elif keluar_input_barang == "y":
                        continue
            elif menu_cek_gudang == "3":
                break

    elif menu_utama == "3":
        print("="*5,"history pinjaman","="*5)
        if not pinjam :
            print("belum ada pinjaman")
        elif pinjam:
            no=1
            for kategori,isi in pinjam.items():
                    print(f"{no}. kategori = {kategori.upper()}")
                    no+=1
                    nosub=1     
                    for riwayat in isi:
                        print(f"  {nosub}. judul = {riwayat['judul']:<20} jumlah = {riwayat['jumlah']:<5} waktu peminjaman = {riwayat['waktu']}")
                        nosub+=1
            
        while True:
            keluar_histori = input("keluar (y/n) = ").lower()
            if keluar_histori not in ["y","n"]:
                print("error, ulangi")
                continue
            elif keluar_histori == "y":
                break
            elif keluar_histori == "n":
                continue