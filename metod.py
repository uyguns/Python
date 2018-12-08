#REPLACE 

kardiz="elma"
print(kardiz.
	replace("e","E"))

#karakter_dizisi.metot(parametre)
#Metotlar karakter dizilerinden nokta ile ayrilir..
kardiz="memleket"
print(kardiz.replace("ket","KET"))	

kardiz="memleket"
print(kardiz.replace("e",""))

#Burada gordugunuz gibi, replace() metodu ayni anda birden 
#fazla karakteri degistirme yetenegine de sahip.
#Gordugunuz gibi, replace() metodunu iki parametre ile kullanip 
#Ucuncu parametreyi belirtmedigimizde, “memleket” kelimesi icindeki
#butun “e” harfleri bos karakter dizisi ile
#degistiriliyor (yani bir anlamda siliniyor).

kardiz="memleket"
print(kardiz.replace("e","",1))
print(kardiz.replace("e","",2))

#Burada replace() metodunu Ucuncu bir parametre ile birlikte kullandik. Ucuncu parametre
#olarak 1 sayisini verdigimiz icin replace() metodu sadece tek bir “e” harfini sildi.
#Bu ucuncu parametreyi, silmek istediginiz harf sayisi kadar arttirabilirsiniz
#Burada ilk ornekte ucuncu parametre olarak 2 sayisini kullandigimiz icin, ‘replace’ isleminden
#karakter dizisi icindeki 2 adet “e” harfi etkilendi.


#split(), rsplit(), splitlines()
#Bu metodun gorevi karakter dizilerini belli noktalardan bolmektir.
kardiz="istanbul buyuksehir belediyesi"
print(kardiz.split())
for i in kardiz.split():
	print(i)

kardiz=input("Kisaltmasini istedigimiz kurum adi: ")
for i in kardiz.split():
	print(i[0])


kardiz = "Bolvadin, Kilis, Siverek, iskenderun, istanbul"
kardiz=kardiz.split()
for i in kardiz:
	print(i)

kardiz = "Bolvadin, Kilis, Siverek, iskenderun, istanbul"
kardiz=kardiz.split("l")#tirnak isareti arasinda ki virgul bolunen yeri virgullerle birlikte alir. 
for i in kardiz:
	print(i)
#Bu sayede split() metodu karakter dizisini virgullerden bolmeyi basardi.
#Tahmin edebileceginiz gibi, split() metoduna hangi parametreyi verirseniz bu metot ilgili karakter dizisini o karakterin gectigi yerlerden bolecektir. Yani mesela siz bu metoda “l” parametresini
#verirseniz, bu metot da ‘l’ harfi gecen yerden karakter dizisini bolecektir:
#Eger degitirilmek istenen karakter, karakter dizisi icinde yer almiyorsa herhangi bir islem yapilmaz.
kardiz="Ankara Buyuksehir Belediyesi"
for i in kardiz.split(" ",1):#Cumlenin 1 sefer bolunecegini ifade eder.
	print(i)

#rsplit() metodu her yonuyle split() metoduna benzer. split() ile rsplit() arasindaki
#tek fark, split() metodunun karakter dizisini soldan saga, rsplit() metodunun ise sagdan
#sola dogru okumasidir.
kardiz="Ankara Buyuksehir Belediyesi"
for i in kardiz.rsplit(" ",1):#Sondan belediyeyi boldu.
	print(i)

#splitlines() metodunu ise bir karakter dizisini satir satir ayirmak icin kullanilir.
#Amacimiz uzun bir metni satir satir bolmek olsun
kardiz="""Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin
Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını
düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından
gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz
komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek
adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama
dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek
halini almıştır diyebiliriz."""
print(kardiz.splitlines())