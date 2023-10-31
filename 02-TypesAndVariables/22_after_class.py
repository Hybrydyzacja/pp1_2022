price = round(float(input("Podaj cenę: ")),2)
#jeśli cena jest liczbą całkowitą, to wyświetla się tylko jedno miejsce po przecinku
#jak zrobic 2?
VAT = round(price * 0.23,2)

print(f"Cena: {price} zł")
print(f"Podatek VAT 23%: {VAT} zł")

