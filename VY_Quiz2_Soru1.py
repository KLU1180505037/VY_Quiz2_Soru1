
n = int(input("Dizinin boyutu: "))
# kullanıcıdan dizinin elemanlarını al
dizi = []
for i in range(n):
    eleman = input("{}. eleman: ".format(i+1))
    while not eleman.isnumeric():  # sadece sayısal değerler kabul edilir
        eleman = input("Lütfen sadece sayısal değerler giriniz: ")
    dizi.append(int(eleman))

# kullanıcıdan aranacak elemanı al
aranan = input("Aranacak eleman: ")
while not aranan.isnumeric():  # sadece sayısal değerler kabul edilir
    aranan = input("Lütfen sadece sayısal bir değer giriniz: ")
aranan = int(aranan)

# Linear Search 
bulundu = False
for i in range(n):
    if dizi[i] == aranan:
        bulundu = True
        break


if bulundu:
    print("Aranan eleman dizi içinde bulundu.")
else:
    print("Aranan eleman dizi içinde bulunamadı.")
