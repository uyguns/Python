Giris= """
(1) Topla
(2) Cikar
(3) Carp
(4) Bol
(5) Karesini Hesapla
(6) Karakök Hesapla
"""
print(Giris)

soru=input("Lutfen Yapmak istediginiz islemin numarasını girin: ")

if soru =="1":
    sayi1=int(input("Toplama islemi icin ilk sayiyi girin:  "))
    sayi2=int(input("Topla islemi icin ikinci sayiyi girin: " ))
    print(sayi1, "+", sayi2,"=",sayi1+sayi2 )
#eğer sorunun değeri '1' ise:
#Toplama işlemi için ilk sayı girilsin. Bu değere 'sayı1' diyelim.
#Sonra ikinci sayı girilsin. Bu değere de 'sayı2' diyelim.
#En son, 'sayı1', '+' işleci, 'sayı2', '=' işleci ve 'sayı1 + sayı2'
#ekrana yazdırılsın...
if soru =="2":
    sayi3=int(input("Cikarma islemi icin ilk sayiyi girin: "))
    sayi4=int(input("Cikarma islemi icin ikinci sayiyi girin: " ))
    print(sayi3, "-", sayi4,"=",sayi3-sayi4)
elif soru =="3":
    sayi5=int(input("Carpma islemi icin  ilk sayiyi girin: "))
    sayi6=int(input("Carpma islemi icin ikinci sayiyi girin: "))
    print(sayi5,"*",sayi6,"=",sayi5*sayi6)
elif soru =="4":
    sayi7=int(input("Bolme islemi icin ilk sayiyi girin:  "))
    sayi8=int(input("Bolme islemi icin ikinci sayiyi girin: "))
    print(sayi7, "/",sayi8,"=",sayi7/sayi8)
elif soru =="5":
    sayi9=int(input("Karesini almak icin  sayiyi  girin: "))
    print(sayi9,"sayisinin karesi =",sayi9**2)
elif soru =="6":
    sayi10=int(input("Karekokunu hesaplamak istediginiz sayiyi girin: "))
    print(sayi10,"sayisinni karekoku =",sayi10**0.5)
else:
    print("yanlıs giris")
    print("Asagidaki seceneklerden birini girin",Giris)
#Eğer burada bütün blokları
#if kullanarak yazarsanız, biraz sonra kullanacağımız else bloğu her koşulda çalışacağı için
#beklentinizin dışında sonuçlar elde edersiniz.
#Yukarıdaki kodlarda az da olsa farklılık gösteren tek yer son iki elif bloğumuz. Esasında
#buradaki fark da pek büyük bir fark sayılmaz. Neticede tek bir sayının karesini ve karekökünü
#hesaplayacağımız için, kullanıcıdan yalnızca tek bir giriş istiyoruz.

#Eğer böyle bir durum varsa:
#şöyle bir işlem yap
#Yok eğer şöyle bir durum varsa:
#böyle bir işlem yap
#Eğer bambaşka bir durum varsa
#şöyle bir şey yap