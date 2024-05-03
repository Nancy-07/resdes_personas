from PIL import Image
import os

def limpiar_carpeta(carpeta):
    """Limpia la carpeta destino borrando todos los archivos existentes."""
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    else:
        for archivo in os.listdir(carpeta):
            ruta_archivo = os.path.join(carpeta, archivo)
            if os.path.isfile(ruta_archivo):
                os.remove(ruta_archivo)

def dividir_imagen(imagen, ancho_segmento, alto_segmento, carpeta_destino, numero_de_imagen):
    """Divide una imagen en segmentos y los guarda en la carpeta destino."""
    img = Image.open(imagen)
    ancho_total, alto_total = img.size

    contador = 1
    for y in range(0, alto_total, alto_segmento):
        for x in range(0, ancho_total, ancho_segmento):
            cuadro = (x, y, x + ancho_segmento, y + alto_segmento)
            segmento = img.crop(cuadro)
            nombre_segmento = f"nopeople{numero_de_imagen}_{contador}.jpg"
            segmento.save(os.path.join(carpeta_destino, nombre_segmento))
            contador += 1

def procesar_carpeta_imagenes(carpeta_origen, ancho_segmento, alto_segmento, carpeta_destino):
    """Procesa todas las imágenes en la carpeta origen, dividiéndolas en segmentos."""
    limpiar_carpeta(carpeta_destino)
    
    for indice, archivo in enumerate(os.listdir(carpeta_origen), start=1):
        if archivo.endswith(".jpg") or archivo.endswith(".png"):
            ruta_imagen = os.path.join(carpeta_origen, archivo)
            
            dividir_imagen(ruta_imagen, ancho_segmento, alto_segmento, carpeta_destino, indice)

carpeta_origen = "imag/without_people"
ancho_segmento = 200
alto_segmento = 200
carpeta_destino = "nancy_segmentos2"

procesar_carpeta_imagenes(carpeta_origen, ancho_segmento, alto_segmento, carpeta_destino)
