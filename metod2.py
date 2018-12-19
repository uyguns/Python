#capitalize()metodunun görevi karakter dizilerinin yalnızca ilk 
# harfini büyütmektir
kardiz="python"
print(kardiz.capitalize())#SADECE BAS HARFİ BUYULTUR.
print(kardiz.upper())#BUTUN HARFLERİ BUYULTUR.
print(kardiz.lower())#BUTUN HARFLERİ KUCULTUR

a="istanbul  buyuksehir belediyesi"
if a.startswith("i"):#eger baslangici "i" ise
    a="İ"+a[1:]  
a=a.capitalize()#bas harfi buyult
print(a)

#title()
#Bu metot,birden fazla kelimeden oluşan karakter dizilerinin her 
# kelimesinin ilk harflerini büyütür
a="istanbul buyuksehir belediyesi"
print(a.title())
kardiz="on iki ada"
kardiz=kardiz.title()
print(kardiz)

#swapcase()metoduda büyük-küçük harfle ilgili bir metottur. 
# Bu metot bir karakter dizisi içindeki büyük harfleri küçük harfe;
# küçük harfleri de büyük harfe dönüştürür.

kardiz="python"
print(kardiz.swapcase())

kardiz="PYTHON"
print(kardiz.swapcase())

#casefold() Bu metot işlev olarak lower() metoduna çok benzer. 
# Hatta Türkçe açısından,bu metodun lower()metodundan hiçbirfarkı yoktur
#tamamini kucuk harf yapar.
a="Python"
a=a.casefold()
print(a)

#  strip(), lstrip(), rstrip()
#strip() metodu yukarıdaki örnekte olduğu gibi parametresiz olarak
# kullanıldığında, bir karakter dizisinin sağında veya solunda 
# bulunan belli başlı karakterleri kırpar.
a="python << "
print(a)
a="python<"
print(a.strip("<"))

metin = """
>Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından> 90'lı yılların başında geliştirilmeye başlanmıştır.
>Çoğu insan, isminin Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını düşünür.
>Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından gelmez.
>Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz komedi
>grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır.
>Ancak her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
>bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır diyebiliriz."""
for i in metin.split():
   print(i.strip(">"),end=" ")

#lstrip  sadece sol tarafındakileri alır
kardiz="?merhaba?"
kardiz=kardiz.strip("?")
print(kardiz)

kardiz="?merhaba?"
kardiz=kardiz.lstrip("?")
print(kardiz)
#rstrip sadece sağ taratakileri kaldirir
kardiz="?merhaba?"
kardiz=kardiz.rstrip("?")
print(kardiz)



#join()
#split meteduyla kestigimiz karakter dizelerini tekrar birlestirir
kardiz="galatasaray spor kulubu"
bolunmus=kardiz.split()
print(bolunmus)

kardiz= " ".join(bolunmus)
print(kardiz)

#count()
#Bu metodun görevi bir karakter dizisi içinde belli bir karakterin
# kaç kez geçtiğini sorgulamaktır.
a="Kahramanmaras"
print(a.count("r"))# r harfinin kac kez gectigini gosterir.
a="Kahramanmaras"
print(a.count("a",2))
#Bu ikinci parametre,count()metodunun bir karakteri saymaya başlarken
# karakter dizisinin kaçıncı sırasından başlayacağını gösteriyoR
parola=input("parolaniz: ")
kontrol=True
for i in parola:
    if parola.count(i)>1:
        kontrol=False
if kontrol:
    print("parolaniz onaylandi")
else:
    print("parolanizda ayni harfi bir kez kullanabilirsiniz.")
#Bu metodu kullanarak,örneğin,kullanıcıyı aynı karakterden yalnızca 
#bir adet girmeye zorlayabilirsiniz .

kelime=input("Herhangi bir kelime")
for i in kelime:
    if i not in sayac:
        sayac+=i
for i in sayac:
    print("{} harfi {} kelimesinde {} geciyor ".format(i,kelime,kelime.count(i)))


#Daha sonra sayaç adlı bir değişken tanımlıyoruz. Bude ğişken,kullanıcının girdiği kelime içindeki harfleri tutacak.
# Bu değişken,kelimede ğişkeninden farklı olarak,kullanıcını ngirdiği sözcük içinde birden fazla geçen harflerden yalnızca tek bir örnek içerecek.
# Değişkenimizi tanımladıktan sonra bir for döngüsü kuruyoruz.Kullanıcının girdiği kelime içinde geçen harflerden herbirini yalnızca birkez 
# alıp sayaç değişkenine gönderiyoruz. Böylece elimizde her harften sadece bir adet olmuş oluyor.

kardiz="python programlama dili"
print(kardiz.count("a")) #butun karaketer icerisindeki a harfi sayisini bulur.
print(kardiz.count("a",15))#15. karakterden itibaren kac a gectigini bulur.
print(kardiz.count("a",15,17))#15 ile 17 karakter arasinda kac a oldugunu hesaplar

# index(), rindex()
#Bir akarket dizesinde harfin kacinci sirada oldugunu soyler
a="mehmet uygun"
print(a.index("t"))

kardiz="adana"
for i in range(len(kardiz)):
    print(kardiz.index("a",i))

kardiz=input("metin girin: ")
a=input("aranacak harf: ")
for i in range(len(kardiz)):
    if i==kardiz.index(a,i):#tekrarlamamsi icin
        print(i)

#Python’ın, karakter dizisini soldan sağa doğru değil de, sağdan sola doğru okumasını da
#sağlayabilirsiniz. Bu iş için rindex() adlı bir metottan yararlanacağız.
a="mehmet uygun"
print(a.rindex("t"))



# find, rfind()
#find() ve rfind() metotları tamamen index() ve rindex() metotlarına benzer. find()
#ve rfind() metotlarının görevi de bir karakter dizisi içindeki bir karakterin konumunu
#sorgulamaktır:
kardiz="python gonulluleri"
a=kardiz.find("o")
print(a)

kardiz="adana"
a=kardiz.find("n")

if a==-1:
    print("harf mevcut degil")
else:
    print(a)

#Aranilan harf eger yoksa .find -1 ciktisi verir.bizde burada -1 ciktisi olursa harf mevcur degil hatasi yazdirdik 
# degilse a yı yazdır dedik.

#center metodu karakter dizelerini ortalamak icin kullaniriz.

#ORNEK 1

kardiz="python"
print(kardiz.center(10))
#(10) islemi karakter dizesine uygulanacak ortalama 
#isleminin genisligini gösterir

#ORNEK 2

for i in range(1,20):
	print(kardiz.center(i))

#ORNEK 3

kardiz="elma"
print(kardiz.center(10,"-"))
#elma ya 10 karkaterlik yer actik.
#sonra elmayi ortalayip  3 sağ taraf 3 sol tarafa - isareti koyduk.

#rjust(), ljust()

#rjust() metodu bir karakter dizisini sağa yaslarken, ljust() metodu karakter dizisini sola yaslar.

#ÖRNEK 1
for i in "elma","armut","patlican":
    print(i.ljust(10,"."))

#ÖRNEK 2

for i in "elma","armut","patlican":
    print(i.rjust(10,"."))

#ÖRNEK 3

kardiz="tel no:"
kardiz=kardiz.ljust(10,".")
print(kardiz)
# ÖRNEK 4  KARAKTER DİZELERİNİ  AYNI HİZAYA GETİRMEKİCİN KULLANILIR.
ad="mehmet"
soyad="Uygun"
print("ad".ljust(10),":",ad)
print("soyad".ljust(10),":",soyad)

#zfill()
#Bu metot kimi yerlerde işimizi epey kolaylaştırabilir. zfill() metodu yardımıyla karakter dizilerinin 
# sol tarafına istediğimiz sayıda sıfır ekleyebiliriz:
#1. ÖRNEK
a="123456"
a=a.zfill(8)# 8 karakter ayirdik.6 tanesi kendisi.basina 2 tane sifir ekler.
print(a)    

#2. ÖRNEK

for i in range(11):
	i=str(i)#i yi str ye cevirdik
	print(i.zfill(2))

    #partition(), rpartition()
#Bu metot yardımıyla bir karakter dizisini belli bir ölçüte göre üçe bölüyoruz
a="mehmet uygun"
a=a.partition("u")
print(a)

b="mehmet uygun"
b=b.rpartition("u")
print(b)

a="adana"
print(a.partition("a"))
print(a.rpartition("a"))# 3 e boler.a yı ortaya koyar öncesi varsa ilk başa koyar.
#sonrasini en sona koyar

#expandtabs()
#u metot yardımıyla bir karakter dizisi içindeki sekme boşluklarını genişletebiliyoruz.
a="elma\tbir\tmeyvedir"#bir tab bosluk birakir. 
print(a)

a="elma\tbir\tmeyvedir"#bir tab bosluk birakir. 
print(a.expandtabs(20))#20 karakterlik tab boslugu birakir.