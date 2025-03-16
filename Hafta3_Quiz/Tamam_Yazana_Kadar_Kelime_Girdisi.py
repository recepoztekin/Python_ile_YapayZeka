# "Tamam" yazana kadar girdiğiniz kelimeleri, bir listeye ekleyen uygulama

liste = []
while(True): #sonsuz döngü
  kelime = input("Kelime Girin (Tamam yazarsanız çıkar): ").lower() #hata vermemesi için girilen kelimeyi küçük harfe çevirdik
  if kelime == "tamam": #eğer kelime "tamam"a eşitse 
    break #döngüden çık
  liste.append(kelime)  #girilen değerleri listeye ekle

print("Kelimeler: ",liste) #listeyi yazdır

# Çıktı
# Kelime Girin (Tamam yazarsanız çıkar): ahmet
# Kelime Girin (Tamam yazarsanız çıkar): ali
# Kelime Girin (Tamam yazarsanız çıkar): ayşe
# Kelime Girin (Tamam yazarsanız çıkar): bora
# Kelime Girin (Tamam yazarsanız çıkar): recep
# Kelime Girin (Tamam yazarsanız çıkar): tamam
# Kelimeler:  ['ahmet', 'ali', 'ayşe', 'bora', 'recep']