#str.maketrans(),translate()

#Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri 
# kullanamıyoruz. Böyle durumlarda, elimizdeki bir metni, cümleyi veya kelimeyi Türkçe
# karakter içermeyecek bir hale getirmemiz gerekebiliyor.

kaynak = "şçöğüıŞÇÖĞÜİ"
hedef = "scoguiSCOGUI"
a=str.maketrans(kaynak,hedef)
metin="Gördüğünüz gibi, “kaynak” adlı karakter dizisi içinde belirttiğimiz bütün harfler “hedef” adlıkarakter dizisi içindeki harflerle tek tek değiştirildi. Böylece Türkçeye özgü karakterleri(‘şçöğüıŞÇÖĞÜİ’) en yakın noktasız benzerleriyle (‘scoguiSCOGUI’) değiştirmiş olduk."
print(metin.translate(a))
print(a)

#Gördüğünüz gibi, “kaynak” adlı karakter dizisi içinde belirttiğimiz bütün harfler “hedef” adlı
# karakter dizisi içindeki harflerle tek tek değiştirildi. Böylece Türkçeye özgü karakterleri
# (‘şçöğüıŞÇÖĞÜİ’) en yakın noktasız benzerleriyle (‘scoguiSCOGUI’) değiştirmiş olduk

#isalpha()

#Bu metot yardımıyla bir karakter dizisinin ‘alfabetik’ olup olmadığını denetleyeceğiz. Peki ‘alfabetik’ ne demek?
#Eğer bir karakter dizisi içinde yalnızca alfabe harfleri (‘a’, ‘b’, ‘c’ gibi...) varsa o karakter dizisi
#için ‘alfabetik’ diyoruz.

a="mehmetuygun"
print(a.isalpha()) #cikti:True

a="mehm3tuy67n"
print(a.isalpha()) #cikti:False

a="mehmet uygun"
print(a.isalpha()) #cikti:False


#isdigit()

#Bu metot da isalpha() metoduna benzer. Bunun yardımıyla bir karakter dizisinin sayısal
#olup olmadığını denetleyebiliriz. Sayılardan oluşan karakter dizilerine ‘sayı değerli karakter
#dizileri’ adı verilir.
a="123445"
print(a.isdigit()) #cikti: True

a="1234ee45"
print(a.isdigit()) #cikti: False

#19.4 isalnum()

#Bu metot, bir karakter dizisinin ‘alfanümerik’ olup olmadığını denetlememizi sağlar.
#Yani sayı ve harflerden oluşan karakter dizilerine alfanümerik karakter dizileri adı verilir.
a="123abc"
print(a.isalnum())#Cikti True

a="123abc**"
print(a.isalnum())#False ciktisi verir

#isdecimal()

#Bu metot yardımıyla bir karakter dizisinin ondalık sayı cinsinden olup olmadığını denetliyoruz.

a="12345"
print(a.isdecimal())#true ciktisi

a="1223.3"
print(a.isdecimal())#false ciktisi

#isidentifier()

#Identifier kelimesi Türkçede ‘tanımlayıcı’ anlamına gelir. Python’da değişkenler, fonksiyon
#ve modül adlarına ‘tanımlayıcı’ denir.
print("1a".isidentifier())  #false
#değişken adı belirlemenin bazı kuralları olduğunu söylemiştik. 
# Buna göre, örneğin, değişken adları bir sayı ile başlayamıyordu. Dolayısıyla şöyle 
# bir değişken adı belirleyemiyoruz
print("a1".isidentifier())#true

#isnumeric()  isdigit ile ayni
#Bu metot bir karakter dizisinin nümerik olup olmadığını denetler. Yani bu metot yardımıyla
#bir karakter dizisinin sayı değerli olup olmadığını denetleyebiliriz:

a="12345"
print(a.isnumeric())#true
print(a.isdigit())#true
a="asd123"
print(a.isnumeric())#False

#isspace()

#Bu metot yardımıyla bir karakter dizisinin tamamen boşluklardan oluşup oluşmadığını
#denetleyebiliriz. Eğer karakter dizimiz boşluklardan oluşuyorsa bu metot True çıktısı verecek,
#ama eğer karakter dizimizin içinde bir tane bile boşluk harici karakter varsa bu metot False çıktısı verecektir


a="  "
print(a.isspace())#true
a=""
print(a.isspace())#false
a="a  "
print(a.isspace())#false

#isprintable()

#bir karakterin basılabilen bir karakter mi yoksa basılmayan bir karakter mi olduğunu söyler

a="as"
print(a.isprintable())#true

a="\n"
print(a.isprintable())#false
#son örnek print de cikmadigi icin false verir.yani yazdirilmaz.


