precio_parking = 42
precio_semana = 100
semanas = 7

def parking(dias):
    semana = dias // semanas
    dias_restantes = dias % semanas
    coste_semanal = semana * precio_semana 
    coste_dias = dias_restantes * precio_parking
    total =coste_dias + coste_semanal

    return total

print(parking(7))


