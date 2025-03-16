# Bir listedeki sadece stringleri döndüren bir döngü oluşturun

liste = [2323, "Ahmet", True, "Mehmet", True, 15, False, ]
for i in liste:
  if type(i) == str:
    print("String kelimeler: ", i)

# Çıktı
# String kelimeler:  Ahmet
# String kelimeler:  Mehmet