#eval fonksiyonu islem yapabilecegimiz bir suru seyi yapmamizi saglar.
#adeta sihirbaz gibidir.Hesap makinesin diger islemlere kadar.
veri=input("isleminiz: ")
a=eval(veri)
print(a)


url=input("Lutfen adresi yaziniz: ")#Once kullaniciden site adresini girmesini istedik.
print("Hata! google Chrome '{}' sitesini bulamadı".format(url))#'{}' ifadesi yukarida yazdigimiz site adresini gösteriri.
#.format(url) ise  bizim o site adresini zorlanmadan basmamizi saglar.

print("{} ve {} iyi bir iklidir".format("python","django"))
print("{},{}'yi seviyor".format("Ali","Ayse"))

#Burada da, gördüğüz gibi, öncelikle bir karakter dizisi tanımlıyoruz. Bu karakter dizisi
#içindeki değişken değerleri ise {} işaretleri ile gösteriyoruz. Daha sonra format() metodunu
#alıp bu karakter dizisine bağlıyoruz. Karakter dizisi içindeki {} işaretleri ile gösterdiğimiz
#yerlere gelecek değerleri de format() metodunun parantezleri içinde gösteriyoruz. Yalnız
#burada şuna dikkat etmemiz lazım: Karakter dizisi içinde kaç tane {} işareti varsa, format()
#metodunun parantezleri içinde de o sayıda değer olması gerekiyor.