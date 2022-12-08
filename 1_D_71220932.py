uang = int(input('Masukkan jumlah uang:'))
mulai = input("ketik 'START' untuk memulai: ")

susu = 20000
permen = 500
roti = 15000
indomie = 3000
vitamin = 50000

if mulai.lower() == 'start':
    while True:
        beli = input('Apa barang yang akan anda beli? ')
        if beli.lower() =='susu':
            if uang >= susu:
                uang -= susu
                print('sisa uang Anda',uang)
            else:
                print('uang tidak cukup')
        elif beli.lower() =='permen':
            if uang >= permen:
                uang -= permen
                print('sisa uang Anda',uang)
            else:
                print('uang tidak cukup')
        elif beli.lower() =='roti':
            if uang >= roti:
                uang -= roti
                print('sisa uang Anda',uang)
            else:
                print('uang tidak cukup')
        elif beli.lower() =='vitami ':
            if uang >= vitamin:
                uang -= vitamin
                print('sisa uang Anda',uang)
            else:
                print('uang tidak cukup')
        elif beli.lower() =='indomie':
            if uang >= indomie:
                uang -= indomie
                print('sisa uang Anda',uang)
            else:
                print('uang tidak cukup')
        elif beli.lower() == 'sudah':
            break
        else:
            print('Barang tidak tersedia')