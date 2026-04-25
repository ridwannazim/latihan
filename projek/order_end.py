# membuat sistem 
# HARI 18
# kualitas bahan dus kotak
## dus kotak A
dus_a = 100 
harga_dus_a = 3000
## dus kotak B
dus_b = 100
harga_dus_b = 2000


# kualitas bahan kalender
## kalender A
kalender_a = 100
harga_kal_a = 120000
## kalender B
kalender_b = 100
harga_kal_b = 100000

while True:
    print("="*15)
    order = input("melayani pembuatan dus kotak dan kalender \napa yang ingin kamu buat = " ).strip().lower()
    if order not in ["kalender","duskotak","dus kotak"]:
        print("mohon ulangi dengan benar")
        continue
    if order == "kalender":
        while True:
            print("="*15)
            print("kualitas bahan")
            bahan = input("\nkualitas A \nkualitas B \n\ncek bahan (A/B) atau pesan (p) = ").lower().strip()
            if bahan not in ["a","b","p"]:
                print("mohon ulangi dengan benar")
                continue
            elif bahan == "a":
                while True:
                    print("="*15)
                    print(f"stok bahan \t= {kalender_a} \nharga satuan \t= Rp{harga_kal_a:,} ")
                    keluar = input("\ningin kembali (y/n) = ").lower().strip()
                    if keluar == "y":
                        break
                    elif keluar == "n":
                        print("silahkan cek lagi")
                        continue
                    else:
                        print("mohon isi dengan benar")
                        continue
    
            elif bahan == "b":
                while True:
                    print("="*15)
                    print(f"stok bahan \t= {kalender_b} \nharga satuan \t= Rp{harga_kal_b:,} ")
                    keluar = input("\ningin kembali (y/n) = ").lower().strip()
                    if keluar == "y":
                        break
                    elif keluar == "n":
                        print("silahkan cek lagi")
                        continue
                    else:
                        print("mohon isi dengan benar")
                        continue
            
            elif bahan == "p":
                break

        while True:
            print("kalender".center(20,"=")) 
            pesanan = input("masukan nominal pesanan = ").strip().lower()
            kualitas = input("kualitas bahan (A/B) = ").strip().lower()
            if not pesanan.isnumeric():
                print("mohon isi dengan benar")
                continue
            
            pesanan = float(pesanan)
            pengecekan_stok = (pesanan * 10)

            if kualitas == "a":
                print(f"Total harga: Rp{harga_kal_a*pesanan:,}")
                print(f"stok bahan A kurang: {kalender_a}")
                if float(pengecekan_stok) <= float(kalender_a):
                    kalender_a -= pengecekan_stok 
                    print("="*15)
                    print(f"total pesanan \t= {pesanan} \ntotal harga \t= Rp{harga_kal_a*pesanan:,} \nkualitas bahan \t= A")
                elif float(pengecekan_stok) >= float(kalender_a) :
                    print("mohon maaf bahan tidak mencukupi")
                    continue

            elif kualitas == "b":
                print(f"Total harga: Rp{harga_kal_b*pesanan:,}")
                print(f"stok bahan B kurang: {kalender_b}")
                if float(pengecekan_stok) <= float(kalender_b):
                    kalender_b -= pengecekan_stok 
                    print("="*15)
                    print(f"total pesanan \t= {pesanan} \ntotal harga \t= Rp{harga_kal_b*pesanan:,} \nkualitas bahan \t= B ")
                elif float(pengecekan_stok) >= float(kalender_b) :
                    print("mohon maaf bahan tidak mencukupi")
                    continue
            
            elif kualitas not in ["a","b"]:
                print("mohon isi dengan benar")
                continue

            while True:
                keluar = input("terimakasi telah order \ningin order lagi (y/n) = ").lower().strip()
                if keluar == "n":
                    print("terimakasih")
                    exit()
                elif keluar == "y":
                    break
                elif keluar not in ["y","n"]:
                    print("mohon isi dengan benar")
                    continue


    if order in ["dus kotak","duskotak"]:
        while True:
            print("="*15)
            print("kualitas bahan")
            bahan = input("\nkualitas A \nkualitas B \n\ncek bahan (A/B) atau pesan (p) = ").lower().strip()
            if bahan not in ["a","b","p"]:
                print("mohon ulangi dengan benar")
                continue
            elif bahan == "a":
                while True:
                    print("="*15)
                    print(f"stok bahan \t= {dus_a} \nharga satuan \t= Rp{harga_dus_a:,} ")
                    keluar = input("\ningin kembali (y/n) = ").lower().strip()
                    if keluar == "y":
                        break
                    elif keluar == "n":
                        print("silahkan cek lagi")
                        continue
                    else:
                        print("mohon isi dengan benar")
                        continue
    
            elif bahan == "b":
                while True:
                    print("="*15)
                    print(f"stok bahan \t= {dus_b} \nharga satuan \t= Rp{harga_dus_b:,} ")
                    keluar = input("\ningin kembali (y/n) = ").lower().strip()
                    if keluar == "y":
                        break
                    elif keluar == "n":
                        print("silahkan cek lagi")
                        continue
                    else:
                        print("mohon isi dengan benar")
                        continue
            
            elif bahan == "p":
                break

        while True:
            print("dus kotak".center(20,"=")) 
            pesanan = input("masukan nominal pesanan = ").strip().lower()
            kualitas = input("kualitas bahan (A/B) = ").strip().lower()
            if not pesanan.isnumeric():
                print("mohon isi dengan benar")
                continue
            
            pesanan = float(pesanan)
            pengecekan_stok = (pesanan * 4)

            if kualitas == "a":
                print(f"Total harga: Rp{harga_dus_a*pesanan:,}")
                print(f"stok bahan A kurang: {dus_a}")
                if float(pengecekan_stok) <= float(dus_a):
                    dus_a -= pengecekan_stok 
                    print("="*15)
                    print(f"total pesanan \t= {pesanan} \ntotal harga \t= Rp{harga_dus_a*pesanan:,} \nkualitas bahan \t= A")
                elif float(pengecekan_stok) >= float(dus_a) :
                    print("mohon maaf bahan tidak mencukupi")
                    continue

            elif kualitas == "b":
                print(f"Total harga: Rp{harga_dus_b*pesanan:,}")
                print(f"stok bahan B kurang: {dus_b}")
                if float(pengecekan_stok) <= float(dus_b):
                    dus_b -= pengecekan_stok 
                    print("="*15)
                    print(f"total pesanan \t= {pesanan} \ntotal harga \t= Rp{harga_dus_b*pesanan:,} \nkualitas bahan \t= B ")
                elif float(pengecekan_stok) >= float(dus_b) :
                    print("mohon maaf bahan tidak mencukupi")
                    continue
            
            elif kualitas not in ["a","b"]:
                print("mohon isi dengan benar")
                continue

            while True:
                keluar = input("terimakasi telah order \ningin order lagi (y/n) = ").lower().strip()
                if keluar == "n":
                    print("terimakasih")
                    exit()
                elif keluar == "y":
                    break
                elif keluar not in ["y","n"]:
                    print("mohon isi dengan benar")
                    continue

''' PROGRAM SELESAI '''