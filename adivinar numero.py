from random import randrange
objetivo = randrange(100)
veces = 0

for i in range(10):
    veces +=1
    intento = int(input("introduce un numero :  "))
    if objetivo > intento:
        print("es mayor")
    elif objetivo < intento:
        print("es menor")
    else:
        print (f"has acertado en {veces} intentos")
        break
    if veces > 9:
        print(f"has perdido.\nEl numero era {objetivo}")