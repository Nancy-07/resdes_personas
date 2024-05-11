import csv
import matplotlib.pyplot as plt

# Listas para almacenar los datos
num_neuronas = []
precision = []

# Leer el archivo CSV y filtrar los datos
with open('resultados_model_primera100.csv', 'r') as archivo_csv:
    datos_csv = csv.reader(archivo_csv)
    for fila in datos_csv:
        momentum = float(fila[2])    # Tercer dato: momentum
        learning_rate = float(fila[3])         # Cuarto dato: learning rate
        if learning_rate == 0.1 and momentum == 0.8:
            num_neuronas.append(int(fila[1]))  # Segundo dato: número de neuronas
            precision.append(float(fila[4]))    # Último dato: precisión

# Graficar los datos
plt.plot(num_neuronas, precision, marker='o')
plt.title('Primer capa')
plt.xlabel('Número de neuronas')
plt.ylabel('Precisión')
plt.grid(True)
plt.show()
