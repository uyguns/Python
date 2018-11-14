# Bool islecleri
#and   ve anlami
#or       veya anlami
#not


#and islecinde kullanici ve parola d=gerleri mutlaka true olamsi gerekir

kullanici=input("kullanici adini gir: ")
parola=input("parolayi gor:  ")
if kullanici=="mehmet" and parola=="1234":# esas yazilimi if bool(kulanici== "mehmet" and parola=="1234"): dur
		print("hosgeldiniz")
else:
		print("kullanici adi veya parola yanlis")
	# Not alma	
	
		x=int(input("notunuz:  "))
if x >100 or x<0:
			print("boyle bir not yok")
elif x >= 85 and x<=100:	
	print("AA")
elif x<85 and x>=70:
	print("BB")
elif x<70 and x>=55:
	print("CC")
		
#or isleci
# or  islecinde asagidaki  kullanici ve parolanin bir tanesinin dogru olm!si yeterlidir.


kullanici=input("kullanici adini gir: ")
parola=input("parolayi gor:  ")
if kullanici=="mehmet" or parola=="1234":# esas yazilimi if bool(kulanici== "mehmet" and parola=="1234"): dur
		print("hosgeldiniz")
else:
		print("kullanici adi veya parola yanlis")
		
#not    degildir anlamina gelir
#Bu işleç, özellikle kullanıcı tarafından bir değişkene veri girilip girilmediğini denetlemek için kullanılabilir. Örneğin

parola=input("parola gir :")
if not parola:
	print("parola bos bir!kilamaz")
#yukaridaki ornekte suna benzer sorular soruyoruz.

parola = ""
bool(parola) #parola boş bırakılmamış, değil mi?

False #Hayır, parola boş bırakılmış.

bool(not parola) #parola boş bırakılmış, değil mi?

True #Evet, parola boş bırakılmış