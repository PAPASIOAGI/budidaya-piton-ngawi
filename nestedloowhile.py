i=int(input("Tuliskan sebuah angka sigma "))

brs=0
klm=0

while brs<=i:
    while klm<brs: 
        print(brs, end=" ")
        klm=klm+1
    klm=0
    print("\n")
    brs=brs+1