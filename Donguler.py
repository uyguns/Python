# WHILE DONGUSU

a=1
while a<10:
    print(a) 
    a+=1
#1. Python öncelikle a = 1 satırını görüyor ve a ‘nın değerini 1 yapıyor.
#2. Daha sonra a ‘nın değeri 10 ‘dan küçük olduğu müddetçe... (while a < 10) satırını görüyor.
#3. Ardından a ‘nın değerini, 1 artırıyor (a += 1) ve a ‘nın değeri 2 oluyor.
#4. a ‘nın değeri (yani 2 ) 10 ‘dan küçük olduğu için Python ekrana ilgili çıktıyı veriyor.
#5. İlk döngüyü bitiren Python başa dönüyor ve a ‘nın değerinin 2 olduğunu görüyor.
#6. a ‘nın değerini yine 1 artırıyor ve a ‘yı 3 yapıyor.
#7. a ‘nın değeri hâlâ 10 ‘dan küçük olduğu için ekrana yine ilgili çıktıyı veriyor.
#8. İkinci döngüyü de bitiren Python yine başa dönüyor ve a ‘nın değerinin 3 olduğunu görüyor.
#9. Yukarıdaki adımları tekrar eden Python, a ‘nın değeri 9 olana kadar ilerlemeye devam ediyor.
#10. a ‘nın değeri 9 ‘a ulaştığında Python a ‘nın değerini bir kez daha artırınca bu değer 10 ‘a ulaşıyor.
#11. Python a ‘nın değerinin artık 10 ‘dan küçük olmadığını görüyor ve programdan çıkıyor.   

#String örneği    
a=1
while a<10:   #  "a" değişkeninin değeri 10 dan kucuk olduğu sürece...
    print("%s.merhaba"%a)  # 9 defa"merhaba" yı yazdır. "%s" ifaedesi terminalde satir no gösterir.
    a=a+1  #"a" yı bir arttırarak yazdır
print("bitti")

#Fibonacci serisi
#0,1,1,2,3,5,8,13,21,
#a,b
#    c
#   a,b
a,b=0,1
while a<22:
    print(a)
    
    a,b=b,a+b
a,b=0,1
while a<1000:
    print(a)
    a,b=b,a+b

#while dongusunu hesap makinesi icinde kullandık

Giris= """
(1) Topla
(2) Cikar
(3) Carp
(4) Bol
(5) Karesini Hesapla
(6) Karakök Hesapla
"""
print(Giris)

while True:   #Dogru oldugu muddetce  Aksi belirtilmediği sürece çalışmaya devam et!
    soru=input("Lutfen Yapmak istediginiz islemin numarasını girin(Cikmak icin q): ")

    if soru == "q":    #dongunun durması ıcın asagidaki komut yazılır
        print("çıkılıyor...")
        break

    elif soru =="1":
        sayi1=int(input("Toplama islemi icin ilk sayiyi girin:  "))
        sayi2=int(input("Topla islemi icin ikinci sayiyi girin: " ))
        print(sayi1, "+", sayi2,"=",sayi1+sayi2 )

    elif soru =="2":
        sayi3=int(input("Cikarma islemi icin ilk sayiyi girin: "))
        sayi4=int(input("Cikarma islemi icin ikinci sayiyi girin: " ))
        print(sayi3, "-", sayi4,"=",sayi3-sayi4)
    elif soru =="3":
        sayi5=int(input("Carpma islemi icin  ilk sayiyi girin: "))
        sayi6=int(input("Carpma islemi icin ikinci sayiyi girin: "))
        print(sayi5,"*",sayi6,"=",sayi5*sayi6)
    elif soru =="4":
        sayi7=int(input("Bolme islemi icin ilk sayiyi girin:  "))
        sayi8=int(input("Bolme islemi icin ikinci sayiyi girin: "))
        print(sayi7, "/",sayi8,"=",sayi7/sayi8)
    elif soru =="5":
        sayi9=int(input("Karesini almak icin  sayiyi  girin: "))
        print(sayi9,"sayisinin karesi =",sayi9**2)
    elif soru =="6":
        sayi10=int(input("Karekokunu hesaplamak istediginiz sayiyi girin: "))
        print(sayi10,"sayisinni karekoku =",sayi10**0.5)
    else:
        print("yanlıs giris")
        print("Asagidaki seceneklerden birini girin",Giris)

        #Acaba while döngüsünü kullanarak 1 ‘den 100 ‘e kadar olan
#aralıktaki çift sayıları nasıl bulursunuz?

a=1
while a<100:
    a+=1
    if a%2==1:
        print(a)
#a değişkeninin değeri 100 ‘den küçük olduğu müddetçe a değişkeninin değerini
#1 artır. 
# Bu değişkenin değerini her artırışında yeni değerin 2 ‘ye tam bölünüp
#bölünmediğini kontrol et. 
# Eğer a modülüs 2 değeri 0 ise (if a % 2 == 0), yani
#a ‘nın değeri bir çift sayı ise, bu değeri ekrana yazdır.

# FOR DONGUSU

a=("şöği")  
for b in a:   ##for değişken_adı in değişken:
    print(b)   # yapılacak_işlem
    # karakter dizileri, üzerinde döngü kurulabilecek bir veri tipidir.
    #  Ama sayılar öyle  degildir.
a="12345"
for sayilar in a:
    print("Sayilar ")
    #Bu kod hata verir
sayi ="123456"   #Hala karakter dizisi
for sayilar in sayi :   #Hatırlarsanız inisleci bir ögenin bir veri tipi içinde bulunup bulunmadıgını sorguluyordu
    print(int(sayilar))   #int()fonksiyonu yardımıyla bu ögeleri tek tek sayıya çevirdik

#for dongusunun if ile kullanımı

a="123456789"
for sayi in a:
    if int(sayi) > 4 :
        print(sayi)
#a degiskeni içinde sayi  adını verdigimiz herbir öge için:
#eger sayıya dönüstürülmüs sayi degeri 3 ‘ten büyükse: sayi ögesini ekrana
#basma islemi gerçeklestir!
a="ıçöşğü"
parola=input("Lutfen parola gir: ")
for c in parola:  #parola degiskeni icinde c adini verdigimiz bir oge icin
    if c in a:  # eger c ogesi icinde a degiskeninden harf varsa 
        print("Parolada turkce karakter kullanmayin")  #bas
    else:            #yoksa hosgeldin bas
        print("hosgeldin")

#Örnegin kullanıcıya bir parola belirletirken, belirlenecek parolanın 8 karakterden uzun, 3
#karakterden kısa olmamasını saglayalım:

while True:  #Parola dogru oldugu surece
    parola=input("Lutfen yeni parola gir:  ")
    if not parola: #Eger parola bos birakilirsa
        print("Parola bos birakilamaz")
    elif len(parola) > 8 or len(parola) < 3 :  #Eger parolanin uzunlugu 8 karakterden uzun olursa ve 3 karak
        #terden kisa olursa
        print("Parola 8 karakterden cok veya 3 karakterden az olamaz")
    else:   #artik parola kosula uygunsa
        print("Yeni parolaniz",parola)
        break

#eval()fonksiyonu için basit bir kontrol mekanizması kuralım:

izinli_karakterler="123456789+-*/="
print("""
Basit bir hesap makinesi uygulaması.
İşleçler:
+ toplama
- çıkarma
* çarpma
/ bölme
Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23 * 46 yazdıktan sonra
ENTER tuşuna basın""")
while True:
    veri=input("Lutfen isleminizi secin:  ")
    if veri=="q":   #q ya basıldığı takdirde cık
        print("cikiliyor")
        break
    for s in veri:   #for döngüsü kurarak, veri içindeki her bir karakterin
#izinli_karakterler degiskeni içinde yer alıp almadıgını denetliyoruz.
        if s  not in izinli_karakterler:  #eger izinli karakterle dısında giris olursa
            print("Neyin Pesindesin")
            quit()
    hesap=eval(veri)
    print(hesap)

#Range fonksiyonu arasında demektir range for veya while ile birlikte kullanılır.
for i in range (99,115):  #Burada 99 ile 115 arasındaki sayiları bastırdık
    print(i)
#Range formülü:  range(ilk sayi,son sayi)
for i in range (10):
    print(i)  #ilk sayiyi belirtmessek python otomatik olarak 0 dan baslar

# parola alma 
while True:
    parola=input("Lutfen parola girin. ")
if not parola:
    print("Parola bos birakilamaz")

elif len(parola) in range(3,8):  #Parola 3 ile 8 arasında olmalıdır
    print("Yeni parola",parola)
else:
    print("Parola 8 karakterden uzun 3 karakterden kısa olamaz")

#Bu fonksiyonu kullanarak bir döngünün kaç kez çalışacağını da belirleyebilirsiniz

for s in range(3):
    print(s)
    parola=input("Lutfen Parolayı gir:  ")
    if s ==2:
        print("parolayı 3 kez yanlış girdiniz.",
"Lütfen 30 dakika sonra tekrar deneyin!")
  #Gördüğünüz gibi, i değişkeninin başlangıçtaki değeri 0. 
  # Bu değer her döngüde 1 artıyor ve
#bu değişkenin değeri 2 olduğu anda if i == 2 bloğu devreye giriyor.
    elif not parola:
        print("Parola bos bırakılamaz")
    elif len(parola) in range(3,8):
        print("Yeni parola",parola)
    else:
        print("Parola 8 karakterden fazla 3 karakterden az olamaz")

#range(ilk sayi,son sayi,atlama degeri)
#Formüldeki son parametre olan atlama_değeri, aralıktaki sayıların kaçar kaçar 
# ilerleyeceğini  gösterir. Yani:

for s in range(0,10,2):
    print(s)
#cıktı:  0 2 4 6 8
#Gördüğünüz gibi, son parametre olarak verdiğimiz 2 sayısı sayesinde 0 ‘dan 10 ‘a kadar
#  olansayılar ikişer ikişer atlayarak ekrana dökülüyor.
for s in range(10,0,-2): #10 dan geriye 2 ser ser basat
    print(s)   

# pass Deyimi  pas geçme görmezden gelme

sayi=int(input("Lutfen sayi girin: "))
if sayi ==0:
    print("merhaba")
elif sayi<0: #burada girilen sayi eger 0 dan kucukse onu pas geçtik 
    #python görmezden gelecek
    pass
else:
    print(sayi)

#continue deyiminin görevi kendisinden sonra gelen
#her şeyin es geçilip döngünün başına dönülmesini sağlamaktır.


while True:
    s=input("sayı girin: ")
    if s=="iptal":
        break 
    if len(s) <= 3:   
        continue
    print("En fazla 3 haneli sayi girebilirsiniz.")
    

#Eğer kullanıcı tarafından girilen sayı üç haneli veya daha az haneli bir sayı ise, 
# continue ifadesinin etkisiyle: satırı es geçilecek ve döngünün en başına gidilecektir.

#break Deyimi
#Python’da break özel bir deyimdir. Bu deyim yardımıyla, devam eden bir süreci kesintiye
#uğratabiliriz.






