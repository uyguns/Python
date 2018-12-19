tahta=[["_ _ _","_ _ _","_ _ _"],
       ["_ _ _","_ _ _","_ _ _"],
       ["_ _ _","_ _ _","_ _ _"]]
print("\n"*15)#oyun tahtası içinde boş alan yaratmak  icin 15 Adet yeni satir karakteri bastık ekrana

for i in tahta:  #Bu  döngünün amacı tahta adlı listedeki“__”öğelerini düzgün bir şekilde oyuncuya gösterebilmek
    print("\t".expandtabs(30),*i ,end="\n"*2)
    
#Oyun tahtasının, ekranı (yaklaşık olarak  da olsa) ortalamasını istiyoruz. O yüzden, tahta öğelerine soldan girinti verebilmek için
#print() fonksiyonunun ilk parametresini "\t".expandtabs(30) şeklinde yazdık
#.expandtabs metodunu  kullanarak sekme (TAB) karakterlerini genişletebiliyorduk. Burada da “\t” karakterini
#bu metot yardımıyla genişleterek liste öğelerini sol baştan girintiledik.
#*i karakteri listeyi  değil listenin içindekileri gösterir

#tahta adlı liste içindeki iç içece geçmiş listelerin her birinin sonuna ikişer adet “\n” karakteri yerleştirerek, çıktıdaki satırlar
#arasında yeterli miktarda aralık bıraktık. Eğer oyun tahtasındaki satırların biraz daha aralıklı
#olmasını isterseniz bu parametredeki 2 çarpanını artırabilirsiniz. Mesela: end="\n"*3

#Şimdi yapmamız gereken şey, oyundaki kazanma ölçütlerini belirlemek.
#Dediğim gibi, kodların bu bölümünde, hangi durumda oyunun biteceğini ve kazananın kim
#olacağını tespit edebilmemiz gerekiyor. Mesela oyun sırasında şöyle bir görüntü ortaya
#çıkarsa hemen oyunu durdurup “O KAZANDI!” gibi bir çıktı verebilmemiz lazım:

kazanma_olcutleri=[[[0, 0], [1, 0], [2, 0]],
                   [[0, 1], [1, 1], [2, 1]],
                   [[0, 2], [1, 2], [2, 2]],
                   [[0, 0], [0, 1], [0, 2]],
                   [[1, 0], [1, 1], [1, 2]],
                   [[2, 0], [2, 1], [2, 2]],
                   [[0, 0], [1, 1], [2, 2]],
                   [[0, 2], [1, 1], [2, 0]]]
            
x_durumu=[]#Bu değişkenler sırasıyla X işaretinin ve O işaretinin oyun içinde aldıkları konumlarıkaydedecek
o_durumu=[]

#Gördüğünüz gibi, oyunda iki farklı işaret var: X ve O. Dolayısıyla oynama sırası sürekli
#olarak bu iki işaret arasında değişmeli. Mesela oyuna 0 işareti ile başlanacaksa, 0 işaretinin
#yerleştirilmesinden sonra sıranın X işaretine geçmesi gerekiyor. X işareti de yerleştirildikten
#sonra sıra tekrar 0 işaretine geçmeli ve oyun süresince bu böyle devam edebilmeli.
#Bu sürekliliği sağlamak için şöyle bir kod yazabiliriz:
sira=1
while True:
    if sira % 2==0:
        isaret="X".center(3)
    else:
        isaret="O".center(3)
    
    print()
    print("ISARET: {}\n".format(isaret))
#Burada sayıların tek veya çift olma özelliğinden yararlanarak X ve O işaretleri arasında geçiş
#yaptık. Önce sıra adlı bir değişken tanımlayıp bunun değerini 1 olarak belirledik. while
#döngüsünde ise bu değişkenin değerini her defasında 1 artırdık. Eğer sayının değeri çiftse
#işaret X; tekse O olacak. Bu arada X ve O adlı karakter dizilerini, center() metodu yardımıyla
#ortaladığımıza dikkat edin.

    x=input("Yukaridan Asagiya[1,2,3]: ".ljust(30))
    if x=="q":
        break
    y=input("Soldan saga[1,2,3]: ".ljust(30))
    if y=="q":
        break

    x=int(x)-1
    y=int(y)-1
#Burada X veya O işaretlerini tahta üzerinde uygun yerlere yerleştirebilmek için kullanıcının konum bilgisi girmesini istiyoruz
#Burada ljust() metotlarını, kullanıcıya gösterilecek verinin düzgün bir şekilde hizalanması amacıyla kullandık.
#Eğer kullanıcı x veya y değişkenlerinden herhangi birine “q” cevabı verirse oyundan çıkıyoruz.
#O yüzden mesela kullanıcı 1 sayısını
#girdiğinde Python’ın bunu 0 olarak algılamasını sağlamamız gerekiyor. Bunun için x ve y
#değerlerinden 1 çıkarıyoruz.

    print("\n"*15)#15 ADET SATIR BASI KARAKTERİ BASIYORUZ.
    
    if tahta[x][y]=="_ _ _":
#BU KOD hali hazırda bir konumun bosmu dolomu oldugunu tespit etmemizi sağlar
#ğer bakılan konumda “___” işareti varsa orası boş demektir.
        tahta[x][y]=isaret
        if isaret=="X".center(3):#eger ______ yoksa x o isaretlerinden birini koyarız
            x_durumu += [[x,y]]
        elif isaret=="O".center(3):#girdigimiz 0 ve x i ortalıyoruz.
            o_durumu += [[x,y]]
        sira += 1
    else:
        print("\n ORASI DOLU! TEKRAR DENEYİN\n")#____yoksa orası dolu uyarısı veiryoruz

    for i in tahta:
        print("\t".expandtabs(30),*i,end="\n"*2)#oyun tahatasının son durumunu göstermek için kullanıyoruz.

    #oyunu kimin kazandığını belirleme
    for i in kazanma_olcutleri:
        o=[z for z in i if z in o_durumu]
        x=[z for z in i if z in x_durumu]

    if len (o)==len(i):
        print("O KAZANDI!")
        quit()
    if len(x)==len(i):
        print("X KAZANDI!")
        quit()

#Bu kodlar içindeki en önemli öğeler o ve x adlı değişkenlerdir. Burada, o_durumu
#veya x_durumu adlı listelerdeki değerlerle kazanma_ölçütleri adlı listedeki değerleri
#karşılaştırarak, ortak değerleri o veya x değişkenlerine yolluyoruz. Eğer ortak öğe sayısı 3’e
#ulaşırsa (if len(o) == len(i): veya if len(x) == len(i):), bu sayıyı yakalayan ilk işaret
#hangisiyse oyunu o kazanmış demektir.