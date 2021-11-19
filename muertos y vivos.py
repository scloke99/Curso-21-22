import os
import csv
import pprint   

os.system('cls')

ruta =  "/home/admin/Desktop/curso/"

def leer_archivo():
    csv_in = open(ruta + 'titanic.csv') 
    lector_dic = csv.DictReader(csv_in)

    lista_dict = list(lector_dic)

    csv_in.close()
    return lista_dict
    
def leer_valores():
    pasajeros = leer_archivo()
    hombres = []
    mujeres = []
    hv = 0
    hm = 0
    mv = 0
    mm = 0
    for p in pasajeros:
        if p["Sex"] == "female":
            mujeres.append(p["Survived"])
        else:
            hombres.append(p["Survived"])
    
    h_v = hombres.count("1")
    h_m = hombres.count("0")
    m_v = mujeres.count("1")
    m_m = mujeres.count("0")

    return h_m, h_v , m_v , m_m

resultado = leer_valores()
print(f"hombres vivos:{resultado[1]} hombres muertos:{resultado[0]}")
print(f"mujeres vivas:{resultado[2]} mujeres muertas:{resultado[3]}")

