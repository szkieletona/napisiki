import random
liczba=random.randint(1,100)

proby=int(input('liczba prob: '))
print('Odgaduj liczbę od 1 do 100, masz %s prób' %proby)
for proba_odp in range(0,proby):
    odp=int(input("Podaj liczbę: "))

    if odp >100 or odp<1:
        print("Źle źle źleeeeeeeeeeeeeeee")
        continue
        
    print(odp)

    if odp == liczba:
        print("Brawo prawidłowa odpowiedź")
        break
    elif odp < liczba:
        print("Za mało")
    else:
        print("Za dużo")

    zostalo=proby-(proba_odp +1)
    print("Zostalo Ci prob: %s" %zostalo)
    
    
print("Dzięki za grę")
print(liczba)
