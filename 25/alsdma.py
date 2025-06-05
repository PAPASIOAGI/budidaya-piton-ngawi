# pak hadi nak jual tanah
# ukuran tanah adalah PANJANG 500 m x Lebar 300 m
# Harga Rp100000/meter





panjang = 500      
lebar = 300        
harga_per_meter = 100000  

print ("Panjang =", panjang, "Meter")
print ("Lebar =", lebar, "Meter")
print ("Harga per meter =", harga_per_meter, "Rupiah")

print("apakah kamu ingin mengetahui total ukuran tanah dan harga dari tanah tersebur?")
if input("Ketik 'y' untuk melanjutkan: ").lower() != 'y':
    print("Terima kasih telah menggunakan program ini.")
    exit()


luas = panjang * lebar
total_harga = luas * harga_per_meter

print(f"Luas tanah: {luas} m2")
print(f"Total harga: Rp{total_harga:,}")