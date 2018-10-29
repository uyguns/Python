
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
print("merhaba, " x)

#Dairenin çapını girmesini kullanıcıdan isteyelim.
cap=input("Dairenin capini girin: ")
yaricap=int(cap) /2
pi=3.14159
#Yukarıdaki bilgileri girerek Alanımızı hesaplıyalım.
alan=pi* (yaricap*yaricap)
#Hesapladığımız alanı yazdırma.
print("capi", cap, "cm olan dairenin alani:", alan, "cm2'dir" )

a=input("Lutfen yasinizi girin: ")
print("Yeni kullanicimiz", a ,"Yasindadir")36
