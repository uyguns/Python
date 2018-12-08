import os  #pythonda hangi dizinde olduğumuzu öğreniriz.
os.getcwd

import keyword
keyword.kwlist #hangi kelimeler değişken adı olamaz


#etkileşimli kabuktan çıkma 
import sys;sys.exit()

import sys
sys.stdout

#Çıktı  _io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>

#Python’da modüller import komutu ile içe aktarılır. Örneğin sys adlı modülü içe aktarmak 
# için import sys komutunu veriyoruz.
#sys modülü içindeki değişkenlere bir örnek stdout ; fonksiyonlara örnek ise exit() fonksiyonudur.
#Bir modül içindeki bu değişken ve fonksiyonlara ‘modül_adı.değişken_ya_da_fonksiyon’ formülünü kullanarak erişebiliriz.

#sys.stdout’u Kalıcı Olarak Değiştirmek
import sys
f=open("/home/uygun/Masaüstü/deneme.txt","w")
sys.stdout=f
print("deneme metni",flush=True)


#21² yazımının açılımı  21**2 dir  karekök ise 0.5  ile hesaplanır.
#print(144**0.5) 144 karekökü hesaplanır


veri1=input("Karakökünü Hesaplamakistediğmiz sayi: ")
karekök=int(veri1)**0.5
print(veri1,"sayisinin karakökü",karekök)
veri2=input("Karakökünü Hesaplamak istediğimiz sayi")
kare=int(veri2)**0.5
print(veri2,"sayisinin karekökü",kare)



#SESLİ VE SESSİZ HARFLERİ AYIRT ETME ÖRNEK

Sesli_Harfler="aeıioöuü"
Sessiz_Harfler= "bcçdfgğhjklmnprsştvyz"
sesliler=""
sessizler=""
cumle=input("Lutfen cumleyi giriniz:  ")
for harf in cumle:
    if harf in Sesli_Harfler:
        if harf not in sesliler:
            sesliler+=harf
    elif harf in Sessiz_Harfler:
        if harf not in sessizler:
            sessizler+=harf
    else:
        pass
print("cumle karakter uzunlugu: ",len(cumle))
print("cumledeki sesliharfler: ",sesliler)
print("cumledeki sessiz harfler: ",sessizler)

