# v1 = [1,2]
# v2 = [7,8]
# total = 0

# for x in range(len(v1)):
#     total += v1[x] * v2[x]
# print(total)

origen = [1,2,3,4,5, "Jose", "Alan", "Fernando"]
numero = []
alumnos = []

for x in origen:
    if type(x) == str:
        alumnos.append(x)
    else:
            numero.append(x)
print(origen)
print(alumnos)
print(numero)
