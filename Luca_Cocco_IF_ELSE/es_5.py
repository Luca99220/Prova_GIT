altezza_palazzo = int(input("inserisci il numero di piani del palazzo: "))
piano_ascensore_1 = int(input("inserisci il piano dell'ascensore 1: "))
piano_ascensore_2 = int(input("inserisci il piano dell'ascensore 2: "))
piano_utente = int(input("l'utente si trova al piano: "))

distanza_ascensore_1= abs(piano_ascensore_1 - piano_utente)
distanza_ascensore_2= abs(piano_ascensore_2 - piano_utente)

if distanza_ascensore_1 > distanza_ascensore_2:
    print("l'ascensore 2 sta arrivando ")
else:
    print("l'ascensore 1 sta arrivando")