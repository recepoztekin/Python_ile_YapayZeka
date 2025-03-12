# Kullanıcı bir kelime girecek, bu kelime "tr" ifadesi içeriyorsa "kelime tr ifadesi içeriyor" mesajı, içermiyorsa "tr ifadesi içermiyor" mesajı versin.

print("Bir kelime girin: ")
kelime = input().lower()
if "tr" in kelime:
  print("Kelime 'tr' ifadesi içeriyor.")
else :
  print("Kelime 'tr' ifadesi içermiyor.")
