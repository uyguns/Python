# open dosya acma islemini yapar
#  dosya=open("dosya ismi","w-r-a ")
#   "w"  dosya yoksa dosyayı yaratmayı sağlar.dosya varsa eski dosyayı siler
#   yenisini açar
#  "r" read okuma modu .dosyayı okumamızı sağlar.ancak değişiklik yapamayız.
# "a"  modu append modu. var olan dosyanın  içindeki
#bilgileri değiştirmemmizi sağlar.yoksa aynı zamanda dosya oluşturur.

dosya=open("yazılım.txt","a")
dosya.write("yazılım denemeleri")
print(dosya)

dosya=open("yazılım.txt","a")
dosya.write("yazılım denemeleri")
print(dosya)

#dosya yazma
dosya=open("yazılım.txt","w",encoding="utf-8")
dosya.write("Ahmet Özbudak : 0533 123 23 34  Mehmet Sülün : 0532 212 22 22  Sami Sam : 0542 333 34 34")
print(dosya)

#dosya okuma
dosya=open("yazılım.txt","r")
print(dosya.read())#tumunu okur.
print(dosya.readline()) #ilk satırı okur
print(dosya.readlines()) #liste biçiminde okur

#otamatik dosya kapatma
with open("yazılım.txt") as dosya:
    print(dosya.read())
#dosyaları ileri geri sarmak

#dosyaları tekrar okumak için    seek() metodundan yararlanırız.

dosya=open("yazılım.txt","r")
print(dosya.read())
dosya.seek(0)
print(dosya.readline())
dosya.seek(0)
print(dosya.readlines())
#dosyanın hangi byte konumunda olduğunu öğrenmek için  sonuç 88 byte nin üzeirndeyiz.
print(dosya.tell())

#dosyalarda değişiklik yapmak  "a" dosyanın sonuna ekleme
dosya=open("yazılım.txt","a")
dosya.write("ali cengiz oyunları")
print(dosya)


#şöyle yazmaya dikkat edelim
with open("yazılım.txt","a") as dosya:
    dosya.write("hello world")

with open("yazılım.txt") as dosya:
    print(dosya.read())


liste=open("liste.txt","w")
liste.write("Ahmet Özbudak : 0533 123 23 34\n Mehmet Sülün : 0532 212 22 22\n Sami Sam : 0542 333 34 34\n Selin Özden : 0212 222 22 22")
print(liste)

#dosyaların başında değişiklik yapmak


with open("liste.txt","r+") as liste:  #r+  dosyayı hem yazma hemde okuma modunda açar
    veri=liste.read() #yazmadığımız takdir de ilk satır silkinir onun yerine eklenir.
    liste.seek(0)  #başa doner
    liste.write("Sedat Köz : 0322 234 45 45\n"+veri)# + veri önceden var olan bilgileri ekler

with open("liste.txt","r+") as liste:
    print(liste.read())

liste=open("yazilim.txt")
with open("yazilim.txt","r+") as liste:
    liste.seek(0)#  kacıncı karakterden başlayacığını söyleyebiliriz.
    liste.seek(10)
    print(liste.read(5))# sadece bes karakter alır. 

liste=open("yazilim.txt")
with open("yazilim.txt","r+") as liste:
    str1=liste.read(5) #5 karakter okudu
    liste.seek(15)  #karaktere geri giiti
    str2=liste.read(5)# 5 karakter okudu
    print(str1,str2)

#dosyaların ortasında değişiklik yapma
with open("liste.txt","r+") as liste:
    veri=liste.readlines()#listeye çeviriyoruz.çünkü liste değiştiilebilir.
    veri.insert(2,"merhaba dünyalılar okullar tatil\n") #2. satıra ekle
    liste.seek(0) #başa don
    liste.writelines(veri)# butun verileri dosyaya yazıyoruz.  writelines dosyaya liste tipinde veri yazmamıza izin verir

#okuma faslı yukarıdaki ile karıştırma
with open("liste.txt","r+") as liste:
    print(liste.read())