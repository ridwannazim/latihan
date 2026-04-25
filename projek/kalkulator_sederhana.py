'''hari 12'''
# kalkulator sederhana

while True:
    print('='*10)
    angka1 = (input("masukan angka pertama = "))
    if not angka1.isnumeric():
        print("salah!! ulangi input")
        continue
    operasi = input("masukan operasi = ")
    if operasi not in ["+","-","*","//","/","**","%"]:
        print("salah!! ulangi input")
        continue
    angka2 = (input("masukan angka kedua = "))
    if not angka2.isnumeric():
        print("salah!! ulangi input")
        continue

    angka1_1 = float(angka1)
    angka2_2 = float(angka2)
    if operasi== "+" :
        print(f"{angka1_1} + {angka2_2} = {angka1_1 + angka2_2}")
    elif operasi== "-" :
        print(f"{angka1_1} - {angka2_2} = {angka1_1 - angka2_2}")
    elif operasi== "*" :
        print(f"{angka1_1} * {angka2_2} = {angka1_1 * angka2_2}")
    elif operasi== "/" :
        if angka2_2 ==0 : # dalam matematika tidak boleh dibagi dengan angka nol
            print("gabisa dibagi nol nih boss")
        else:
            print(f"{angka1_1} / {angka2_2} = {angka1_1 / angka2_2}")
    elif operasi== "**" :
        print(f"{angka1_1} ** {angka2_2} = {angka1_1 ** angka2_2}")
    elif operasi== "//" :
        print(f"{angka1_1} // {angka2_2} = {angka1_1 // angka2_2}")
    elif operasi== "%" :
        print(f"{angka1_1} % {angka2_2} = {angka1_1 % angka2_2}")
    else:
        print("error boosss!!!")
    
    while True :
        pilihan = input("mau lanjut y/n = ").strip().lower()
        if pilihan == "y":
            print("="*10)
            break # untuk menghentikan while ke dua
        elif pilihan == "n":
            print("terimakasih")
            exit()
        else :
            print("kesalahan input")