i = 1
while i:
    print("1 inserisci stringa: ")
    print("2 inserisci numero")
    print("3 esci")

    scelta = input("scegli un opzione")

    if scelta == "1":
        j = 1
        while j :
            stringa = input("inserisci una stringa: ")
            if stringa.isnumeric():
                print("hai scritto un numero")
            else:
                print(f"hai inserito la stringa: {stringa}")
                j=0

    elif scelta == "2":
        j = 1
        while j:
            numero = input("inserisci un numero: ")
            if numero.isnumeric():
                print(f"hai inserito il numero {numero}")
                j=0
            else:
                print("hai inserito una stringa")
            

    elif scelta == "3":
        i = 0
        print("esco")
    else:
        print("non hai inserito un valore valido") 