def introduce():
    personas = {}


    for i in range(5):
        nombre = input ("introduzca nombre: ")
        apellidos = input ("introduzca apellidos: ")
        dni = input ("introduzca DNI: ")
        personas[dni] = {"nombre":nombre, "apellidos": apellidos}
    
    return personas

print(introduce())

