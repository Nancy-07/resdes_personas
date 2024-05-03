import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
from IPython.display import clear_output

def etiquetar(carpeta_entrada):
    # Imagen original
    
    
    # Obtener las regiones de la imagen
    archivos = os.listdir(carpeta_entrada)
    i=0
    # Mostrar cada región y guardarla
    for archivo in archivos:
        ruta_imagen = os.path.join(carpeta_entrada, archivo)
        region = cv2.imread(ruta_imagen)
        
        plt.imshow(cv2.cvtColor(region, cv2.COLOR_BGR2RGB))
        plt.show()
        
        tag = input("Etiqueta de imagen: ") # Puede ser C (ciudad) / A (animal) / P (persona)
        if tag == "C":
            folder_name = "ciudadCropped"
        elif tag =="P":
            folder_name = "personasCropped"
        elif tag == "A":
            folder_name = "animalesCropped"
        elif tag == "R":
            folder_name = "ruidoCropped"
            
        folder = f"vale_etiquetas/{folder_name}"

        if not os.path.exists(folder):
            os.makedirs(folder)
        
        # Guardar la imagen
        image_name = f"{i + 1}.jpg"
        i = i+1
        cv2.imwrite(os.path.join(folder, image_name), region)
        
        print(f"Imagen {image_name} guardada en la carpeta {folder}")
        clear_output(wait=True)
        


etiquetar("vale_segmentos2")