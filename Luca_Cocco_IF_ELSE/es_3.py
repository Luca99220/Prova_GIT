numero_1= int(input("inserire un numero: "))
numero_2= int(input("inserire un numero: "))
numero_3= int(input("inserire un numero: "))
numero_4= int(input("inserire un numero: "))

numero_minimo = min (numero_1, numero_2, numero_3, numero_4)
numero_massimo = max (numero_1, numero_2, numero_3, numero_4)

if numero_1 == numero_2 or numero_1 == numero_3 or numero_1 == numero_4:
    print("ci sono due numeri uguali")
else: 
    print("non ci sono numeri uguali")

print(f"il numero più grande è il {numero_massimo}")
print(f"il numero più piccolo è il {numero_minimo}")