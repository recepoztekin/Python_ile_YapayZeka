# Kullanıcı bir kelime girecek, sonu "miş" le mi bitiyor kontrol edilecek. mesaj yazdıracaksınız.

print("Bir kelime girin: ")
kelime = input()
if kelime.endswith("MİŞ"):
  print("Kelime 'miş' ile bitiyor.")
elif kelime.endswith("miş"):
  print("Kelime 'miş' ile bitiyor.")
else:
  print("Kelime 'miş' ile bitmiyor.")