import csv

def csv_write():
    matriz =
    with open("nuevo_1.csv","a") as f:
        escritor = csv.writer(csv_write)
        escritor.writerow(["Jueves"]*10+["viernes"])
        escritor.writerow(["nada"]*10+["fin"])

csv_write()