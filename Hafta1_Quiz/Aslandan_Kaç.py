# Uygulama Aslandan kaçma oyunu Bir aslanla karşılaştınız ne yapardınız?
# 1-Kaçardım

# 2-Ağaca tırmanırdım

# 1 seçeneği seçilirse

# 1-Nehire doğru

# 2-Otoyola doğru

# eğer burda

# 1 seçilirse aslana yakalanacak,

# 2 seçilirse aslandan kaçabilecek.

# 2 seçeneği seçilirse

# 1-En yakın 2-Biraz daha uzak ama daha uzun

# eğer burada 1 seçeneği seçilirse aslan sizi yakalayacak.

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