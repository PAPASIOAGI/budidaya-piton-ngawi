#mencari total penjualan "susu"😋

#untuk mendapatkan harga penjualan susu
#kita perlu memasukan code susu, code jenis, code ukuran 
#Code; 101=Dancow
     #code jenis ==11 maka Bubuk
        #code Ukuran ==1 maka harga 20000
        #code Ukuran ==2 maka harga 38000
        #code Ukuran ==3 maka harga 56000
    #code jenis ==12 maka cair
        #code Ukuran ==1 maka harga 25000
        #code Ukuran ==2 maka harga 43000
        #code Ukuran ==3 maka harga 61000
#Total pembelian = Jumlah pembelian*harga

#Input
print("Dancow 101")
print("Ultra 102")
print("Bendera 103")
ks=input("Masukan code susu = ")

print("Bubuk 11 ")
print("Cair 12")
js=input("Masukan jenis susu = ")

print("Ukuran tersedia 1, 2, dan 3")
us=input("Masukan ukuran susu = ")

jp=input("Masukan jumlah pembelian = ")

#Conversi
ks = int(ks)
js = int(js)
us = int(us)
jp = int(jp)

#Process
if ks==101:
    merk="dancow"
    if js==11:
        jenis="bubuk"
    if us==1:
        harga=20000
    elif us==2:
        harga=38000
    else:
        harga=56000
if js==12:
    Jenis="cair"
    if us==1:
        harga=25000
    elif us==2:
        harga=43000
    else:
        haga=61000

if ks==102:
    merk="Ultra"
    if js==11:
        jenis="bubuk"
        if us==1:
            harga=18000
        elif us==2:
            harga=27000
        else:
            harga=40000
    if js==12:
        jenis="cair"
        if us==1:
            harga=20000
        elif us==2:
            harga=31000
        else:
            harga=48000

if ks==103:
    merk="Bendera"
    if js==11:
        jenis="bubuk"
        if us==1:
            harga=23000
        elif us==2:
            harga=31000
        else:
            harga=45000
    if js==12:
        jenis="cair"
        if us==1:
            harga=22000
        elif us==2:
            harga=34000
        else:
            harga=47000

#OUTPUT
if harga!=1:
    TH=harga*jp
    print("Harga 1 barang = Rp.", harga)
    print("Total harga = Rp.",TH)
else:
    print("Anda memasukan salah dan tidak valid🙏")
    
