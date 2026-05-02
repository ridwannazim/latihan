 
import datetime as dt
import os
import time
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

def tanya(pesan):
    while True:
        jawab = input(pesan + " (y/n) = ").lower().strip()
        if jawab in ["y", "n"]:
            return jawab == "y"
        else:
            print("input salah!!") 
        
def history():
    '''fitur menu riwayat pinjaman'''
    while True:
        os.system("cls")
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

        if not tanya("lihat lagi?"):
            break

def tambah_barang():
    '''fitur sub menu tambah barang'''
    while True:
        os.system("cls")
        print("="*25)
        print(f"{'TAMBAH BARANG':^25}")
        print("="*25,"\n")
        tambah_kategori = input(f"{'kategori':<15}= ").title()
        tambah_buku = input(f"{'judul buku':<15}= ").title()
        jumlah_buku = input(f"{'masukan jumlah':<15}= ")
        if not jumlah_buku.isnumeric():
            print("error")
            time.sleep(1)
            continue
        jumlah_buku=int(jumlah_buku)
        if tambah_kategori in gudang_ and tambah_buku in gudang_[tambah_kategori]:
            gudang_[tambah_kategori][tambah_buku] += jumlah_buku
        elif tambah_kategori in gudang_ and not tambah_buku in gudang_[tambah_kategori]:
            gudang_[tambah_kategori][tambah_buku] = jumlah_buku
        elif tambah_kategori not in gudang_:
            gudang_[tambah_kategori] = {}
            gudang_[tambah_kategori][tambah_buku] = jumlah_buku
            print("="*25)
        if not tanya("\ntambah lagi?"):
            break

def cek_stok():
    '''fitur sub menu tambah barang'''
    while True:
        os.system("cls")
        print("="*25)
        print(f"{'STOK SAAT INI':^25}")
        print("="*25)
        no=1
        for kategori,isi in gudang_.items():
            print(f"{no}. kategori = {kategori.upper()}")
            no+=1
            nosub=1     
            for judul,stok in isi.items():
                print(f"  {nosub}. judul \t= {judul:20} stok = {stok}")
                nosub+=1
        print("="*25)
        if tanya("keluar?"):
            break

def cek_gudang():
    '''fitur menu cek gudang'''
    while True:
        os.system("cls")
        print("="*25)
        print(F"{'CEK GUDANG':^25}")
        print("="*25)
        menu_cek_gudang = input("\t1.cek stok \n\t2.tambah barang \n\t3.keluar  \n\npilihan = ")
        if menu_cek_gudang not in ["1","2","3"]:
            print("maaf input salah, mohon ulangi")
            time.sleep(1)
            continue
        elif menu_cek_gudang == "1":
            cek_stok()
        elif menu_cek_gudang == "2":
            tambah_barang()
        elif menu_cek_gudang == "3":
            break

def pinjam_buku():
    '''fitur menu pinjam buku'''
    while True:
        os.system("cls")
        print("="*25)
        print(f"{'PINJAM BUKU':^25}")
        print("="*25)
        print("\nketik (k) untuk keluar")
        input_kategori = input(f"  {'kategori buku':<15}= ").title()
        if input_kategori == "K":
            break
        elif input_kategori not in gudang_:
            print("maaf kategori tidak ditemukan")
            time.sleep(1)
            continue
        input_judul = input(f"  {'judul buku':<15}= ").title()
        if input_judul not in gudang_[input_kategori] :
            print("maaf barang tidak tersedia")
            time.sleep(1)
            continue
        jumlah_pinjaman = input(f"  {'jumlah':<15}= ")
        if not jumlah_pinjaman.isnumeric():
            print("silakan isi dengan benar")
            time.sleep(1)
            continue
        jumlah_pinjaman = int(jumlah_pinjaman)
        if jumlah_pinjaman > gudang_[input_kategori][input_judul]:
            print(f"maaf jumlah stok tidak memadai. stok saat ini = {gudang_[input_kategori][input_judul]} ")
            time.sleep(1)
            continue   

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
        print("\ndata berhasil disimpan. semangat membaca.")
        print("="*25)
        if not tanya("pinjam lagi?"):
            break


# awal program
while True:
    os.system("cls")
    print("="*25)
    print(f"{'SELAMAT DATANG':^25}")
    print(F"{'PERPUSTAKAAN CENDIKIA':^25}")
    print("="*25)
    print("\t1.pinjam buku \n\t2.cek gudang \n\t3.riwayat pinjaman \n\t4.keluar")
    print("="*25)
    menu_utama = input("pilihanmu = ").strip()
    if menu_utama not in ["1","2","3","4"]:
        print("pilihan tidak tersedia! mohon ulangi!")
        time.sleep(1)
        continue

    elif menu_utama == "4":
        break
    elif menu_utama == "1":
        pinjam_buku() 
    elif menu_utama == "2":
        cek_gudang()
    elif menu_utama == "3":
        history()
# akhir program