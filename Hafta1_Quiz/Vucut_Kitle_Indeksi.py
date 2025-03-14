# Restoran. Kullanıcı "pizza", "burger" veya "salata" seçeneklerinden birini seçecek. 
# Seçtiği menünün fiyatını bir değişkene atayacak. Bu fiyata %15 vergi oranı uygulayacak, %10 bahşiş ekleyecek ve toplam fiyat yazdırılacak.

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
