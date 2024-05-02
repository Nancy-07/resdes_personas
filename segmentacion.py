from PIL import Image
import os

def limpiar_carpeta(carpeta):
    for archivo in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta_archivo):
            os.remove(ruta_archivo)

def dividir_imagen(imagen, ancho_segmento, alto_segmento, carpeta_destino):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
    else:
        limpiar_carpeta(carpeta_destino)

    img = Image.open(imagen)
    ancho_total, alto_total = img.size

    contador = 1
    for y in range(0, alto_total, alto_segmento):
        for x in range(0, ancho_total, ancho_segmento):
            cuadro = (x, y, x + ancho_segmento, y + alto_segmento)
            segmento = img.crop(cuadro)
            segmento.save(os.path.join(carpeta_destino, f"segmento_{contador}.png"))
            contador += 1


imagen_original = "17.jpg"
ancho_segmento = 100
alto_segmento = 100
carpeta_destino = "segmentos"

dividir_imagen(imagen_original, ancho_segmento, alto_segmento, carpeta_destino)
