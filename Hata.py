#Python’da hata yakalama işlemleri için try... except... bloklarından yararlanılır
ilk_sayi=input("İlk sayi girin: ")
ikinci_sayi=input("ikincisayi girin: ")
try:
    sayi1=int(ilk_sayi)
    sayi2=int(ikinci_sayi)
    print(sayi1,"/",sayi2,"=",sayi1/sayi2)
except ValueError:
    print("lutfen sayi girin")

#Eğer try bloğu içinde belirtilen işlemler sırasında bir ValueError ile karşılaşırsan
# bunu görmezden gel ve normal şartlar altında kullanıcıya göstereceğin hata mesajını gösterme. 
# Onun yerine kullanıcıya Lütfen sadece sayı girin! uyarısını göster

#try:
#hata verebileceğini bildiğimiz kodlar
#except HataAdı:
#hata durumunda yapılacak işlem

ilk_sayi=input("İlk sayi girin: ")
ikinci_sayi=input("ikincisayi girin: ")
try:
    sayi1=int(ilk_sayi)
    sayi2=int(ikinci_sayi)
    print(sayi1,"/",sayi2,"=",sayi1/sayi2)
except ZeroDivisionError:
    print("Bu sayı 0 'a bölünemez")# 0 'A BÖLÜNEMECEĞİNİ BELİRTMEK İÇİN "ZERO DEVİSİON ERROR" KULLANIRIZ.
except ValueError:
    print("lutfen sayi girin")
#Gördüğünüz gibi çözüm gayet mantıklı. Birden fazla hata türü üreteceğini bildiğimiz kodları
#yine tek bir try bloğu içine alıyoruz. Hata türlerini ise ayrı except blokları içinde ele alıyoruz

while True:
    ilk_sayi=input("İlk sayi girin(programdan çıkmak için q basın ):")
    if ilk_sayi=="q":
        break
    ikinci_sayi=input("ikincisayi girin: ")
    try:
        sayi1=int(ilk_sayi)
        sayi2=int(ikinci_sayi)
        print(sayi1,"/",sayi2,"=",sayi1/sayi2)
    except (ValueError,ZeroDivisionError): #gruplandırma yapabiliriz.
        print("Bir Hata oluştu.")
        print("Lutfen tekrar deneyin")
#try... except... as...
#Diyelim ki kullanıcıya olası bir hata durumunda hem kendi yazdığınız hata mesajını, hem 
# de özgün hata mesajını göstermek istiyorsunuz. İşte yukarıdaki yapı böyle durumlarda 
# işe yarayabilir:
while True:
    ilk_sayi=input("İlk sayi girin(programdan çıkmak için q basın ):")
    if ilk_sayi=="q":
        break
    ikinci_sayi=input("ikincisayi girin: ")
    try:
        sayi1=int(ilk_sayi)
        sayi2=int(ikinci_sayi)
        print(sayi1,"/",sayi2,"=",sayi1/sayi2)
    except (ValueError,ZeroDivisionError ) as hata: #gruplandırma yapabiliriz.
        print(hata)
        print("Lutfen tekrar deneyin")


#try... except... else...
try:
    bolunen =int(input("Lutfen bolunecek sayıyı girin: "))
    bolen =int(input("Lutfen bolen sıyıyı girin: "))
    
except ValueError:
    print("lütfen sayı girin!")
else:
    try:
        print(bolunen/bolen) 
    except ZeroDivisionError:
        print("lutfen 0 dan farklı sayı girin!")

#try... except... finally...
#try:
#...bir takım işler...
#except birHata:
#...hata alınınca yapılacak işlemler...
#finally:
#...hata olsa da olmasa da yapılması gerekenler..
#finally.. bloğunun en önemli özelliği, programın çalışması sırasında herhangi bir hata
#gerçekleşse de gerçekleşmese de işletilecek olmasıdır. Eğer yazdığınız programda mutlaka
#ama mutlaka işletilmesi gereken bir kısım varsa, o kısmı finally... bloğu içine yazabilirsiniz.

try:
dosya = open("dosyaadı", "r")
...burada dosyayla bazı işlemler yapıyoruz...
...ve ansızın bir hata oluşuyor...
except IOError:
print("bir hata oluştu!")
finally:
dosya.close()

#raise  hata olmasada biz hata verdirmek istersek kullanırız

bolunen=int(input("bolunecek sayıyı girin: "))
if bolunen==23:
    raise Exception ("23 sayısı gormek istemiyorum")
bolen=int(input("Bolen sayiyi girin: "))
print(bolunen/bolen)
#kullanıcı 23 girerse "23 sayısını görmek istemiyorum hatası çıkar."


tr_karakter="şğıüö"
parola=input("Parolanız: ")
for i in parola:
    if i in tr_karakter:
        raise TypeError("TURKCE KARAKTER KULLANILAMAZ")
    else:
        pass
print("Parola kabul edildi")

#Bu kodlar çalıştırıldığında, eğer kullanıcı, içinde Türkçe karakter geçen bir parola yazarsa
#kendisine TypeError tipinde bir hata mesajı gösteriyoruz. Eğer kullanıcının parolası Türkçe
#karakter içermiyorsa hiçbir şey yapmadan geçiyoruz ve bir sonraki satırda kendisine ‘Parola
#kabul edildi!’ mesajını gösteriyoruz.

#4.örnek
sayi=int(input("sayi girin:")) 
if sayi==25:
    raise ValueError("25 i sevmiyorum")

    
try:
    bolunen=int(input("sayiyi girin: "))
    bolen=int(input("sayiyi girin: "))
    print(bolunen/bolen)
except ZeroDivisionError:
    print("sıfır kullanmassınız")
    raise

#Bütün Hataları Yakalamak

#try:
#....birtakım işler...
#except:
#...hata mesajı...

try:
    a=int(input("1.sayi: "))
    b=int(input("2. sayi: "))
    print(a*b)
   
except:
    print("Hata yaptın")
