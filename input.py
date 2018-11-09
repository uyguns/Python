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

a=input("Adinizi girin: ")
print("merhaba", a)

#Dairenin çapını girmesini kullanıcıdan isteyelim.
cap=input("Dairenin capini girin: ")
yaricap=int(cap) /2
pi=3.14159
#Yukarıdaki bilgileri girerek Alanımızı hesaplıyalım.
alan=pi* (yaricap*yaricap)
#Hesapladığımız alanı yazdırma.
print("capi", cap, "cm olan dairenin alani:", alan, "cm2'dir" )
#Burada yası ele alalım.
a=input("Lutfen yasinizi girin: ")
print("Yeni kullanicimiz", a ,"Yasindadir")

a=input("ogrencinin adi: ")
ad=str(a)
b=input("Dersin adi:   ")
ders=str(b)
c=input("1. yazili notunu girin: ")
y=int(c)
d=input("2. yazili notunu girin: ")
z=int(d)
Ortalama=(y+z)/2
print(ad,"adli ogrencinin", ders, "not ortalamasi",Ortalama)

print("-"*30)#30 cizgi ceker
gun_is=input("Lutfen ise gittiginiz gun sayisini girin: ")
a=int(gun_is)
gid_uc=input("Lutfen ise giderken odediginiz ucreti yazin: ")
b=float(gid_uc)
don_uc=input("Lutfen isten donerken odediginiz ucreti yazin: ")
c=float(don_uc)
masraf=a*(b+c)
print("-"*30)
print("Aylık ise gidis gelis masrafi: ", masraf)