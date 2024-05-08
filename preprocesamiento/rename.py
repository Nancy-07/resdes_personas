import os

def rename_images_in_folder(folder_path):
    # Lista de extensiones de archivos de imagen que queremos renombrar
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

    # Obtenemos la lista de archivos en la carpeta especificada
    files = os.listdir(folder_path)

    # Inicializamos un contador para los nombres incrementales
    counter = 745

    # Recorremos cada archivo en la carpeta
    for file_name in files:
        # Obtenemos la extensión del archivo
        _, extension = os.path.splitext(file_name)

        # Verificamos si el archivo tiene una extensión de imagen
        if extension.lower() in image_extensions:
            # Creamos el nuevo nombre con el formato "1.jpg", "2.png", etc.
            new_name = f"{counter}{extension}"

            # Ruta completa al archivo actual
            old_path = os.path.join(folder_path, file_name)
            # Ruta completa al nuevo nombre de archivo
            new_path = os.path.join(folder_path, new_name)

            # Renombramos el archivo
            os.rename(old_path, new_path)

            # Incrementamos el contador
            counter += 1

    print("Renombrado completado.")

# Especifica la ruta a la carpeta que contiene las imágenes que deseas renombrar
carpeta = "new_images/animals"

# Llamamos a la función para renombrar las imágenes
rename_images_in_folder(carpeta)
