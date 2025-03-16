# Liste şeklindeki Celsius değerlerin fahrenayt a çevirecek uygulama

celsius = [15, 34, 23, 10, 1] #liste oluşturduk
fahrenayt = [] #boş liste 
for i in celsius: #i değişkeni celsius listesinde gezecek
  f = (i * 1.8) + 32 #her değeri formül ile işlem yapacak, fahrenayt değişkeninde 
  fahrenayt.append(f)
print(fahrenayt)

# Çıktı
# [59.0, 93.2, 73.4, 50.0, 33.8]