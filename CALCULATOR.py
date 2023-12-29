import math
def toplama(*sayilar): # *... , bir Python fonksiyonunda değişken sayıda argüman almak için
    return sum(sayilar)

def cikarma(*sayilar):
    result = sayilar[0]
    for sayi in sayilar[1:]:
        result -= sayi
    return result

def carpma(*sayilar):
    result = 1
    for sayi in sayilar:
        result *= sayi
    return result

def bolme(*sayilar):
    result = sayilar[0]
    for sayi in sayilar[1:]:
        result /= sayi
    return result

def kalan_bulma(x, y):
    if y != 0:
        return x % y
    else:
        return "Hata! Payda sıfır olamaz."
def faktoriyel(x):
    if x < 0:
        return "Negatif sayıların faktöriyeli tanımsızdır."
    elif(x not in range(0, 1559)):
        return f"Hata! {1558} sayısından büyük sayıların faktöriyeli hesaplanamaz."
    else:
        return math.factorial(x)

def us_alma(x, y):
    return x ** y


while True:
    print("Yapmak istediğiniz işlemi seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Kalan Bulma")
    print("6. Faktöriyel Hesabı")
    print("7. Üs Alma")
    print("8. Çıkış")

    secim = input("Seçiminiz (1-8): ")

    if secim == '8':
        print("Çıkılıyor...")
        break

    if secim not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        print("Geçersiz bir seçim. Lütfen 1 ile 8 arasında bir sayı girin.")
        continue

    if secim == '7':
        sayi = float(input("Bir sayı girin: "))
        diger_sayi = float(input("Üs değerini girin: "))
        sonuc = us_alma(sayi, diger_sayi)
        print("Sonuç:", sonuc)
    elif secim == '6':
        x = float(input("Bir sayı girin: "))
        sonuc = faktoriyel(int(x))
        print("Sonuç:", sonuc)
    elif secim == '5':
        sayi = float(input("Bir sayı girin: "))
        diger_sayi = float(input("Mod alınacak sayıyı girin: "))
        sonuc = kalan_bulma(sayi, diger_sayi)
        print("Sonuç:", sonuc)
    else:
        sayilar = [float(x) for x in input("Sayıları aralarında boşluk bırakarak girin: ").split()]

        if not sayilar:
            print("Hata: En az bir sayı girmelisiniz.")
            continue

        if secim == '1':
            sonuc = toplama(*sayilar)
            print("Sonuç: {}".format(sonuc))
        elif secim == '2':
            sonuc = cikarma(*sayilar)
            print("Sonuç: {}".format(sonuc))
        elif secim == '3':
            sonuc = carpma(*sayilar)
            print("Sonuç: {}".format(sonuc))
        elif secim == '4':
            sonuc = bolme(*sayilar)
            print("Sonuç: {}".format(sonuc))
