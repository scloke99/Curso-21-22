def letras():

    while True:
        vocales = input("introduzca la letra: ")

        if vocales == "a":
            print("vocal")
        elif vocales == "e":
            print("vocal")
        elif vocales == "i":
            print("vocal")
        elif vocales == "o":
            print ("vocal")
        elif vocales == "u":
            print ("vocal")
        elif vocales == " ":
             return False
        else:
            print("No vocal")

print(letras()) 