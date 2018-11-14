#* işleci de Python’da birden fazla anlama gelir. Bu işlecin, çarpma ilişkisi kurma işlevi dışında tekrar etme ilişkisi kurma işlevi de vardır. Yani:

print("hizli" * 2)

#+=toplama
#-=cikarma
#/=bolme
#*=carpma
# %=modul: bolme isleminin kalanini gosterir

print(30 % 4)# 30 u 4 e bolduk 7*4=28 kalan 2.
a=int(input("sayi gir:"))
if a % 2== 0:
	# herhangi bir sayinin 2'ye bolumu 0'a esit ise o sayi cift sayidir
	print(a,"cift sayidir")
else:
	print(a, "tek sayidir")


#Programımız, kullanıcının girdiği ilk sayının ikinci sayıya tam bölünüp bölünmediğini hesaplıyor ve sonuca göre kullanıcıyı bilgilendiriyor. 

bolunen=int(input("sayi girin :"))
bolen=int(input("sayi girin :"))
sablon="{} sayisi {} sayisina tam".format(bolunen,bolen)
if bolunen % bolen==0:
#Programımızın temelini bu kod (yukaridaki) oluşturuyor. Çünkü bir sayının bir sayıya tam bölünüp bölünmediğini bu kodla belirliyoruz. Eğer bir sayı başka bir sayıya bölündüğünde kalan değer, yani modülüs 0 ise, o sayı öbür sayıya tam bölünüyor demektir.
	print(sablon,"bolunuyor")
else:
	print(sablon,"bolunmuyor")


# //= taban bolme

print(5/2)
#normal bolmede ciktisi 2.5 dir.yani kesirlidir.
print(5//2) 
# taban bolme islemi yaprsak sonuc kesirli degil tamsayi cikar  cikti=2 dir
a=5/2
print(type(a))# sonuc float cikar 
a=5//2
print(type(a))#sonuc int cikar

# round fonksiyonu yuvarlama fonksiyonudur
print(round(2.55))#ruond 2.55 sayisini 3'e yuvarlar
print(round(100.67,))
print(round(33.68,3))# 3 sayisinin oldugu yer  noktanin sagindan sonr!ki korunacak basamagi gosterir.

#**foksiyonu karesini alma

print(25*25)#bunu soyle yapabiliriz

print(25 ** 2)
print(625 ** 0.5)#tam tersi
#pow fonksiyonuda kare alma fonksiyonudur
print(pow(25,2))#25 in karesi

