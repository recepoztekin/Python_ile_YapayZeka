# Birşeyler yazın: tAmAm

isim = ["Recep", "Ahmet", "Ali", "Ali", "Recep", "Recep", "Bora"]
isim2 = []
for i in isim: #i parametresi isim'in içinde dönecek
  if i not in isim2:
    isim2.append(i)
print(isim2)

# Çıktı
# ['Recep', 'Ahmet', 'Ali', 'Bora']