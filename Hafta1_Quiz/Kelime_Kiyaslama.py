# Kullanıcıdan iki kelime girdisi isteyeceksiniz. 
# İkisinin aynı kelime olup olmadığını kıyaslayacaksınız.(kullanıcı ister büyük harfle girsin ister küçük. -lower)

print("2 adet kelime girinzi: ")
kelime1 = input().lower()
kelime2 = input().lower()
if kelime1 == kelime2:
  print("Kelimeler aynı !")
else:
  print("Kelimeler farklı !")
