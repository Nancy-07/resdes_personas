import csv
import matplotlib.pyplot as plt

def procesar_archivo(archivo_csv, lr_target, momentum_target):
    num_neuronas = []
    precision = []

    with open(archivo_csv, 'r') as archivo_csv:
        datos_csv = csv.reader(archivo_csv)
        for fila in datos_csv:
            momentum = float(fila[2])
            learning_rate = float(fila[3])
            if learning_rate == lr_target and momentum == momentum_target:
                num_neuronas.append(int(fila[1]))
                precision.append(float(fila[4]))

    return num_neuronas, precision

# Procesar los tres archivos CSV
lr_target = 0.1
momentum_target = 0.8

num_neuronas_capa1, precision_capa1 = procesar_archivo('resultados_model_primera100.csv', lr_target, momentum_target)
num_neuronas_capa2, precision_capa2 = procesar_archivo('resultados_model_segunda.csv', lr_target, momentum_target)
num_neuronas_capa3, precision_capa3 = procesar_archivo('resultados_model_tercera.csv', lr_target, momentum_target)

# Graficar los datos
plt.plot(num_neuronas_capa1, precision_capa1, label='Capa 1', marker='o', color='#7035d3')
plt.plot(num_neuronas_capa2, precision_capa2, label='Capa 2', marker='o', color='#7696eb')
plt.plot(num_neuronas_capa3, precision_capa3, label='Capa 3', marker='o', color='#2528b5')

plt.title('Precisión en función del número de neuronas (LR=0.1, Momentum=0.8)')
plt.xlabel('Número de neuronas')
plt.ylabel('Precisión')
plt.grid(True)
plt.legend()
plt.show()
