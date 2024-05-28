import csv
import matplotlib.pyplot as plt

def obtener_mejores_precisiones(archivo_csv, num_neuronas, top_n=10):
    precisiones = []

    with open(archivo_csv, 'r') as archivo:
        datos_csv = csv.reader(archivo)
        for fila in datos_csv:
            if int(fila[1]) == num_neuronas:
                precisiones.append((float(fila[4]), float(fila[2]), float(fila[3])))

    # Ordenar las precisiones de mayor a menor
    precisiones.sort(reverse=True)

    return precisiones[:top_n]

# Número de neuronas deseado
num_neuronas = 15

# Procesar los tres archivos CSV
archivo_capa1 = 'resultados_model_tercera.csv'

mejores_precisiones_capa1 = obtener_mejores_precisiones(archivo_capa1, num_neuronas)

# Preparar datos para graficar
precisiones = []
lr_momentums = []

for i, (precision, lr, momentum) in enumerate(mejores_precisiones_capa1):
    lr = round(lr, 1)
    momentum = round(momentum, 1)
    lr_momentums.append(f'LR = {lr} \nMomentum = {momentum}')
    precisiones.append(precision)

# Graficar los datos
plt.bar(lr_momentums, precisiones, color='skyblue')
plt.ylabel('Precision')
plt.xlabel('Learning Rate y Momentum')
plt.title(f'Las 10 mejores precisiones para {num_neuronas} neuronas')
plt.show()

