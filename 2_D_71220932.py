print ("Pilihan model Matematika")
print ("1. Perkalian")
print ("2. Pembagian")
p1= int(input("Masukkan model matematika yang diinginkan 1/2 : "))
p2= int(input("Menampilkan table matematika dari angka: "))
if (p1==1):
    a1=[1,2,3,4,5,6,7,8,9,10]
    for i in range (1,11):
        kali=i*p2
        print(i, "x", p2, "=", kali)

elif (p1==2):
    a2=[50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65]
    for i in range(50,66):
        bagi=i/p2
        print(i, ":", p2, "=", bagi)
