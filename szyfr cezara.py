# Szyfr cezara

# funkcja sprawdzająca poprawność przesuniecia o ile miejsc ma się przesunać znak kodu
def skok(x, min=1, max=26):
    while True:
        try:
            x = int(input("Wprowadź liczbę od 1 do 25: "))
            if x > min and x < max:
                break
            elif x < min or x > max:
                    print('liczba poza zakresem')
                    continue
        except ValueError: 
                print("Musisz wpisać wartość całkowitą.")
                continue
    return x


tekst = input('Wpisz wiadomość do zaszyrowania: ')

szyfr = ''
klucz = skok("Powiedz o jakie parametr od 1 do 25 zmienimy kod: ")
# właściwy kod szyfrujący
for i in range(len(tekst)):

    if ord(tekst[i]) > 122 - klucz:
        szyfr += chr(ord(tekst[i]) + klucz - 26) # 26 liczba liter a alfabecie angielskim
    elif ord(tekst[i]) < 64:
        szyfr += chr(ord(tekst[i])) # nie zmienione znaki nie alfabetyczne oraz liczby
    else:
        szyfr += chr(ord(tekst[i]) + klucz)
print("Zaszyfrowany tekst ma wygląd:", szyfr)
