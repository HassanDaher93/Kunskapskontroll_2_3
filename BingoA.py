# Importerar in modulen random för att få tillgång till slumptals funktioner
import random
# Importerar in modulen NumPy för att få tillgång till 2d array
import numpy as np
# Importerar in modulen os för att kunna hantera utskrivet text till användaren
import os

# Variabel som tilldelas 10 för att hålla koll på användarens gissningar. (Man kan ändra detta till lägre värde)
antal_gissningar = 10

# En tom lista
lista = []
# loop som körs så länge antal heltal i lista är mindre än antal_gissningar
while len(lista) < antal_gissningar:
# Felhantering tillsammans med att anändaren ska skriva in ett heltal mellan 1 och 25 som läggs in i listan bara ifall heltalet inte finns i listan
    try:
        gissa = input("Ange ett tal mellan 1 och 25! ")
        tal = int(gissa)
        if 1 <= tal <= 25:
            if tal not in lista:
                lista.append(tal)
# Ifall heltalet finns i listan så skriv det till användaren         
            else:
                print("Talet finns redan i listan. Försök igen.")
# Ser till att du inte skriver något annat tal än det som är tillsagt         
        else:
            print("Talet måste vara mellan 1 och 25!")
    except ValueError:
        print("Ogiltigt! Försök igen med ett heltal.")

# Skriver ut alla heltal i listan som användaren fick skriva in
print("\n\nBoll nr: " + str(lista))

# Skapar en numpy array med talen 1 till 25
bingobricka = np.arange(1, 26)
# Blandar talen i numpy arrayen
np.random.shuffle(bingobricka)
# Ändrar arrayens form till 5x5 så det ser ut som en bricka
bingobricka5x5 = bingobricka.reshape((5, 5))

# Oändlig loop
while True:
# Rensar utskrivet text i konsollen
    os.system("cls")

# Ifall heltalen(bollar) matchar med brickan vågrät så skriv ut bingo samt skriver ut uppdatering av bollar
    for vägrät in bingobricka5x5:
        if all(talen1 in lista for talen1 in vägrät):
            print("   Bingobricka")
            print(bingobricka5x5)
            print("\nBollar" + str(lista))
            print("\nBingo i rad (vågrät)!")
# Hållkod            
            input()
# Avslutar programmet            
            os._exit(1)

# Ifall heltalen(bollar) matchar med brickan lodrät så skriv ut bingo samt skriver ut uppdatering av bollar
    for lodrät in bingobricka5x5.T:
        if all(talen2 in lista for talen2 in lodrät):
            print("   Bingobricka")
            print(bingobricka5x5)
            print("\nBollar" + str(lista))
            print("\nBingo i rad (lodrät)!")
# Hållkod            
            input()
# Avslutar programmet            
            os._exit(1)

# Ifall heltalen(bollar) matchar med brickan diagonalt så skriv ut bingo samt skriver ut uppdatering av bollar
    for diagonal1 in [bingobricka5x5.diagonal()]:
        if all(talen3 in lista for talen3 in diagonal1):
            print("   Bingobricka")
            print(bingobricka5x5)
            print("\nBollar" + str(lista))
            print("\nBingo i diagonal")
# Hållkod
            input()
# Avslutar programmet              
            os._exit(1)
            
# Ifall heltalen(bollar) matchar med brickan diagonalt så skriv ut bingo samt skriver ut uppdatering av bollar
    for diagonal2 in [np.fliplr(bingobricka5x5).diagonal()]:
        if all(talen4 in lista for talen4 in diagonal2):
            print("   Bingobricka")
            print(bingobricka5x5)
            print("\nBollar" + str(lista))
            print("\nBingo i diagonal!")
# Hållkod 
            input()
# Avslutar programmet 
            os._exit(1)           

# slumpmässigt tal mellan 1 och 25
    nyboll = random.randint(1,25)
# Ifall talet som slumpas inte är med i listan så lägg in det samt skriver ut uppdatering av bollar    
    if nyboll not in lista:
        lista.append(nyboll)
        print("   Bingobricka")
        print(bingobricka5x5)
        print("\nBoll nr: " + str(nyboll) + "\n\nBollar" + str(lista))
# Ifall talet finns i listan så skriv ut det samt skriver ut uppdatering av bollar   
    else:
        print("   Bingobricka")
        print(bingobricka5x5)
        print("\nBoll nr: " + str(nyboll), "finns redan så den kan inte användas")
        print("\nBollar" + str(lista))

# Tryck på enter tangenten för att få en ny boll 
    input("\n\nTryck på enter tangenten för ett nytt boll drag")
    