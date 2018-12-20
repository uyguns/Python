#append()
#append kelimesi İngilizcede ‘eklemek, ilave etmek, iliştirmek’ gibi anlamlara gelir. append()
#metodunun görevi de kelime anlamıyla uyumludur. Bu metodu, bir listeye öğe eklemek için
#kullanıyoruz.

liste=["python","Ruby","C++"]
liste=liste+["html"]
print(liste)


liste=["python","Ruby","C++"]
liste.append("css")
print(liste)

işletim_sistemleri = ["Windows", "GNU/Linux", "Mac OS X"]
platformlar = ["IPhone", "Android", "S60"]

hepsi=işletim_sistemleri+platformlar
print(hepsi)

for i in platformlar:
    işletim_sistemleri.append(i)
    print(işletim_sistemleri)

a=[1,3,4]

for i in [10,11,12]:
    a.append(i)
print(a)

#birden fazla ekleme yapacağımız zaman for döngüsü kurmamiz gerejkir.

liste=[1,2,3]
for i in [4,5,6]:
    liste.append(i)
print(liste)

#Diyelim ki kullanıcının girdiği bütün sayıları birbiriyle çarpan bir uygulama yazmak istiyoruz.
kontrol=[]#kullanıcının girdiği sayıyı depolayacak
sonuc=1
while True:
    sayi=input("sayi(hesaplamak icin q):")
    if sayi=="q":
        break
    kontrol.append(sayi)
    sonuc *=int(sayi)

if len(kontrol)<2:#ontrol değişkeninin boyutuna bakarak kullanıcının 2 ‘den az sayı girip girmediğini denetliyoruz.
    print("yeterli sayi girilmedi")
else:
    print(sonuc)

#Burada kullanıcı her döngüde bir sayı girecek ve programımız girilen bu sayıyı sonuç
#değişkeninin o anki değeriyle çarparak yine sonuç değişkenine gönderecek. Böylece kullanıcı
#tarafından girilen bütün sayıların çarpımını elde etmiş olacağız. Kullanıcının ‘q’ harfine
#basmasıyla birlikte de sonuç değişkeninin değeri ekranda görünecek.

#extend()
#for döngüsü kurmadan birden fazla öğeyi ekler

a=[1,3,4]
b=[10,11,12]
a.extend(b)
print(a)

işletim_sistemleri = ["Windows", "GNU/Linux", "Mac OS X"]
platformlar = ["IPhone", "Android", "S60"]
işletim_sistemleri.extend(platformlar)
print(işletim_sistemleri)

#insert()
#listenin sonuna değil başka konuma eklemek için kullanılır.
liste=["ahmet özkoparan", "mehmet veli","serdar güzel","zeynep güz"]
liste.insert(1,"ferhat yaz")#1 sayısı nereye ekleyeceğimizi gösterir
print(liste)

f=open("/home/uygun/deneme.txt","r")
icerik=f.readlines()
icerik.insert(1,"ferhat yaz\n")
print(icerik)

g=open("/home/uygun/deneme.txt","w")
g.writelines(icerik)
f.close()
g.close()

#Gördüğünüz gibi yaptığımız işlem şu basamaklardan oluşuyor:
#1. Öncelikle dosyamızı okuma modunda açıyoruz (f = open("deneme.txt", "r"))
#2. Ardından dosya içeriğini bir liste olarak alıyoruz (içerik = f.readlines())
#3. Aldığımız bu listenin 2.sırasına “Ferhat Yaz” öğesini ekliyoruz (içerik.insert(1, "Ferhat Yaz\n"))
#4. Listeyi istediğimiz şekle getirdikten sonra bu defa dosyamızı yazma modunda açıyoruz
#(g = open("deneme.txt", "w"))
#5. Biraz önce düzenlediğimiz listeyi dosyaya yazıyoruz (g.writelines(içerik))
#6. Son olarak da, hem yaptığımız değişikliklerin etkin hale gelebilmesi hem de işletim
#sisteminin programımıza tahsis ettiği kaynakların serbest kalması için dosyalarımızı
#kapatıyoruz (f.close() ve g.close())

#reversed(list)
#liste öğelerini ters cevirme
diller=["python","ruby","c++","css"]
diller=diller[::-1]
print(diller)

reversed(diller)
print(diller)
print(*diller)

diller=["python","ruby","c++","css"]
diller.reverse()
print(diller)
print(*diller)

#pop
#remove()  metodu gibi listeden öğe silmemizi sağlar.
diller=["python","ruby","c++","css"]
diller.pop(0)#0 .öğeyi sildik.
print(diller)

#sort()
#Yine listelerin önemli bir metodu ile karşı karşıyayız. sort() adlı bu önemli metot bir listenin
#öğelerini belli bir ölçüte göre sıraya dizmemizi sağlar.
diller=["python","ruby","c++","css"]
diller.sort()#alfabe sırasına göre dizdi.
print(diller)

#sayıoları ıralaamk içinde kullanılır.
sayılar = [1, 0, -1, 4, 10, 3, 6]
sayılar.sort()
print(sayılar)

#tersten sıralamk içi reverse  parametresini kullanırız.
sayılar = [1, 0, -1, 4, 10, 3, 6]
sayılar.sort(reverse=True)#false olursa normal olur.
print(sayılar)

isimler = ["Ahmet", "Işık", "İsmail", "Çiğdem", "Can", "Şule"]
isimler.sort()
print(isimler)
#tersten
isimler.sort(reverse=True)
print(isimler)

#turkce harfleir doğru sıralamak içi kod.
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {harf: harfler.index(harf) for harf in harfler}
isimler = ["ahmet", "ışık", "ismail", "çiğdem", "can", "şule"]
isimler.sort(key=lambda x: çevrim.get(x[0]))
print(isimler)



#index()
# Bu metot bir liste öğesinin liste içindeki  konumunu söyler bize:
isimler = ["Ahmet", "Işık", "İsmail", "Çiğdem", "Can", "Şule"]
print(isimler.index("Ahmet"))
#count()
#bir öğenin o veri tipi içerisinde kaç kez geçtiğini söyler.
isimler = ["Ahmet", "Işık", "İsmail", "Çiğdem", "Can", "Şule"]
print(isimler.count("Can"))

isimler = ["Ahmet", "Işık", "İsmail", "Çiğdem", "Can", "Şule","Can"]
print(isimler.count("Can"))
#listeleri biribirini etkilemeden kopyalama
#copy metodu

#normal mod
isimler = ["Ahmet", "Işık", "İsmail", "Çiğdem", "Can", "Şule","Can"]
adlar=isimler
print(isimler)
print(adlar)
#etkilememsi için

isimler = ["Ahmet", "Işık", "İsmail", "Çiğdem", "Can", "Şule","Can"]
adlar=isimler[:]
isimler = ["Ahmet", "Işık", "İsmail", "Çiğdem", "Can", "Şule"]
print(isimler)
print(adlar)#etkilenmedi

isimler = ["Ahmet", "Işık", "İsmail", "Çiğdem", "Can", "Şule","Can"]
adlar=isimler.copy()
isimler = ["Ahmet", "Işık", "İsmail","Can", "Şule","Can"]
print(isimler)
print(adlar)#etkilenmedi
#clear()
#Listenin içini boşaltmak için kullanılır.

isimler = ["Ahmet", "Işık", "İsmail", "Çiğdem", "Can", "Şule","Can"]
isimler.clear()
print(isimler)#çıktısı [] bu şekildedir.

#Demetlerin Metodları
#index()
demet = ("elma", "armut", "çilek")
print(demet.index("çilek"))

#diğerlerindeki gibi öğe yerine söyler bize

#count() öğenin kaç kez geçtiğini söyler

demet = ("elma", "armut", "çilek")
print(demet.count("armut"))