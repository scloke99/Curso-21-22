import random as rd
def genera_equipos(personas):
    personas = alumnos.copy()
    rd.shuffle(personas)
    equipos = []
    numero_equipos = len(personas) // 2 
    for i in range (numero_equipos):
        eq = []
        eq.append(personas.pop())
        eq.append(personas.pop())
        equipos.append(eq)
       
    if len(personas) > 0:
        equipos[numero_equipos - 1].append(personas.pop())


    return equipos


alumnos = [1,2,3,4,5,6,7,8,9]
for i in range(5):
    x = genera_equipos(alumnos)
    print(x)


