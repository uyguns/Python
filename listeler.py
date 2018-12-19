#listeler
liste=["mehmet","uygun",1,2,3,"python",["c++","java",88]]
print(liste)
print(liste[2])
print(liste[-1])
print(liste[-1][1])
print(liste[-1][0])

veri=input("gir: ")
listemiz=list(veri)#list ile tümünü parçalara ayirabiliyoruz.
print(listemiz)




liste=["mehmet","uygun",1,2,3,"python",["c++","java",88]]
liste[4]="go"# listemizin 4 üyesi olan 3 sayisini  go ile degistirdik.
liste[6][1]="ruby"
del liste [0]# 0. öğeyi sildik
del liste [5][2]# 5 2. öğesini sildik.

print(liste)
print(type(liste))



liste=["mehmet","uygun",1,2,3,"python",["c++","java",88]]
oge_no=liste.index("uygun")#uygun kelimesinin kacinci ogede oldugunu buldu
del liste[oge_no]#bulunan ogedeki karakteri sil
print(liste)

#listeye öğe ekleme
liste=["mehmet","uygun",1,2.3,"python",["c++","java",88]]
liste [5]+=["go"]#6. listenin içine go ekler
liste +=["ruby"] #listenin en sonuna ekler
print(liste)

liste=["mehmet","uygun",1,2,3,"python",["c++","java",88]]
liste[1]="karcılar"# burada listenin 1 . öğesini karcılar ile değiştirdik.
print(liste)


#listelerin belirleyici özelliği de köşeli parantezlerdir
#Karakter dizilerinin metotlarını sıralamak için dir() adlı bir fonksiyondan yararlanmıştık.
print(dir(str))
komut=dir(str)
print(type(komut))
#goruldugu gibi "dir" fonksiyonun çıktısı bir listedir.
#dir() fonksiyonu dışında, başka bir şeyin daha bize liste verdiğini biliyoruz. Bu şey, karakter
#dizilerinin split() adlı metodudur:

a="istnabul buyuksehir belediyesi"
print(a[0])#karakter dizesi oldugu icin "i "yi verir
a="istnabul buyuksehir belediyesi"
a=a.split()#split liste haline getirdiğiicin istanbul sonucunu verir
print(a[0])

a=["istnabul buyuksehir belediyesi","izmir","kutahya"]
a=a[2]
print(a)
#listelerde len fonksiyonu

a=["istnabul buyuksehir belediyesi","izmir","kutahya"]
print(len(a))

# len() fonksiyonu dışında, range() fonksiyonuyla listeleri de birlikte kullanabilirsiniz.
sayılar=[[0, 10], [6, 60], [12, 54], [67, 99]]
for i in sayılar:
    print(i)#Eğer döngü içinde sadece öğeleri ekrana yazdırıyor olsaydık böyle bir kodumuz olacaktı:
    print (*range(*i))

#Yukarıdaki listelerde görünen ilk sayılar range() fonksiyonunun ilk parametresi, ikinci sayılar ise
#ikinci parametresi olacak.yani başlangıc ve biriş sayıları

#list() Fonksiyonu
#list metoduyla karakter dizelerini liste ye ceviririz.
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
alfabe=alfabe.split()
print(alfabe)
#split() metodunun bir karakter dizisini bölüp bize bir liste verebilmesi için karakter dizisinin belli
# bir ölçüte göre bölünebilir durumda olması gerekiyor virgü yada boşluk gibi

alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

a=list(alfabe)
print(a)
#list metoduyla listeleri ölçüt olmadan parçalarına ayırabiliyoruz.
#list() fonksiyonu yardımıyla bu karakter dizisini tek hamlede listeye çevirmiş olduk.

print(range(10))

#list() fonksiyonunun önemli bir görevi de range() fonksiyonunun, sayı aralığını ekrana basmasını sağlamaktır.
#Bu sayı aralığını ekrana dökmek için range() fonksiyonu üzerinde bir for döngüsü kurmamız gerekir:
for i in range(10):
    print(i)
#bu görevilist şöyle yapar
print(list(range(10)))
#Aslında burada yaptığımız şey range(10) ifadesini bir listeye dönüştürmekten ibarettir.

#Listeleri Birleştirmek

derlenen_diller = ["C", "C++", "C#", "Java"]
yorumlanan_diller = ["Python", "Perl", "Ruby"]
a=derlenen_diller+yorumlanan_diller
print(a)

sayilar=0
for i in range(10):
    sayilar+=int(input("not: "))
print(sayilar/10)
#kullanicidan 10 tane sayi girmesini istedik ve girilen sayilartin ortalamsını aldık

#eki girilen sayıların ortalaması ile birlikte, hangi sayıların girildiğini de göstermek isterseniz nasıl bir kod yazarsınız?

sayilar=0
notlar=[]
for i in range(10):
    veri=int(input("{} not: ".format(i+1)))
    sayilar+=veri
    notlar+=[veri]#kullanıcıdan gelen veri adli değişkeni liste haline getiriyoruz.
print("girdiğiniz notlar: ",*notlar)
print("not ortalamanız",sayilar/10)

liste=[]
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
for i in alfabe:
    liste+=i
print(liste)
#list() fonksiyonu da tam olarak böyle çalışır. Yani bir karakter dizisi üzerinde döngü kurarak,
# o karakter dizisinin her bir öğesini tek tek bir listeye atar.

liste1=["python","cc++","go","css"]
liste2=liste1
print(liste1)
print(liste2)
#yukarıda ki örnekte liste1 degistiği zaman liste 2 de değişir.
#aşağıda ise liste [:] bu işaret liste 1 deki değişiklikten lisete 2 nin etkilenmemesini sağlar.
liste2=liste1[:]
liste1[0]="java"
print(liste1)
print(liste2)
 # aynı işi list metufuyla da yapabiliriz.
liste1=["python","cc++","go","css"]
liste2=list(liste1)
liste1[1]="ruby"
print(liste1)
print(liste2)

# liste üreteçleri

liste=[i for i in range(10)]
print(liste)

#eski usul
liste=[]
for i in range(10):
    liste+=[i]
    print(liste)
#liste üreteçleriyle kolayca 10 kadar 2 ile bolunen sayıları tuttuk.
liste=[i for i in range(10) if i%2==0]
print(liste)
# uzun yolu
liste=[]
for i in range(10):
    if i%2==0:
        liste+=[i]
print(liste)

liste=[i for i in range (10) if i%2==1]
print(liste)
#uzun yol
liste = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[10, 11, 12]]
a=[]
for i in liste:
    for z in i:
        a+=[z]
print(a)
#kısa yol

a=[ z for i in liste for z in i]
print(a)



liste1 = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[10, 11, 12],
[13, 14, 15],
[16, 17, 18],
[19, 20, 21],
[22, 23, 24],
[25, 26, 27],
[28, 29, 30],
[31, 32, 33]]

liste2 = [1, 27, 88, 98, 50, 9, 28, 45, 54, 66, 61, 23, 10, 33,
22, 12, 6, 99, 63, 26, 87, 25, 77, 5, 16, 93, 99, 44,
59, 69, 34, 10, 60, 92, 61, 44, 5, 3, 23, 99, 79, 51,
89, 63, 53, 31, 76, 41, 49, 10, 88, 63, 55, 43, 40, 71,
16, 49, 78, 41, 35, 97, 33, 76, 25, 81, 15, 99, 64, 20,
33, 6, 89, 81, 44, 53, 59, 75, 27, 15, 64, 36, 72, 78,
34, 36, 20, 41, 41, 75, 56, 30, 86, 46, 9, 42, 21, 64,
26, 52, 77, 65, 64, 12, 38, 1, 35, 20, 73, 71, 37, 35,
72, 38, 100, 52, 16, 49, 79]
#Burada amacınız liste1 içinde yer alan iç içe geçmiş listelerden hangisinin liste2 içindeki
#sayıların alt kümesi olduğunu, yani liste2 içindeki sayıların, liste1 içindeki üçlü listelerden
#hangisiyle birebir eşleştiğini bulmak. Bunun için şöyle bir kod yazabiliriz:

for i in liste1:#liste1 adlı listedeki her bir öğeye i adını verelim
    ortak=[z for z in i if z in liste2]#i içindeki, liste2 ‘de de yer alan her bir öğeye de z adını verelim ve bunları ortak adlı
#bir listede toplayalım.
    if len (ortak)==len(i):#eğer ortak adlı listenin uzunluğu i değişkeninin uzunluğu ile aynıysa
        print(i)