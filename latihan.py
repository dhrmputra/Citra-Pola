print("hello world")

x = 5
y = 6
hasil = x + y
print("hasil dari operasi adalah" , hasil)

z = 6.5
w = "bahasa ular"
coba = z + x
print(coba)

trueOrFalse = True
print(trueOrFalse)

ar=['blue','green','red']
print(ar[0])

dic={'nama buah':'durian',
     'nama ilmiah':'Didog',
     'asal':'Indonesia',
     'persebaran':'Asia Tenggara'
}
print(dic['nama buah'])

if 5>2:
    print('lima lebih dari dua loh')

x=4
y=(8-x)
if x == y:
    print("x dan y sama")
else:
    print("x dan y beda")

def ini_fungsi(siapaNamanya):
    print(siapaNamanya + "belajar bahasa Ular")

ini_fungsi("Nyoman Didog")

ini_fungsi("Made Brado")

ini_fungsi("semua orang")

import cv2
import datetime as dt

x = dt.datetime.now()
print(x)

from datetime import date
hariini = date.today()
print("Hari ini tanggal" .hariini)