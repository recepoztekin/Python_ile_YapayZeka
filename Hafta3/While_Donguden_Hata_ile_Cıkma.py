# While döngüsü yine bir döngü 5 kere dönmesi gerekirken 3. hakkında yanan - döngüden çıkan ve while döngüsünde de çıkan bir uygulama yazın

sayi = 0
while sayi <= 5:
  if sayi == 3:
    print(f"Döngü {5} defa dönmesi gerekirken {sayi}. hakkında çıktı.")
    break
  
  else:
    print(f"Döngü {sayi}")
  sayi+=1

# Çıktı
# Döngü 0
# Döngü 1
# Döngü 2
# Döngü 5 defa dönmesi gerekirken 3. hakkında çıktı.