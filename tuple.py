#demetlerin ayırıcı özelliği normal parantezler.
demet=("ahmet","mehmet",1,2,2.3)
a="ahmet","mehmet",123.8,2.3#bu da demettir.
print(type(demet))
print(demet)
print(a)
print(type(a))
#Demet oluşturmak için tuple() adlı bir fonksiyondan da yararlanabilirsiniz.
b=tuple("123455678")
print(b)
print(type(b))

#tek öğeli demet tanımlamak

demet=("ahmet")#bu karakter dizesidir.
print(type(demet))
demet=("ahmet",)#virgul isareti demet haline getirir
print(type(demet))

#Demetlerin Öğelerine Erişmek
#listelerle aynıdir
demet=("ahmet","mehmet",1,2,2.3)
print(demet[0])
#demetler değiştirilemez
demet=("ahmet","mehmet",1,2,2.3)
demet[0]="uygun"  #hata veiri değiştirilmez
#demet ekleme
demet="ahmet","mehmet"
demet=demet+("kubra",)#kubra yı ekliyoruz
print(demet)