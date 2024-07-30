from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF
import io

def generar_codigo_barras(num_ref):
    # Crear el código de barras
    codigo_barras = Code128(num_ref, writer=ImageWriter())
    
    # Guardar el código de barras en un buffer
    buffer = io.BytesIO()
    codigo_barras.write(buffer)
    
    # Mover el buffer al inicio
    buffer.seek(0)
    
    # Cargar la imagen del buffer
    imagen = Image.open(buffer).copy()
    
    # Dimensiones del código de barras
    ancho_barras, alto_barras = imagen.size
    
    # Definir las nuevas dimensiones
    nuevo_ancho = 600
    nuevo_alto = 298
    
    # Crear una nueva imagen con las dimensiones especificadas
    nueva_imagen = Image.new('RGB', (nuevo_ancho, nuevo_alto), "white")
    
    # Calcular las posiciones para centrar la imagen del código de barras
    posicion_x = (nuevo_ancho - ancho_barras) // 2
    posicion_y = (nuevo_alto - alto_barras) // 2
    
    # Pegar la imagen del código de barras en la nueva imagen
    nueva_imagen.paste(imagen, (posicion_x, posicion_y))
    
    # Añadir texto a la derecha del código de barras
    draw = ImageDraw.Draw(nueva_imagen)
    
    # Definir las fuentes y tamaños
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Cambiar esta ruta según sea necesario
    font_size = 20
    font = ImageFont.truetype(font_path, font_size)
    
    # Calcular las posiciones para el texto
    texto_x = posicion_x + ancho_barras + 10
    texto_y1 = posicion_y + 10
    texto_y2 = texto_y1 + 30  # Ajustar para la segunda línea de texto
    
    # Añadir "Curaduría Urbana"
    draw.text((texto_x, texto_y1), "Curaduría Urbana", font=font, fill="black")
    
    # Añadir "No. 2 Santa Marta" debajo del primer texto
    draw.text((texto_x, texto_y2), "No. 2 Santa Marta", font=font, fill="black")
    
    # Guardar la nueva imagen como PNG en la carpeta raíz
    nueva_imagen_path = "./codigo_barras_con_texto.png"
    nueva_imagen.save(nueva_imagen_path, format='PNG')
    
    # Cerrar el buffer
    buffer.close()

    return nueva_imagen_path

def crear_pdf_con_codigo_barras(imagen_path):
    # Crear el PDF
    pdf = FPDF(orientation='L', unit='mm', format=(28, 89))
    pdf.add_page()
    
    # Ajustar tamaño del título
    pdf.set_font("Arial", size=6)
    
    
    # Ajustar tamaño de la imagen del código de barras
    pdf.image(imagen_path, x=0, y=0, w=20)
    
    # Guardar el PDF en la carpeta raíz
    pdf_output_path = "./codigo_barras.pdf"
    pdf.output(pdf_output_path)
# Ejemplo de uso
num_ref = "123556789012"
imagen_codigo_barras_path = generar_codigo_barras(num_ref)
crear_pdf_con_codigo_barras(imagen_codigo_barras_path)
