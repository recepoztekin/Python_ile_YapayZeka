# Tahmin oyunu "from random import randint" randint(0, 100)

from random import randint
hedef = randint(0,100)
tahmin = -1

print("--- Tahmin Oyunu ---")
while tahmin != hedef:
  tahmin = int(input("Tahmininiz: "))

  if tahmin < hedef:
    print("Daha büyük bir sayı girin.")

  elif tahmin > hedef:
    print("Daha küçük sayı girin.")

  else:
    print("Tebrikler! Doğru tahmin.")

# Çıktı
# --- Tahmin Oyunu ---
# Tahmininiz: 50
# Daha büyük bir sayı girin.
# Tahmininiz: 75
# Daha büyük bir sayı girin.
# Tahmininiz: 90
# Daha küçük sayı girin.
# Tahmininiz: 80
# Daha küçük sayı girin.
# Tahmininiz: 76
# Tebrikler! Doğru tahmin.