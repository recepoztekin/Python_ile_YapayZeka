#Girdiğiniz kelimedeki belirli harfleri yazdıran bir uygulama

kelime = input("Kelime Girin: ").lower()
harfler = input("Görmek istediğiniz harf: ")
for harf in kelime:
    if harf in harfler:
      print(f"'{harf}'harfi {harfler} ile eşleşiyor.")
    else:
      print(f"'{harf}'harfi {harfler} ile eşleşmiyor.")

# Çıktı
# Kelime Girin: naber
# Görmek istediğiniz harf: a
# 'n'harfi a ile eşleşmiyor.
# 'a'harfi a ile eşleşiyor.
# 'b'harfi a ile eşleşmiyor.
# 'e'harfi a ile eşleşmiyor.
# 'r'harfi a ile eşleşmiyor.