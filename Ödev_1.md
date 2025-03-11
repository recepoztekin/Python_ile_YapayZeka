### Soru 1: Dörtgen, üçgen veya dairenin Alan hesabı. Kullanıcıdan en boy değerleri alınacak ve alan hesaplanacak.

```py
print("---- ALAN HESAPLAMA ----")
print("Hangi alanı hesaplamak istiyorsunuz ?")
print("1-Dörtgen Alanı")
print("2-Üçgen Alanı")
print("3-Daire Alanı")

secim = int(input("Seçiminiz: "))
if secim == 1:
  en = int(input("En: "))
  boy = int(input("Boy: "))
  print("Alan: ", en*boy)
elif secim == 2:
  en = int(input("Taban: "))
  boy = int(input("Yükseklik: "))
  print("Alan: ", en*boy/2)
elif secim == 3:
  r = int(input("Yarıçap: "))
  print("Alan: ", 3.14*r*r)
else :
  print("Seçimler dışında seçim yapıldı !")
```
#### Çıktı
```
---- ALAN HESAPLAMA ----
Hangi alanı hesaplamak istiyorsunuz ?
1-Dörtgen Alanı
2-Üçgen Alanı
3-Daire Alanı
Seçiminiz: 2
Taban: 4
Yükseklik: 3
Alan:  6.0
```
### Soru 2. Girilen "gün", "saat", "dakika" ve "saniye" değerine göre, toplam saniyeyi hesaplayan bir uygulama yapınız.:


```py
print("GÜN, SAAT, DAKİKA, SANİYE HESAPLAMA")
gun = float(input("Gün: "))
saat = float(input("Saat: "))
dakika = float(input("Dakika: "))
saniye = float(input("Saniye: "))

print(f"Toplam saniye: ", gun*24*60*60 + saat*60*60 + dakika*60 + saniye)
```
#### Çıktı 
```
GÜN, SAAT, DAKİKA, SANİYE HESAPLAMA
Gün: 1
Saat: 0
Dakika: 0
Saniye: 0
Toplam saniye:  86400.0
```
### Soru 3. Vücut Kitle Endeksini hesaplayan uygulamayı yapın (ağırlığın(kg) boyun karesine (m)bölümü)
````py
print("Vücut Kitle Endeksi")
boy = float(input("Boy Girin: "))
kilo = float(input("Kilo Girin: "))
print("Vücut Kitle İndeksiniz: ", kilo/(boy*boy))
````
#### Çıktı 
````
Vücut Kitle Endeksi
Boy Girin: 1.76
Kilo Girin: 63
Vücut Kitle İndeksiniz:  20.33832644628099
````
### Soru 4. Restoran. Kullanıcı "pizza", "burger" veya "salata" seçeneklerinden birini seçecek. seçtiği menünün fiyatını bir değişkene atayacak. Bu fiyata %15 vergi oranı uygulayacak, %10 bahşiş ekleyecek ve toplam fiyat yazdırılacak.
````py
print("--- Menü Seçin ---")
print("1- Pizza --> 200 TL")
pizza = 200
print("2- Burger --> 170 TL")
burger = 170
print("3- Salata --> 110 TL")
salata = 110

print("---------------------")

giris = int(input("Seçiminiz: "))

if giris == 1:
  print("Fiyat: ", pizza + pizza * 0.15 + pizza * 0.1)
elif giris == 2:
  print("Fiyat: ", burger + burger * 0.15 + burger * 0.1)
elif giris == 3:
  print("Fiyat: ", salata + salata * 0.15 + salata * 0.1)
else :
  print("Hatalı seçim yaptınız !")
````
#### Çıktı
````
--- Menü Seçin ---
1- Pizza --> 200 TL
2- Burger --> 170 TL
3- Salata --> 110 TL
----------------------
Seçiminiz: 3
Fiyat:  137.5
````

### Soru 5. feet'i inch, yard, mil e çevirin.
```py
print("Feet cinsinden değer girin: ")
deger = float(input())
inch = deger * 12
yard = deger * 0.3333333
mil = deger * 0.000189394
print(f"Girdiğiniz '{deger}' Feet değerinin 'inch' cinsinden dönüşümü: ", inch)
print(f"Girdiğiniz '{deger}' Feet değerinin 'yard' cinsinden dönüşümü: ", yard)
print(f"Girdiğiniz '{deger}' Feet değerinin 'mil' cinsinden dönüşümü: ", mil)
```
#### Çıktı
```
Feet cinsinden değer girin: 
5280
Girdiğiniz '5280.0' Feet değerinin 'inch' cinsinden dönüşümü:  63360.0
Girdiğiniz '5280.0' Feet değerinin 'yard' cinsinden dönüşümü:  1759.999824
Girdiğiniz '5280.0' Feet değerinin 'mil' cinsinden dönüşümü:  1.00000032
```

### Soru 6. Kullanıcı bir kelime girecek, bu kelime "tr" ifadesi içeriyorsa "kelime tr ifadesi içeriyor" mesajı, içermiyorsa "tr ifadesi içermiyor" mesajı versin.
```py
print("Bir kelime girin: ")
kelime = input().lower()
if "tr" in kelime:
  print("Kelime 'tr' ifadesi içeriyor.")
else :
  print("Kelime 'tr' ifadesi içermiyor.")
```
####Çıktı
```
Bir kelime girin: 
TRAŞ
Kelime 'tr' ifadesi içeriyor.
```

### 7. Kullanıcıdan iki kelime girdisi isteyeceksiniz. ikisinin aynı kelime olup olmadığını kıyaslayacaksınız.(kullanıcı ister büyük harfle girsin ister küçük. -lower)
```py
print("2 adet kelime girinzi: ")
kelime1 = input().lower()
kelime2 = input().lower()
if kelime1 == kelime2:
  print("Kelimeler aynı !")
else:
  print("Kelimeler farklı !")
```
#### Çıktı
```
2 adet kelime girinzi: 
NasılSıN
nasılsın
Kelimeler aynı !
```

### Soru 8. Herhangi bir sayı girsin. Girdiği sayının 100 den büyük, küçük veya eşit olduğu mesajı verilsin. (tiplere dikkat)
```py
sayi = float(input("Herhangi bir sayı girin: "))

if float(sayi) < 100:
  print(f"Girdiğiniz {sayi} sayısı 100'den küçük")
elif float(sayi) == 100:
  print(f"Girdiğiniz {sayi} sayısı 100'e eşit")
else:
  print(f"Girdiğiniz {sayi} sayısı 100'den büyük")
```
#### Çıktı
```
Herhangi bir sayı girin: 454546
Girdiğiniz 454546.0 sayısı 100'den büyük
```


### Soru 9. Kullanıcı yaşını girecek, 12 yaşa kadar- Çocuk, 13-19 yaş - Ergen, 20-30 yaş Genç yetişkin, 30-64 yaş Yetişkin, 64 yaş üzeri olgun.
```py
yas = int(input("Yaşınızı Girin: "))
if yas > 0 and yas <= 12:
  print("Çocuk")
elif yas >= 13 and yas <= 19:
  print("Ergen")
elif yas > 19 and yas < 30:
  print("Genç Yetişkin")
elif yas >= 30 and yas <= 64:
  print("Yetişkin")
elif yas > 64:
  print("Olgun")
else:
  print("Hatalı yaş girdiniz !")
```
#### Çıktı
```
Yaşınızı Girin: -9999
Hatalı yaş girdiniz !
```


### Soru 10. Kullanıcı bir kelime girecek, sonu "miş" le mi bitiyor kontrol edilecek. mesaj yazdıracaksınız.
```py
print("Bir kelime girin: ")
kelime = input()
if kelime.endswith("MİŞ"):
  print("Kelime 'miş' ile bitiyor.")
elif kelime.endswith("miş"):
  print("Kelime 'miş' ile bitiyor.")
else:
  print("Kelime 'miş' ile bitmiyor.")
```
#### Çıktı
```
Bir kelime girin: 
miş
Kelime 'miş' ile bitiyor.
```


### Soru 11. Hesap makinesi. Kullanıcıdan hangi işlemi yapmak istediği metin olarak alınacak. "bol" "carp" gibi.
```py
islem = input("İşleminizi girin (topla,çıkar,çarp,böl): ").lower()
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

if islem == "topla":
  print(f"{sayi1} + {sayi2} = {sayi1+sayi2}")
elif islem == "çıkar":
  print(f"{sayi1} - {sayi2} = {sayi1-sayi2}")
elif islem == "çarp":
  print(f"{sayi1} * {sayi2} = {sayi1*sayi2}")
elif islem == "böl":
  if sayi2 == 0 or sayi1 == 0:
    print("Hatalı işlem bölme de 0 kullanılmaz !")
  elif True:
    print(f"{sayi1} / {sayi2} = {sayi1/sayi2}")

else:
  print("Hatalı işlem yaptınız !")
```
#### Çıktı
```
İşleminizi girin (topla,çıkar,çarp,böl): BÖL
Birinci sayıyı girin: 4
İkinci sayıyı girin: 2
4.0 / 2.0 = 2.0
```


### Soru 12. Uygulama Aslandan kaçma oyunu Bir aslanla karşılaştınız ne yapardınız?

1-Kaçardım

2-Ağaca tırmanırdım

1 seçeneği seçilirse

1-Nehire doğru

2-Otoyola doğru

eğer burda

1 seçilirse aslana yakalanacak,

2 seçilirse aslandan kaçabilecek.

2 seçeneği seçilirse

1-En yakın 2-Biraz daha uzak ama daha uzun

eğer burada 1 seçeneği seçilirse aslan sizi yakalayacak.

```py
print("--- ASLANDAN KAÇMA OYUNU ---")
print("Bir aslanla karşılaştınız ne yapardınız ?")
print("1- Kaçardım")
print("2- Ağaca Tırmanırdım")
print("--------------------------")
secim = input("Seçiminiz: ")

if secim == "1":
  print("1- Nehire Doğru")
  print("2- Otoyola Doğru")
  secim = input("Seçiminiz: ")
  if secim == "1":
       print("Aslan sizi yakaladı !!!")
  elif secim == "2":
       print("Aslandan kaçtınız, Tebrikler !")
  else:
      print("Hatalı seçim Tekrar deneyin !")
elif secim == "2":
  print("1- En Yakın Ağaç")
  print("2- Biraz Daha Uzak Ama Daha Uzun Ağaç")
  secim = input("Seçiminiz: ")
  if secim == "1":
    print("Aslan sizi yakaladı !!!")
  elif secim == "2":
    print("Aslandan kaçtınız, Tebrikler !")
  else:
    print("Hatalı seçim Tekrar deneyin !")

else:
  print("Hatalı seçim Tekrar deneyin !")
```
#### Çıktı
```
--- ASLANDAN KAÇMA OYUNU ---
Bir aslanla karşılaştınız ne yapardınız ?
1- Kaçardım
2- Ağaca Tırmanırdım
--------------------------
Seçiminiz: 2
1- En Yakın Ağaç
2- Biraz Daha Uzak Ama Daha Uzun Ağaç
Seçiminiz: 2
Aslandan kaçtınız, Tebrikler !
```
