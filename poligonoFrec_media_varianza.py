# Importación de statistics, paquete que nos permite realizar calculos estadísticos de datos numéricos
import statistics as st
import matplotlib.pyplot as plt


def poligono_frecuencia():
    marcaDeClase = [37, 52, 65, 70, 93]
    frecuenciaRelativa = [0.1, 0.13, 0.3, 0.2, 0.26]

    fig, ax = plt.subplots()
    ax.set_xlabel("Marcas de clase")
    ax.set_ylabel("Frecuencias relativas")
    ax.plot(marcaDeClase, frecuenciaRelativa)
    plt.show()


poligono_frecuencia()

# Captura de datos
calificaciones = [100, 78, 89, 68, 88, 68, 69, 79, 94, 46, 36, 76, 40, 67, 58, 89, 90, 68, 70, 68,
                  30, 67, 86, 52, 45, 78, 60, 77, 99, 100]
# se ordenan los datos
calificaciones.sort()

# cálculo de la media con función mean, valor redandeado a 3 dígitos
media = round(st.mean(calificaciones), 3)

# Calculo de la varianza muestral con función variance, valor redondeado a 3 dígitos
varianza_insesgada = round(st.variance(calificaciones, media), 3)
# Calculo de la varianza poblacional con función pstdev, valor redondeado a 3 dígitos
varianza_poblacional = round(st.pstdev(calificaciones, media), 3)

print("Calificaciones: {}\nMedia: {}\nVarianza muestral: {}\nVarianza poblacional: {}".format(
    calificaciones, media, varianza_insesgada, varianza_poblacional))
