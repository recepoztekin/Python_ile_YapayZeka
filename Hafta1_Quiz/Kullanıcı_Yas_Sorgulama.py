# Kullanıcı yaşını girecek, 12 yaşa kadar- Çocuk, 13-19 yaş - Ergen, 20-30 yaş Genç yetişkin, 30-64 yaş Yetişkin, 64 yaş üzeri olgun.

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
