
import random
import statistics

# yds_por_jugador lista con las yardas que anotó cada jugador
yds_por_jugador = [4.99, 4.648, 4.631, 4.618, 4.611, 4.569, 4.168, 4.154, 3.977, 3.971,
                   3.752, 3.547, 3.540, 3.496, 3.494, 3.447, 3.418, 3.378, 3.299, 3.144]

# muestra lista con los 5 elementos aleatorios a considerar en la mestra
muestra = []

# Se llena la lista con el valor de la posicion aleatoria de la lista yds_por_jugador
for i in range(5):
    muestra.append(yds_por_jugador[random.randint(0, 19)])

# Se obtiene la media de la muestra con el método mean y se gurada en la varible media
media = statistics.mean(muestra)


print(muestra)
print(media)
