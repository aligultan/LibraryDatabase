import sqlite3

import time

class Kitap():

    def __init__(self,isim,yazar,yayinevi,sayfasayisi,yil,tür):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.sayfasayisi = sayfasayisi
        self.yil = yil
        self.tür = tür

    def __str__(self):
        return "Kitap İsmi: {}\nYazar: {}\nYayınevi: {}\nSayfa Sayısı: {}\nYıl: {}\nTür: {}".format(self.isim,self.yazar,self.yayinevi,self.sayfasayisi,self.yil,self.tür)



class Kütüphane():

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti=sqlite3.connect("Kütüphane.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create table if not exists Kitaplar (isim TEXT,yazar TEXT,yayinevi TEXT,sayfasayisi INT,yıl INT,tür TEXT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def kitapları_goster(self):

        sorgu = "Select * from Kitaplar"

        self.cursor.execute(sorgu)

        kitaplar = self.cursor.fetchall()

        if (len(kitaplar)==0):
            print("Kütüphanede kitap bulunmuyor.")

        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4],i[5])
                print(kitap)
                print("\n")

    def kitap_sorgula(self,isim):

        sorgu = "Select * from Kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kitaplar  = self.cursor.fetchall()

        if(len(kitaplar)==0):
            print("Böyle bir kitap bulunmuyor...")

        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4],kitaplar[0][5])

            print(kitap)
    def kitap_ekle(self,kitap):

        sorgu = "insert into kitaplar values(?,?,?,?,?,?)"

        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.sayfasayisi,kitap.yil,kitap.tür))

        self.baglanti.commit()

    def kitap_sil(self,isim):

        sorgu = "Delete from kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        self.baglanti.commit()
