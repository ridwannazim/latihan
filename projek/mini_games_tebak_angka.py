'''HARI 15'''

# percobaan menebak angka menggunakan while

angka_rhs = 6
percobaan = 0
while  True :
    print("tebak angka 1-20")
    angka = int(input("masukan angkamu ="))
    percobaan += 1

    if angka == angka_rhs :
        print(f"selamat tebakanmu benar dalam {percobaan} percobaan")
        break
    elif angka > angka_rhs:
        print("uppss kelewatan ")
    elif angka < angka_rhs :
        print("sedikit lagi")