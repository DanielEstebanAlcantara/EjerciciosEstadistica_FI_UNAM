# Importar stemgraphic, paquete para realizar gráficas de tallos y hojas
import stemgraphic
# Captura de datos
niveles_sangineos = [45, 66, 83, 71, 76, 64, 59, 59, 76, 82, 80, 81, 85, 77, 82, 90, 87, 72, 79, 69, 83,
                     71, 87, 69, 81, 76, 96, 83, 67, 94, 101, 94, 89, 94, 73, 99, 93, 85, 83, 80, 78, 80,
                     85, 83, 84, 74, 81, 70, 75, 89, 70, 80, 84, 77, 65, 46, 80, 70, 75, 45, 101, 71, 109,
                     73, 73, 80, 72, 81, 63, 74]

# Graficar, método stem_graphic con la lista de datos, esala de 10, y sin espacios vacios
stemgraphic.stem_graphic(niveles_sangineos, scale=10, compact=True)
