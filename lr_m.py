import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Listas para almacenar los datos
learning_rates = []
momentums = []
precision = []

# Leer el archivo CSV y filtrar los datos
with open('resultados_model_tercera.csv', 'r') as archivo_csv:
    datos_csv = csv.reader(archivo_csv)
    for fila in datos_csv:
        learning_rate = float(fila[3])     # Cuarto dato: learning rate 
        momentum = float(fila[2])    # Tercer dato: momentum   
        num_neuronas = int(fila[1])    # Segundo dato: número de neuronas
        if num_neuronas == 15 and learning_rate == 0.9999999999999999:
            # learning_rates.append(float(fila[3]))    
            momentums.append(float(fila[2]))         
            precision.append(float(fila[4]))         

plt.plot(momentums, precision, marker='o')
plt.xlabel('Momentum')
plt.ylabel('Precisión')
plt.grid(True)
plt.show()