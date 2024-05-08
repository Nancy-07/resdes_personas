import cv2
import os
import math
import numpy as np
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfTransformer
import csv

def encontrarDescriptores(ruta_imagen, detector):
    img = cv2.imread(ruta_imagen)
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    keypoints, descriptores = detector.detectAndCompute(gris, None)
    return keypoints, descriptores

def momentosHu(ruta_imagen):
    imagen = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
    _, imagen = cv2.threshold(imagen, 128, 255, cv2.THRESH_BINARY)
    moments = cv2.moments(imagen)
    momentos_hu = cv2.HuMoments(moments)
    for i in range(0, 7):
        if momentos_hu[i] <= 0:
            momentos_hu[i] = 0.0  #
        else:
            momentos_hu[i] = -1 * math.copysign(1.0, momentos_hu[i]) * math.log10(abs(momentos_hu[i]))
    return momentos_hu

def extraerDescriptoresGlobal(ruta_folder, detector):
    descriptores_global = []
    ruta_imagenes = []
    for nombre_imagen in os.listdir(ruta_folder):
        ruta_imagen = os.path.join(ruta_folder, nombre_imagen)
        keypoints, descriptores = encontrarDescriptores(ruta_imagen, detector)
        momentos_hu = momentosHu(ruta_imagen)
        if descriptores is not None:
            descriptores_global.extend(descriptores)
            ruta_imagenes.append(ruta_imagen)
    return np.array(descriptores_global), ruta_imagenes

def calcularHistograma(ruta_imagen, detector, kmedias):
    keypoints, descriptores = encontrarDescriptores(ruta_imagen, detector)
    if descriptores is None:
        return None
    else:
        palabras_visuales = kmedias.predict(descriptores)
        histograma, _ = np.histogram(palabras_visuales, bins=range(kmedias.n_clusters + 1))
        return histograma

def main(ruta_folders, csv_file):
    detector = cv2.SIFT_create()
    all_descriptors = []
    all_labels = []

    for etiqueta, ruta_folder in enumerate(ruta_folders, start=0):
        descriptores_global, ruta_imagenes = extraerDescriptoresGlobal(ruta_folder, detector)

        # Clusters de características
        kmedias = KMeans(n_clusters=13)
        kmedias.fit(descriptores_global)

        final_descriptores = []

        for ruta_imagen in ruta_imagenes:
            histograma = calcularHistograma(ruta_imagen, detector, kmedias)
            if histograma is not None:
                momentos_hu = momentosHu(ruta_imagen)
                momentos_hu_flat = momentos_hu.flatten()  # Convertir a unidimensional

                # Calcular histogramas TF-IDF
                transformer = TfidfTransformer()
                histograma_tfidf = transformer.fit_transform([histograma]).toarray()[0]

                # Juntar momentos de Hu con histogramas TF-IDF
                descriptores_combinados = np.concatenate((momentos_hu_flat, histograma))
                final_descriptores.append(descriptores_combinados)
                all_labels.append(etiqueta)

        all_descriptors.extend(final_descriptores)

    # Se crea el archivo CSV
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for descriptor, label in zip(all_descriptors, all_labels):
            writer.writerow(list(map(str, descriptor)) + [label])

# 0 - animales
# 1 - ciudad
# 2 - personas

# Define las carpetas y etiquetas
ruta_folders = ["etiquetado_final/animales", "etiquetado_final/ciudad", "etiquetado_final/personas"]
csv_file = "descriptores/descriptores_completos.csv"

# Ejecuta la función principal
main(ruta_folders, csv_file)


