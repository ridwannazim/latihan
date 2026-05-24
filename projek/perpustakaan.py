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

def header():
    '''header utama'''
    print("="*25)
    print(f"{'SELAMAT DATANG':^25}")
    print(F"{'PERPUSTAKAAN CENDIKIA':^25}")
    print("="*25)
    print("\t1.pinjam buku \n\t2.cek gudang \n\t3.riwayat pinjaman \n\t4.keluar")
    print("="*25)

def header_fitur(pesan):
    '''header fitur'''
    print("="*25)
    print(f"{pesan:^25}")
    print("="*25)

def tanya(pesan):
    while True:
        jawab = input(pesan + " (y/n) = ").lower().strip()
        if jawab in ["y", "n"]:
            return jawab == "y"
        else:
            print("input salah!!") 
        
'''fitur 1 pinjam buku'''
def input_user_pinjam():
    '''input pinjaman'''
    while True:
        print("\nketik (k) untuk keluar")
        kategori = input(f"  {'kategori buku':<15}= ").title()
        if kategori == "K":
            return None
        elif kategori not in gudang_:
            print("maaf kategori tidak ditemukan")
            time.sleep(1)
            continue
        judul= input(f"  {'judul buku':<15}= ").title()
        if judul not in gudang_[kategori] :
            print("maaf barang tidak tersedia")
            time.sleep(1)
            continue
        jumlah_pinjaman = input(f"  {'jumlah':<15}= ")
        if not jumlah_pinjaman.isnumeric():
            print("silakan isi dengan benar")
            time.sleep(1)
            continue
        jumlah_pinjaman = int(jumlah_pinjaman)  
        if jumlah_pinjaman > gudang_[kategori][judul]:
            print(f"maaf jumlah stok tidak memadai. stok saat ini = {gudang_[kategori][judul]} ")
            time.sleep(1)
            continue   
        return kategori,judul,jumlah_pinjaman

def proses_data_pinjaman(kategori,judul,jumlah):
    '''proses pengolahan data pinjaman'''
    gudang_[kategori][judul] -= jumlah
    waktu_sekarang = dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    riwayat_pinjaman = {
        'judul':judul,
        'jumlah':jumlah,
        'waktu':waktu_sekarang
        }
    
    return riwayat_pinjaman

def menyimpan_riwayat(kategori,riwayat):
    '''data riwayat pinjam'''
    if kategori not in pinjam:
        pinjam[kategori] = [riwayat]
    else :
        pinjam[kategori].append(riwayat)

def pinjam_buku():
    '''fitur menu pinjam buku'''
    while True:
        os.system("cls")
        header_fitur("PINJAM BUKU")
        hasil = input_user_pinjam()
        if hasil is None:
            break
        kategori,judul,jumlah_pinjam = hasil 
        data_pinjam_sementara = proses_data_pinjaman(kategori,judul,jumlah_pinjam)
        menyimpan_riwayat(kategori,data_pinjam_sementara)
        print("\ndata berhasil disimpan. semangat membaca.")
        print("="*25)
        if not tanya("pinjam lagi?"):
            break

'''fitur 2 cek gudang'''
def proses_tambah_barang(kategori,buku,jumlah):
    '''menambahkan barang ke gudang'''
    if kategori in gudang_ and buku in gudang_[kategori]:
        gudang_[kategori][buku] += jumlah
    elif kategori in gudang_ and not buku in gudang_[kategori]:
        gudang_[kategori][buku] = jumlah
    elif kategori not in gudang_:
        gudang_[kategori] = {}
        gudang_[kategori][buku] = jumlah
        
def tambah_barang():
    '''fitur sub menu tambah barang'''
    while True:
        os.system("cls")
        header_fitur("TAMBAH BARANG")
        tambah_kategori = input(f"{'kategori':<15}= ").title()
        tambah_buku = input(f"{'judul buku':<15}= ").title()
        jumlah_buku = input(f"{'masukan jumlah':<15}= ")
        if not jumlah_buku.isnumeric():
            print("error")
            time.sleep(1)
            continue
        jumlah_buku=int(jumlah_buku)
        proses_tambah_barang(tambah_kategori,tambah_buku,jumlah_buku)
        print("="*25)
        if not tanya("\ntambah lagi?"):
            break

def stok_gudang():
    '''menampilkan stok gudang'''
    no=1
    for kategori,isi in gudang_.items():
        print(f"{no}. kategori = {kategori.upper()}")
        no+=1
        nosub=1     
        for judul,stok in isi.items():
            print(f"  {nosub}. judul \t= {judul:20} stok = {stok}")
            nosub+=1

def cek_stok():
    '''fitur sub menu cek stok'''
    while True:
        os.system("cls")
        header_fitur("STOK SAAT INI")
        stok_gudang()
        print("="*25)
        if tanya("keluar?"):
            break

def cek_gudang():
    '''fitur menu cek gudang'''
    while True:
        os.system("cls")
        header_fitur("CEK GUDANG")
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
        
'''fitur 3 riwayat pinjaman'''
def menampilkan_riwayat_pinjaman():
    '''menampilkan data pinjaman'''
    no=1
    for kategori,isi in pinjam.items():
            print(f"{no}. kategori = {kategori.upper()}")
            no+=1
            nosub=1     
            for riwayat in isi:
                print(f"  {nosub}. judul = {riwayat['judul']:<20} jumlah = {riwayat['jumlah']:<5} waktu peminjaman = {riwayat['waktu']}")
                nosub+=1

def riwayat_pinjaman():
    '''fitur menu riwayat pinjaman'''
    while True:
        os.system("cls")
        header_fitur("HISTORY PINJAMAN")
        if not pinjam :
            print("belum ada pinjaman")
        elif pinjam:
            print("="*87)
            menampilkan_riwayat_pinjaman()
            print("="*87)
        if not tanya("lihat lagi?"):
            break
        


def main():
    while True:
        os.system("cls")
        header()
        menu_utama = input("pilihanmu = ").strip()
        if menu_utama not in ["1","2","3","4"]:
            print("pilihan tidak tersedia! mohon ulangi!")
            time.sleep(1)
            continue

        if menu_utama == "4":
            break
        elif menu_utama == "1":
            pinjam_buku() 
        elif menu_utama == "2":
            cek_gudang()
        elif menu_utama == "3":
            riwayat_pinjaman()

main()