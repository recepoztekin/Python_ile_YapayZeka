# Dörtgen, üçgen veya dairenin Alan hesabı. Kullanıcıdan en boy değerleri alınacak ve alan hesaplanacak.

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