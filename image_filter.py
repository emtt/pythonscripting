#Aplicar filtros a una imagen
from PIL import ImageFilter, Image
def apply_filters(input_path, ouput_path): #Función
    #Abrir la imagen
    img = Image.open(input_path)
    
    # Aplicar Filtros
    filtered_img = img.filter(ImageFilter.BLUR)
    #filtered_img = filtered_img.filter(ImageFilter.SHARPEN)
    filtered_img = filtered_img.filter(ImageFilter.CONTOUR)
    filtered_img = filtered_img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    
    #Guardar la imagen con filtros
    filtered_img.save(ouput_path)
    #filtered_img.show()
    
#Ejemplo de uso
image_origen = "C:\\Cursos\\Python\\Scripting\\images\\resized_IMG_3213.jpg"
image_destino = "C:\\Cursos\\Python\\Scripting\\images\\filtered_IMG_3213.jpg"

#Llamar la función
apply_filters(image_origen, image_destino)