# Herhangi bir sayı girsin. Girdiği sayının 100 den büyük, küçük veya eşit olduğu mesajı verilsin. (tiplere dikkat)

sayi = float(input("Herhangi bir sayı girin: "))

if float(sayi) < 100:
  print(f"Girdiğiniz {sayi} sayısı 100'den küçük")
elif float(sayi) == 100:
  print(f"Girdiğiniz {sayi} sayısı 100'e eşit")
else:
  print(f"Girdiğiniz {sayi} sayısı 100'den büyük")
