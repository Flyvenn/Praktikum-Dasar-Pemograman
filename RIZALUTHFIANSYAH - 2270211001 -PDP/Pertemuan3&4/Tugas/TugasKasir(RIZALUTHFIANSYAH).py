print("             NGOPILAH                ")
print("           Bumi Mutiara              ")
print("           087796515630              ")
print("=====================================") 

nama=input(" Nama Pelanggan     : ")
telpon=input(" Nomor Telepon      : ")
import time

tanggal = time.strftime("%d-%m-%y %H:%M:%S")
print(tanggal)
print(type(tanggal))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("     ~~~~~MENU~~~~~    ")
print("1. Kopi Susu Gula Aren           Rp.10000")
print("2. Coffe Caramel                 Rp.15000")
print("3. Americano                     Rp.12000")
print("4. Caffe Latte                   Rp.12000")
print("5. Green Tea Latte               Rp.16000")
print("6. Thai Tea                      Rp.16000")
print("     ~~~~~MENU~~~~~      ")
h=[]
a=1 

menu_pesanan = int (input("Masukkan Menu Pesanan Anda (Nomor Pesanan) : "))
if menu_pesanan == 1:
    harga = 10000
elif menu_pesanan == 2:
    harga = 15000
elif menu_pesanan == 3:
    harga = 12000
elif menu_pesanan == 4:
    harga = 12000
elif menu_pesanan == 5:
    harga = 16000
elif menu_pesanan == 6:
    harga = 16000
else:
    while True :
        print("----Menu Tidak Tersedia Silahkan Pilih Menu Lain ----")
        if menu_pesanan ==  1 or menu_pesanan == 2 or menu_pesanan == 3 or menu_pesanan == 4 or menu_pesanan == 5 or menu_pesanan == 6:
            if menu_pesanan == 1:
                harga = 10000
            elif menu_pesanan == 2:
                harga = 15000
            elif menu_pesanan == 3:
                harga = 12000
            elif menu_pesanan == 4:
                harga = 12000
            elif menu_pesanan == 5:
                harga = 16000
            elif menu_pesanan == 6:
                harga = 16000
                break

jumlah_pembelian = int (input("Masukkan Jumlah Pembelian :"))
for i  in range(jumlah_pembelian):
    h.append(harga)

while True:
    jawab = input("Apakah ada yang ingin ditambah/dikurangi ? tambah/kurang/tidak   : ")
    if jawab == 'tambah' :
        tambah = int(input("Masukkan Menu Pesanan (Nomor Menu):    "))
        if tambah == 1:
            harga = 10000
        elif tambah== 2:
            harga = 15000
        elif tambah == 3:
            harga = 12000
        elif tambah == 4:
            harga = 12000
        elif tambah == 5:
            harga = 16000
        elif tambah == 6:
            harga = 16000
        jumlah_tambahan = int(input("Masukan Jumlah Pembelian : "))
        for i in range(jumlah_tambahan):
            h.append(harga)
        c =jumlah_tambahan+jumlah_pembelian
        print("Total Pesanan :  ",c)
        bayar = sum(h)
        print("Total Pembayaran : Rp.{}".format(bayar))
        break
    elif jawab == 'kurang' :
        kurang = int(input("Berapa Jumlah yang dikurangkan ? "))
        for  i in range (kurang):
            if kurang <= 1:
                a -= kurang
                del h[a]
                bayar = sum(h)
                break
            else:
                kurang -= a
                del h[kurang]
                if kurang < 0:
                    break
        c = jumlah_pembelian - kurang 
        print("Total Pemesanan ",c)
        bayar = sum(h)
        print("Total Pembayaran : Rp.{}".format(bayar))
        break
    else :
        bayar = sum(h)
        c = jumlah_pembelian
        print("Total Pemesanan", c)
        print("Total Pembayaran : Rp.{}".format(bayar))
    break