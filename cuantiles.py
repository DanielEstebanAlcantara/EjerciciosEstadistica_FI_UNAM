import statistics

# calorias_por_barra lista con las calorias de cada barra
calorias_por_barra = [342, 377, 319, 353, 295, 234, 294, 286, 377,
                      182, 310, 439, 111, 201, 182, 197, 209, 147, 190, 151, 131, 151]


# Se calculan los cuantiles, en este caso centiles usando el método quantiles() que regresa una lista con los centiles y almacenan en la variable cuantiles
cuatniles = statistics.quantiles(calorias_por_barra, n=100)

# A cada variable se le adigna la posición de la lista cuantiles según sea el cuantil que se pide, 35, 50 o 76
cuantil_35 = cuatniles[35-1]
cuantil_50 = cuatniles[50-1]
cuantil_76 = cuatniles[76-1]


print("El cauntil 35 es: {}\nEl cauntil 50 es: {}\nEl cauntil 76 es: {}".format(
      cuantil_35, cuantil_50, cuantil_76))
