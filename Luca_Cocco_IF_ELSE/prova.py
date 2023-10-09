while True:
    print("Menu:")
    print("1. inserisci una stringa")
    print("2. inserisci un numero")
    print("3. esci")

    scelta = input("scegli un opzione tra 1 2 3")
    if scelta == "1":
        stringa = input("inserisci una stringa")
        if stringa.isnumeric():
            print("hai inserito un numero, riprova")
        else:
            print(f"hai inserito la stringa {stringa}")
    