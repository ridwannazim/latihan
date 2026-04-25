'''hari 4'''
#konversi satuan suhu
'''latihan konversi satuan temperatur'''
#mengkonversi satuan suhu ke satuan suhu yang lain

#celcius
'''celcius'''
celcius = float(input('masukan celcius :'))
print('suhu :',celcius,'C')
#reamur
reamur = (4/5)*celcius
print('reamur :',reamur,'RE')
#fahrenheit
fahrenheit = ((9/5)*celcius)+32
print('fahrenheit :',fahrenheit,'F')
#kelvin
kelvin = celcius + 273
print('kelvin :',kelvin,'K')

#reamur
'''reamur'''
reamur = float(input('masukan reamur :'))
print('suhu :',reamur,'RE')
#celcius
celcius = (5/4)*reamur
print('celcius :',celcius,'C')
#fahrenheit
fahrenheit = ((9/4)*reamur)+32
print('fahrenheit :',fahrenheit,'F')
#kelvin
kelvin = ((5/4)*reamur)+273
print('kelvin :',kelvin,'K')

#fahrenheit
'''fahrenheit'''
fahrenheit = float(input('masukan fahrenheit :'))
print('suhu :',fahrenheit,'F')
#celcius
celcius = 5/9*(fahrenheit-32)
print('celcius :',celcius,'C')
#reamur
remaur = 4/9*(fahrenheit-32)
print('fahrenheit :',fahrenheit,'F')
#kelvin
kelvin = ((5/9*(fahrenheit-32))+273)  #PR 
print('kelvin :',kelvin,'K')

#kelvin
'''kelvin'''
kelvin = float(input('masukan kelvin :'))
print('suhu :',kelvin,'K')
#celcius
celcius = kelvin-273
print('celcius :',celcius,'C')
#reamur
reamur = 4/5*(kelvin-273)
print('reamur :',reamur,'RE')
#fahrenheit
fahrenheit = (9/5*(kelvin-273))+32    #PR
print('fahrenheit :',fahrenheit,'F')