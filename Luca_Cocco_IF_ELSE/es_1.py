def area_rettangolo (base, altezza):
    area= base * altezza
    return area

base_1 = int(input("inserisci la prima base: "))
altezza_1 = int(input("inserisci la prima altezza: "))

base_2= int(input("inserisci la seconda base: "))
altezza_2= int(input("inserisci la seconda altezza: "))

area_1= area_rettangolo(base_1, altezza_1)
area_2= area_rettangolo(base_2, altezza_2)

if area_1 > area_2:
    print("l'area del rettangolo 1 è la più grande", area_1)

elif area_2 > area_1:
    print("l'area del rettangolo 2 è la più grande", area_2)
else:
    print("i due rettangoli hanno la stessa area")