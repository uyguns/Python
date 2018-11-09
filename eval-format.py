#eval fonksiyonu islem yapabilecegimiz bir suru seyi yapmamizi saglar.
#adeta sihirbaz gibidir.Hesap makinesin diger islemlere kadar.
veri=input("isleminiz: ")
a=eval(veri)
print(a)


url=input("Lutfen adresi yaziniz: ")#Once kullaniciden site adresini girmesini istedik.
print("Hata! google Chrome '{}' sitesini bulamadı".format(url))#'{}' ifadesi yukarida yazdigimiz site adresini gösteriri.
#.format(url) ise  bizim o site adresini zorlanmadan basmamizi saglar.