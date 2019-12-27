lista = []
wybor = ["1. Zaplanuj zakupy - wpisz produkty do listy", "2. Na zakupach - odznacz kupione produkty", "3. Zakmnij program"]
x = 0
x = (int(x))
while x !=3:

    print("\nTwoja lista zakupów:")
    for zakupki in lista:
        print("-",zakupki)
    print("\nCo chcesz zrobić? (wpisz odpowiednią cyfrę):")
    for wybierz in wybor:
        print(wybierz)
    x=input()
    x=int(x)
    if x == 1:
        while True:
            print("\nTwoja lista zakupów:")
            for zakupki in lista:
                print("-", zakupki)
            print("\nco dodajemy do listy?: (żeby powrócić do menu wciśnij 'e')")
            y = input()
            if y == "e":
                break
            else:
                lista.append(y)
    if x == 2:
        while True:
            print("\nTwoja lista zakupów:")
            for zakupki in lista:
                print("-", zakupki)
            print("\nco usuwamy z listy?: (żeby powrócić do menu wciśnij 'e')")
            y = input()
            if y == "e":
                break
            if y in lista:
                lista.remove(y)
            else:
                print("ups nie ma takiego produktu na liście")

print("Dzięki do zobaczenia!")



