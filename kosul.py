#Yas ornegi

a= int(input("lutfen yasini gir: "))

b=13


if a >= b:  
 	print("Hosgeldiniz\t")
elif a < b : 
	print("Programi kullanabilmek icin 13 yasinda olmalisiniz.\nBuyuyunce gel\t")
#Kullanici adi ve parola ornegi	
	ad=input("Kullanici adini girin: ")
parola=input("parolayi girin: ")
toplam=len(ad)+len(parola)
mesaj=("Kullanici adi ve parolaniz '{}' karakterden olusuyor.")

if toplam>10:
	print(mesaj.format(toplam),"\nKullanici adi ve parola 10 karakteri gecmemeli")
else:
	print("sisteme hosgeldiniz")
#cift sayi tek sayi ornegi	
	sayi=int(input("lutfen sayi girin: "))
if sayi %2==0:
	print("cift sayi")
else:
	print("tek sayi")