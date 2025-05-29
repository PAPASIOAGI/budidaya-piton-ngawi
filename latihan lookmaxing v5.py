# walas menghitung nilai mapel
# mapelnya adalh fisika dan kimia
# nilai rata-rata  = (fisika + kimia)/2
#jika nilai rata-rata <=70 maka grade D (dongo)
#jika nilai rata-rata <=80 maka grade C (1/4 CERDAS)
#jika nilai rata-rata <=90 maka grade B (1/2 CERDAS)
#jika nilai rata-rata <=100 maka grade A (Cerdas sekali kisanak ini)

#input
Nama=input("Masuckan nama mahsigma = ")
NF=float(input(" Masuckan nilai Fisika ="))
NK=float(input(" Masuckan nilai Kimia ="))
RT2=(NF+NK)/2

#Process
if RT2<=70:
    Ket="Grade D "
elif RT2<80:
    Ket="Grade C "
elif RT2<90:
    Ket="Grade B "
elif RT2<100:
    Ket="Grade A"
else:
    Ket="Salah memasukan data"

#output
print("Nilai rata-rata=", RT2)
print("Keterangan=", Ket)
