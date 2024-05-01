# Distancias dadas en el problema
distancia_entre_fuentes = 150
distancia_efecto_fuente = 40

# Distancia del punto a la primera fuente (ejemplo)
distancia_punto_a_fuente_1 = 1

# Calcular la distancia del punto a la segunda fuente
distancia_punto_a_fuente_2 = distancia_entre_fuentes - distancia_punto_a_fuente_1

# Verificar si el punto está lo suficientemente lejos de ambas fuentes
if distancia_punto_a_fuente_1 > distancia_efecto_fuente + distancia_punto_a_fuente_2 and distancia_punto_a_fuente_2 > distancia_efecto_fuente + distancia_punto_a_fuente_1:
    print("El punto está libre de contaminación.")
else:
    print("El punto no está libre de contaminación.")