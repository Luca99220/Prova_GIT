numero_1 = int(input("inserisci il primo numero: "))
numero_2 = int(input("inserisci il secondo numero: "))
numero_3= int(input("inserisci il terzo numero: "))

if numero_1 == numero_2 == numero_3:
    print("i numeri sono tutti uguali")
elif numero_1 != numero_2 and numero_1 != numero_3 and numero_3 != numero_2:
    print ("tutti i numeri sono diversi")
else:
    print("solo un numero è diverso dagli altri")