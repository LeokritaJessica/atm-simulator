import datetime
import random
from customer import Customer

atm = Customer(id)

#Input PIN
while True:
    id = int(input('Masukkan Pin Anda: '))
    trial = 0

#Looping Verifikasi 
    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input('Pin yang Anda masukkan salah. \n Silahkan memasukkan kembali pin Anda: '))
        trial += 1

        if trial == 3:
            print('Error, Silahkan menunggu untuk memasukkan kembali pin Anda')
            exit()

#Looping Verifikasi setelah benar   
    while True:
        print('Selamat Datang di Bank kami')
        print('Pilihan Menu Utama')
        print('\n 1 - Cek Saldo \t 2 - Debet \n 3 - Simpan \t 4 - Ganti Pin \n 5 - keluar')
        chooseMenu = int(input('\n Silahkan pilih Menu: '))

        if chooseMenu == 1:
            print("\n Saldo anda: " + str(atm.checkBalance()))
        elif chooseMenu == 2:
            nominal = int(input('Masukkan nominal saldo: '))
            verifyBalance = input('Konfirmasi : Anda akan melakukan debel dengan nominal berikut ? y/n ' + str(nominal) + ' ')

            #Verify Y/N 
            if verifyBalance == 'y' :
                print('Saldo awal anda adalah: Rp ' + str(atm.checkBalance()) + ' ')
            else:
                break
            
            #Proses Debet
            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print('Transaksi debet berhasil')
                print('Saldo sisa sekarang: Rp' + str(atm.checkBalance()) + ' ')
            else:
                print('Maaf, Saldo anda tidak cukup untuk melakukan debet')
                print('Silahkan lakukan penambahan nominal saldo')

        elif chooseMenu == 3:
            nominal = int(input('Masukkan nominal saldo: '))
            verifyDeposit= input('Konfirmasi : Anda akan melakukan debel dengan nominal berikut ? y/n ' + str(nominal) + ' ')
            
            #Verify Y/N 
            if verifyDeposit == 'y' :
                atm.depositBalance(nominal)
                print('Saldo anda sekarang: ' + str(atm.checkBalance()) + '')
            else:
                break
        elif chooseMenu == 4:
            verifyPin = int(input('Masukkin Pin Anda: '))

            while verifyPin != int(atm.checkPin()):
                print('Password Anda Salah, \n silahkan Masukkan Pin: ')

            updatePin = int(input('Masukkan Pin baru Anda: '))
            print('Pin anda berhasil diubah')

            verifyNewPin = int(input('Masukkan pin baru Anda: '))

            if verifyNewPin == updatePin:
                print('pin baru anda sukses')
            else:
                print('maaf, pin anda salah! ')

        elif chooseMenu == 5:
            print('Resi tercetak saat Anda Keluar')
            print('No. Resi', random.randint(1000, 1000))
            print('Tanggal: ', datetime.datetime.now())
            print('Saldo akhir: ', atm.checkBalance() )
            print('terimakasih telah menggunakan bank Kami')
            exit()
        else:
            print('Maaf, menu tidak tersedia')
