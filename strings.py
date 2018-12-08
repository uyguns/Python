#karakter dizeleri

#[ilk_karakter:son_karakter:atlama_sayısı]
a="Bilgisiyar kavramları"
print (a[3])
print(a[0:6])
print(a[0:])
print(a[-10:-1])
x="mehmet uygun"
print(x[11:0:-1]) #-1 den dolayı ilk harfi almaz
print(x[::-1])  #tamamini tersten yazdirir.

# karakter dizelerinde m e r h a b a
#+ da				   1 2 3 4 5 6 7
#- de 				  -7-6-5-4-3-2-1 
#kullanilabilir	
print(a[-3])#sondan 3 karakteri  göster demektir.
print(a[:-3])#son 3 karakter hariç göster
print(a.find("kavram")) #"a"nın içerisinde  "kavram" karakterinin  kaçıncı karakterde olduğunu gösterir


veri="Bilgisayar kavramlari"
print(veri[3])
for sayi,harf in enumerate(veri):  #enumerate her ögeye tek tek sayi verir.
    # burada veri degiskeninden aldigi seyleri harf degiskenine atiyor.
    print(veri[sayi])   #yazdırmaya 3 harften baslar
    print(harf)

 
#karakter_dizisi[oge sirasi]
#Bu formulu uygulayarak karakter dizilerinin her bir ogesine tek tek erismemiz mumkun



nesne="mehmetuygun"
for i in range(len(nesne)):#Uzunluğunu bilmediğiniz karakter dizileri için range()
#fonksiyonuyla birlikte len() fonksiyonundan yararlanabilirsiniz.
    print(nesne[i])

isim=input("isminiz girin:  ")
for s in range(len(isim)):
	print(isminizin {}.harfi:{}.format(s,isim[s]))

  a="Bilgisiyar kavramları"
print(a[0:10]+"--"+a[11:22])#Araya birşeyler koyabiliriz.
print(a[5:1:-1])


site1="www.google.com"
site2="www.microsoft.com"
site3="www.apple.com"
site4="www.yahoo.com"
for isim in site1,site2,site3,site4:
    print("site: ",isim[4:-3])##4 ifadesiyle baştan 4 karakter sonra basliyor.
    #-3 ifadesiyle sondan 3 karakter yani"com" lardan sonra başlıyor.

#  çıktı: site:  google.
#site:  microsoft.
#site:  apple.
#site:  yahoo.


#Gorevimiz sonlarindaki ! isaretlerini kalidrmak

ata1="Akıllı bizi arayıp sormaz deli bacadan akar!"
ata2="Ağa güçlü olunca kul suçlu olur!"
ata3="Avcı ne kadar hile bilirse ayı da o kadar yol bilir!"
ata4="Lafla pilav pişse deniz kadar yağ benden!"
ata5="Zenginin gönlü oluncaya kadar fukaranın canı çıkar!"

for s in ata1,ata2,ata3,ata4,ata5:
    print(s[0:-1])

#Karakter Dizilerini Ters Çevirmek
s="mehmet uygun"
print(s[::-1])
print(s[::2])  #sondaki iki aynı zaman da 2 atlama anlamına gelir
#çıktı: mhe yu

nesne="12345678"
print(nesne[ -4]) #Tersden sayiyi okumaya baslar.sondan basa dogru
 print(int(nesne[3])*2) 
print(reversed("merhaba"))

for s in reversed("merhaba"):  #reversed tersten yazdirir.  [::-1]  buradaki -1 görevini yapar
    print(s,end="")#end parametresini yan yazdırsın diye kullandık

#Karakter Dizilerini Alfabe Sırasına Dizmek
# sorted fonksiyonu yazdigimiz dstringleri alfabetik siraya doker
print(sorted("mehmet uygun"))

for s in sorted ("bilgisayar kavramlari"):
    print (s,end="") #cikti:aaaaabgiiikllmrrrsvy


import locale
locale.setlocale(locale.LC_ALL,"tr_TR.UTF-8")
for s in sorted ("bilgisayar çavramlari",key=locale.strxfrm,):# ç nin çalismasi türkçe karakter ekledik.için 
    print (s,end="") #cikti:aaaaabgiiikllmrrrsvy

meyve="elma"
print("E"+meyve[1:])

site1="www.google.com"
site2="www.microsoft.com"
site3="www.apple.com"
site4="www.yahoo.com"
for s in site1,site2,site3,site4:
    print("HTTP://"+s)#Hepsinin basina http koyduk
    #www ları atalım
    print("HTTP://"+s[4:],sep="")#ilk 4 karakterden sonra basladik

    #dir()

#Bu metot bize Python’daki bir nesnenin özellikleri hakkında bilgi edinme imkanı verecek
print(dir(str))#str uzerindeki butun metodlari verir
print(dir(int))
a="merhaba"
print(dir(a))
sayac=0
for s in dir(""):
    if"_"not in s[0]:
        sayac+=1
        print(s)
    print("Toplam {} adet metot ile ilgileniyoruz.".format(sayac))

#Burada dir("") komutunun içerdiği her bir metoda tek tek bakıyoruz. Bu metotlar içinde, ilk
#harfi _ karakteri olmayan bütün metotları listeliyoruz. Böylece istediğimiz listeyi elde etmiş
#oluyoruz.

#Eğer yazdığınız bir programda numaralandırmaya ilişkin işlemler yapmanız gerekiyorsa
#Python’ın size sunduğu çok özel bir fonksiyondan yararlanabilirsiniz. Bu fonksiyonun adı
#enumerate().
print(*enumerate("merhaba"))

q="bilgisayar kavramlari"
for s in enumerate(q):
    print(s) 

for sira,metot in enumerate(dir("")):
    print(sira,metot)
    