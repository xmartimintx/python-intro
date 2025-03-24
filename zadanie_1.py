#zadanie_1

#Opis funkcji wbudowanej (np. zip(), enumerate(), sorted()).

# Funkcja wbudowana sorted() służy do sortowania elementów dowolnego iterowalnego obiektu (takiego jak lista, krotka czy ciąg znaków) i zwraca nową, posortowaną listę, pozostawiając oryginalny obiekt bez zmian. Domyślnie sortowanie odbywa się w kolejności rosnącej, ale można to zmienić za pomocą parametru 'reverse'...

#Dokumentacja: https://docs.python.org/pl/3/library/functions.html#sorted
####################################################

#Opis modułu z biblioteki standardowej (np. math, random, time).

# Moduł random znajduje się w bibliotece standardowej i dostarcza potrzebne funkcje do generowania liczb pseudolosowych oraz wykonywania operacji losowych na danych. Jest przydatny w symulacjach, testowaniu, grach oraz wszędzie tam, gdzie potrzebne są losowe dane...
#Dokumentacja: https://docs.python.org/3/library/random.html
####################################################
#Opis wyjątku (np. ValueError, ZeroDivisionError).

# ValueError to wyjątek w Pythonie, który pojawia się, gdy funkcja otrzymuje argument o poprawnym typie, ale niewłaściwej wartości. Na przykład próba zamiany napisu "abc" na liczbę całkowitą (int("abc")) spowoduje ten błąd, ponieważ "abc" nie jest liczbą. Podobnie, jeśli funkcja matematyczna otrzyma liczbę ujemną, zwróci ValueError...

#Dokumentacja: https://docs.python.org/3/library/exceptions.html#ValueError
####################################################

import random

a = [1, 2, 3, 4, 5] #lista 1
b = ['a', 'b', 'c', 'd', 'e'] #lista 2

zip_list = list(zip(a, b)) #skompresowana lista
print("Połączone listy:", zip_list) #wypisz listę skompresowaną

random_c = random.choice(a) #wygeneruj losową liczbę
print("Losowy element z listy 'cyfr':", random_c) #wypisz ją

try: #wykonaj
    index = int(input("Podaj indeks (liczony od 0!) elementu z listy 'liter': "))
    print("Wybrany element z indeksem:",index,",to: ", b[index])
except ValueError: #jeśli błąd
    print("Błąd: Podana wartość nie jest liczbą!")
except IndexError: #jeśli błąd
    print("Błąd: Indeks poza zakresem listy!")
