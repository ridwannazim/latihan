# kalkulator

def kalkulator(a,b,op):
    tambah = a+b
    kurang = a-b
    kali = a*b
    bagi = a/b
    pangkat = a**b
    floor = a//b
    modulus = a%b
    return tambah,kurang,kali,bagi,pangkat,floor,modulus
def keluar():
    keluar = input("lanjut ? y/n = ")
    return keluar == "n"
while True:
    print("-"*11)
    print(f"{'kakulator':11}")
    print("-"*11)

    angka1 = input(f"{'masukan angka pertama':23}=")
    if not angka1.isnumeric():
        print("input salah!!")
        continue
    operasi = input(f"{'masukan operasi':23}=")
    if operasi not in ['+','-','*','/','//','**','%']:
        print("input salah!!")
        continue
    angka2 = input(f"{'masukan angka kedua':23}=")
    if not angka2.isnumeric():
        print("input salah!!")
        continue
    elif operasi == "/" and angka2 == "0":
        print("ada kesalahan!! tidak bisa dibagi 0")
        continue
    angka1 = float(angka1)
    angka2 = float(angka2)

    tambah,kurang,kali,bagi,pangkat,floor,modulus = kalkulator(angka1,angka2)

    if operasi == "+":
        print(f"{angka1} + {angka2} = {tambah}")
    elif operasi == "-":
        print(f"{angka1} - {angka2} = {kurang}")
    elif operasi == "*":
        print(f"{angka1} * {angka2} = {kali}")
    elif operasi == "/":
        print(f"{angka1} / {angka2} = {bagi}")
    elif operasi == "**":
        print(f"{angka1} ** {angka2} = {pangkat}")
    elif operasi == "//":
        print(f"{angka1} // {angka2} = {floor}")
    elif operasi == "%":
        print(f"{angka1} % {angka2} = {modulus}")
    if keluar():
        break