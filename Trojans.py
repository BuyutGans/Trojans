import os,random

print('TROJAN\nBY:BuyutGans')

c = input("Masukkan Nomor Target: ")
a = 0
b = 'cp 0 /storage/emulated/0/1'
while True:
     d = str(a+1)
     c = str(a+2)
     b = b.replace(d,c)
     print("Menyerang Nomor",c,'Dengan Trojan Sebanyak',a,'Paket')
     os.system(b)
     a += 1