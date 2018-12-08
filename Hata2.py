#1. örnek
while True:
    try:
        ilk_sayi=int(input("ilk sayiyi girin: "))
        ikinci_sayi=int(input("İkinci sayiyi girin: "))
        print(ilk_sayi/ikinci_sayi)
    except ValueError:
        print( "Lütfen harf girmeyin") 
    except ZeroDivisionError:
        print("Herhangi bir sayının 0'a bölümü tanımsızdır")   

#2.örnek

while True:
    try:
        ilk_sayi=int(input("ilk sayiyi girin: "))
        ikinci_sayi=int(input("İkinci sayiyi girin: "))
        
    except ValueError:
        print("harf girmeyin")
    else:
        try:
            print(ilk_sayi/ikinci_sayi)
        except  ZeroDivisionError:
            print("sıfır girme")

#3. örnek 

while True:
    try:
        ilk_sayi=int(input("ilk sayiyi girin: "))
        ikinci_sayi=int(input("İkinci sayiyi girin: "))
        print(ilk_sayi/ikinci_sayi)
    except ValueError:
        print( "Lütfen harf girmeyin")  
    finally:
        print("calisti")   

#4.örnek
sayi=int(input("sayi girin:")) 
if sayi==25:

    raise ValueError("25 sayısını sevmiyorum")

#6. örnek

while True:
    try:
        ilk_sayi=int(input("ilk sayiyi girin: "))
        ikinci_sayi=int(input("İkinci sayiyi girin: "))
        print(ilk_sayi/ikinci_sayi)
    except  :
        print( "hata oluştu")  
        



    
