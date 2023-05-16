import time
print(" * " * 30)
print(" Deprem çantası hazırlama programına hoş geldiniz.")
print("sisteme üye olmak için 1\nsisteme giriş yapmak için 2 \nşifremi unuttum 3")
print(" * " * 30)

deprem_cantası = ["su", "fener", "yiyecek", "radyo"]


admin_sifre = "umut1"
admin_isim = "umut"


admin = input("admin misin?(Evet/Hayır)")  #Admin kısmı
if admin.lower() =="evet":
     admin_sifre_sorgu =input("Admin şifrenizi girin:")
     admin_isim_sorgu = input("Admin ismniniz girin")
     if admin_isim_sorgu ==admin_isim or admin_sifre_sorgu== admin_sifre:
         print("Mevcut deprem çantanız")
         print(deprem_cantası)


         while True:  #ürün eklemek
             canta =  input("eklemek istediğiniz eşyayı yazın:")
             canta_listesi = canta.split()
             deprem_cantası.extend(canta_listesi)
             elma = input("devam etmek ister misiniz (Evet/Hayır)")
             if elma.lower() == "hayır":
                 print(deprem_cantası)
                 break


while True:
    secim = int(input(" Seçiniz: "))

    if secim == 1:
        print("Üye olunuyor...")
        time.sleep(1)
        uye_sifre = input("Şifrenizi girin")
        uye_isim = input("Adınızı girin")

        e = [uye_sifre , uye_isim]

        sorgu = input("şifrenizi ve adınızı görmek istiyor musnuz")
        if sorgu.lower() == "evet":
            print("Şifreniz: {}, Adınız: {} dır ".format(uye_sifre, uye_isim))

    if secim == 2:
        yeni_sifre = input("Lütfen şifrenizi girin")  #şifre  sorgulama
        if yeni_sifre == e[0]:  #yeni_şifre== sifre kısmı çalışmıyor
            print("Doğru şifre")
            print("Çantanızdaki eşyaların fiyatları hesaplanıyor...")  #çantadaki ürünlerin fiyatını hesaplama
            time.sleep(3)




        else:
            print("Litfen şifrenizi belirleyin")

        yeni_sifre = input("lütfen adınızı girin")  #adını sorgulama
        if yeni_sifre == e[1]:
            print("Doğru isim")
        else:
            print("Litfen adınızı belirleyin")

    if secim == 3:
        print("programı tekrar başlatın ve yeni şifre oluşturun")
        break