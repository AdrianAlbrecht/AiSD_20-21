# Z1
# Przygotować funkcję, która przyjmie w parametrach pierwszą literę imienia, oraz nazwisko, a następnie zwróci te wartości połączone kropką. Przykładowe wyjście: J. Kowalski.
def z1( pl, naz):
    return f'{pl}.{naz}'

# Z2
# Przygotować funkcję, która przyjmie w parametrach imię i nazwisko, oraz zwróci pierwszą literę imienia i nazwisko połączone kropką.
# Funkcja powinna również dbać o poprawność wielkich liter. Przykładowo, wejście: (jan, kowalski), wyjście: J. Kowalski.

def z2( im, naz):
    return f'{im[0].upper()}.{naz[0].upper()}{naz[1:]}'

# Z3
# Przygotować funkcję, która przyjmie 3 argumenty: 2 pierwsze cyfry aktualnego roku, 2 ostatnie cyfry aktualnego roku, wiek użytkownika, a następnie zwróci jego rok urodzenia.

def z3( fr, lr, w):
    return (fr*100+lr)-w

# Z4
# Przygotować funkcję, która przyjmie 3 parametry: imię, nazwisko i funkcję przetwarzającą te dane, a następnie zwróci wynik działania funkcji przyjętej w 3. parametrze.
# Przykładwo, wejście: (jan, kowalski, funkcja_z_zadania_2), wyjście: J. Kowalski.

def z4( imie, nazw, funk):
    return funk(imie, nazw)

# Z5
# Przygotować funkcję, która przyjmie 2 argumenty, a następnie zwróci wynik ich dzielenia. Należy sprawdzić w jednej instrukcji if (bez użycia elif i else),
# czy obydwie liczby są dodatnie oraz czy druga liczba jest różna od 0.

def z5( a, b):
    if (a>0) & (b>0): #Przyjmując że 0 nie jest liczbą dodatnią ani ujemną. Przyjmując że 0 jest dodatnia warunek następujący: "if (a>=0) & (b>0):"
        return a/b
    return "Błędne dane"

# Z6
# Przygotować skrypt, w którym użytkownik będzie podawał kolejne liczby w pętli, dopóki suma wszystkich podanych do tej pory liczb nie osiągnie wartości 100.

def z6():
    s=0
    while(s!=100): #Gdy suma musi wynosić równo 100 natomiast gdy przynajmniej 100: "while(s<=100):"
        print('Suma powinna wynosic: 100\nPodawaj liczby dalej! :)')
        s+= int(input())
        print(f'Suma wynosi:{s}')
    print("Koniec! :)")

# Z7
# Przygotować funkcję, która przyjmie 1 argument w postaci listy, a następnie zwróci te elementy w postaci krotki.

def z7( li):
    return tuple(li)

# Z8
# Przygotować skrypt, w którym użytkownik będzie wprowadzał do listy wartości używając pętli, a następnie wartości z tej zostanią zrzutowane do krotki.

def z8():
    a=[]
    b=''
    print("Podawaj wartości do listy. Zakończ wyrażeniem 'stop'. :)")
    while(b!="stop"):
        if b!="":
            a.append(b)
        b=input()
    return tuple(a)
# Z9
# Przygotować funkcję, która przyjmie 1 argument całkowitoliczbowy, a następnie zwróci nazwę dnia tygodnia odpowiadającą przekazanemu argumentowi.
# Nie należy w tym zadaniu używać instrukcji warunkowych! Przykładowo, wejście: 6, wyjście: sobota.

def z9( a ):
    tyg=['poniedziałek','wtorek','środa','czwartek','piątek','sobota','niedziela']
    return tyg[(a-1)%7]

# Z10
# Przygotować funkcję, która przyjmie argument w postaci łańcucha znaków, a następnie zwróci wartość logiczną informującą o tym czy przekazany tekst jest palindromem.

def z10( znaki ):
    if znaki==znaki[len(znaki)::-1]:
        return True
    return False


#print(z1("A","Albrecht"))
#print(z2("jan","kowalski"))
#print(z3(20,20,21))
#print(z4("Sylwia","Adamczyk",z2))
#print(z5(0,7))
#z6()
#print(z7([3,6,3,8,3]))
#print(z8())
#print(z9(281))
print(z10('Agnieszka'))
print(z10('kajak'))



