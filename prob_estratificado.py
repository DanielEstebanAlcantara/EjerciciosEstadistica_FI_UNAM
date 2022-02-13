
# distritos lista con el total de la población en cada distrito
distritos = [1525, 917, 2890]
# poblacion_tatal variable para almacenar el total de la población
poblacion_total = 0
# muestra variable con el valor de la muestra a tomar
muestra = 250
# muestra_por_distrito lista para obtenr la muestra por cada distrito
muestra_por_distrito = []

# Se calcula el total de la población
for poblacion in distritos:
    poblacion_total += poblacion

# Se obtiene el porcentaje y el valor se redondea a 3 dígitos
porcentaje = round((250*100)/poblacion_total, 3)

print("El total de la poblacion es {}, por lo que 250 personas representan el {}% ".format(
    poblacion_total, porcentaje))

# Se calcula la muestra que se obtendrá en por cada distrito y se redondea a dos dígitos
for distrito in distritos:
    muestra_por_distrito.append(round((distrito/poblacion_total)*250, 2))

print('Del distrito 1 se tomará una muestra de: {} personas\nDel distrito 2 se tomará una muestra de: {} personas\nDel distrito 3 se tomará una muestra de: {} personas\n'.format(
    muestra_por_distrito[0], muestra_por_distrito[1], muestra_por_distrito[2],))
