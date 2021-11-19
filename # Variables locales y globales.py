# Variables locales y globales
v_global = "Soy global"
v_contador = 0 

def f1():
    v_contador = 100
    print(v_global)
    for i in range(2):
        pass

    print(i)



f1()
print(v_contador)