import time

from kütüphane import *

print("""**************************

Kütüphane Programına Hoşgeldiniz!

İşlemler:

1. Kitapları Göster

2.Kitap Sorgula

3.Kitap Ekle

4.Kitap Sil

Çıkmak için 'q' ya  basınız.

**************************""")

kütüphane = Kütüphane()


while True:
    islem = input("Yapacağınız işlem:")

    if (islem == "q"):
        print("Program sonlandırılıyor...")
        kütüphane.baglantiyi_kes()
        break

        break
    elif (islem == "1"):
        print("\n")
        kütüphane.kitapları_goster()



    elif (islem == "2"):
        isim = input("Hangi kitabı istiyorsunuz ?:")
        print("Kitap sorgulanıyor..")
        time.sleep(2)

        kütüphane.kitap_sorgula(isim)

    elif (islem == "3"):
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayinevi = input("Yayınevi:")
        sayfa_sayisi = int(input("Sayfa Sayısı:"))
        yil = int(input("Yıl:"))
        tur = input("Tür:")

        yeni_kitap = Kitap(isim,yazar,yayinevi,sayfa_sayisi,yil,tur)

        print("Kitap ekleniyor..")
        time.sleep(2)

        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi.")



    elif (islem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz ?:")
        cevap = input("Emin misiniz ? (E/H):")

        if(cevap=="E"):
            print("Kitap siliniyor...")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("Kitap silindi.")


    else:
        print("Geçersiz işlem!")
