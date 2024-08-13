from PIL import Image, ImageDraw, ImageFont

def create_image_with_text(text: str, font_size: int = 12, output_path: str = "output.png"):
    # Crear un objeto de fuente con el tamaño especificado
    font = ImageFont.truetype("arial.ttf", font_size)

    # Crear una imagen lo suficientemente grande para contener el texto
    # Se crea una imagen temporal para medir el tamaño del texto
    temp_image = Image.new("RGB", (1, 1), (255, 255, 255))
    draw = ImageDraw.Draw(temp_image)
    text_width, text_height = draw.textsize(text, font=font)

    # Crear una imagen ajustada al tamaño del texto
    image = Image.new("RGB", (text_width, text_height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Dibujar el texto en la imagen
    draw.text((0, 0), text, fill="black", font=font)

    # Guardar la imagen
    image.save(output_path)



def overlay_image(w,h, imagen_base: str, imagen_in: str, output_path: str = "output.jpg"):
    # Abrir la imagen base
    base_image = Image.open(imagen_base)
    
    # Abrir la imagen a superponer
    overlay_image = Image.open(imagen_in).convert("RGBA")
    
    # Definir la posición donde se superpondrá la imagen
    position = (w, h)
    
    # Superponer la imagen overlay_image sobre base_image
    base_image.paste(overlay_image, position, overlay_image if overlay_image.mode == 'RGBA' else None)
    
    # Guardar la imagen resultante
    base_image.save(output_path)


# Uso de la función
create_image_with_text("CU2-2401403", output_path="radicado.jpg")
overlay_image(200, 70, "BASE_radicacion2.jpg", "radicado.jpg", "Base_con_radicado.jpg")
create_image_with_text("09/08/2024", output_path="fecha.jpg")
overlay_image(200, 100, "Base_con_radicado.jpg", "fecha.jpg", "Base_con_fecha.jpg")
create_image_with_text("11:11", output_path="hora.jpg")
overlay_image(200, 130, "Base_con_fecha.jpg", "hora.jpg", "final.jpg")
#############################
create_image_with_text("CU2-2401403", output_path="oficio.jpg")
overlay_image(360, 20, "BASE_oficios.jpg", "oficio.jpg", "BaseOF_numof.jpg")
