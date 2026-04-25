'''hari 11'''
''' DATE AND TIME (LATIHAN)'''
# datetime 
import datetime as dt # mengubah pemanggilan datetime menjadi dt (penamaan alias)

print("isi tanggal lahir\n")
tanggal = int(input("tanggal \t= "))
bulan = int(input("bulan \t\t= "))
tahun = int(input("tahun \t\t= "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir = {tanggal_lahir}")
print(f"kamu lahir hari = {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini = {hari_ini}")

umur_hari = hari_ini - tanggal_lahir
tahun_now = umur_hari.days // 365
bulan_now = (umur_hari.days % 365) // 30
hari_now = (umur_hari.days % 365) % 30
print(f"{tahun_now} tahun, \n{bulan_now} bulan, \n{hari_now} hari")