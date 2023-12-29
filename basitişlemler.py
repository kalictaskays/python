#simple calculator
while True:
    operator = input("Bir operatör seçimi yapınız (+ - * /):")

    if operator in ("+", "-", "*", "/"):
        num1 = float(input("ilk sayı:"))
        num2 = float(input("İkinci sayı:"))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:  # Bölme işlemi için sıfıra bölme hatasını kontrol et
                result = num1 / num2
            else:
                print("Hata: İkinci sayı sıfır olamaz.")
                continue  # Hatalı durumda döngüyü tekrar başlat

        print(round(result, 3))

    else:
        print("Geçersiz seçim. Lütfen geçerli bir operatör seçiniz.")