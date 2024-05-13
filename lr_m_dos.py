import csv
import matplotlib.pyplot as plt

def procesar_archivo(archivo_csv, num_neuronas_target, momentum_target, lr_target):
    learning_rates = []
    momentums = []
    precision = []

    with open(archivo_csv, 'r') as archivo_csv:
        datos_csv = csv.reader(archivo_csv)
        for fila in datos_csv:
            learning_rate = float(fila[3])
            momentum = float(fila[2])
            num_neuronas = int(fila[1])
            if num_neuronas == num_neuronas_target and learning_rate == lr_target:
                learning_rates.append(learning_rate)
                momentums.append(momentum)
                precision.append(float(fila[4]))

    return learning_rates, momentums, precision

# Procesar los dos archivos CSV
momentum_target = 0.8
lr_target = 0.1

learning_rates_capa1, momentums_capa1, precision_capa1 = procesar_archivo('resultados_model_segunda.csv', 10, momentum_target, 0.8999999999999999)
learning_rates_capa2, momentums_capa2, precision_capa2 = procesar_archivo('resultados_model_tercera.csv', 15, momentum_target, 0.9999999999999999)

# Graficar los datos
plt.plot(momentums_capa1, precision_capa1, label='Capa 2, Learning rate = 0.8999999', marker='o', color='#7696eb')
plt.plot(momentums_capa2, precision_capa2, label='Capa 3, Learning rate = 0.9999999', marker='o', color='#2528b5')

plt.title('Precisión')
plt.xlabel('Momentum')
plt.ylabel('Precisión')
plt.grid(True)
plt.legend()
plt.show()
