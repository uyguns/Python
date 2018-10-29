

#İnput Kullanıcadan veri alamyı sağlar
input("Giris: ")

#input fonksiyonu kullanıcıdan bir değer alıp
#  bu değeri döndürür. Eğer biz bu fonksiyonu yukarıdaki gibi 
# kullanırsak alınan veriyi bir daha kullanamayız. 
# Aldığımız veriyi kullanmak için input fonksiyonunu bir 
# nesneye atamalıyız.
input("a' nın Degerı:  ")

Giris= input("Lutfen Kullanici Adinizi Giriniz: ")
print(Giris)

Hosgeldiniz_Yazisi = """
Hos Geldiniz...
Bu program pyton diliyle konsol uzerinden yazilmistir. """
print(Hosgeldiniz_Yazisi)

K_Adi=input('Lutfen kullanici adini girin: ')
print(K_Adi, 'Adli uye basariyle giris yaptı. ')

x=input("Adinizi girin: ")
print("merhaba, "  +x)

isim=input("Adınızı girin:")
print("Merhaba", isim, end="!\n")

#Örnek -1 : Girilen iki adet sayıyı toplayan program yazınız
ilk_sayi=input("1. sayiyi yaziniz: ")
ikinci_sayi=input("2. sayyiyi yazınız: ")
topla=int("ilk_sayi+ikinci_sayi")
print(topla)