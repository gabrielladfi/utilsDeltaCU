from PIL import Image, ImageDraw, ImageFont

# Configuración de la imagen
width = 1920  # Ancho de la imagen en píxeles (HD)
height = 1080  # Altura de la imagen en píxeles (HD)
background_color = "yellow"  # Color de fondo
margin_top = 20  # Margen entre el primer y segundo texto en píxeles
margin_between_texts = 30  # Margen entre el segundo y tercer texto en píxeles

# Configuración del texto
text1 = "CURADORA URBANA Nº2 DE SANTA MARTA, Magdalena\nARQ Mónica Villalobos Leal\nCalle 25 4 52"
text2 = """Solicitante(s): GUSTAVO PINEDO COBOS
Fecha de solicitud: 21-jun-24
Nº de Radicación: {Num Radicado}
Dirección(es) del Predio: CL 29 | 21 D 1 36 (ACTUAL)
Barrio/Urbanización: EL PIÑON
Tipo de Solicitud: LICENCIA DE CONSTRUCCIÓN
Modalidades: Obra Nueva
Uso(s): {usos}
Descripción Proyecto: {descripción}
Nº de pisos propuestos: {num_pisos}
Nº unidades propuestas: {num_unidades}"""
text3 = """ESTA VALLA ADVIERTE A TEREROS SOBRE LA INICIACIÓN DEL TRÁMITE ADMINISTRATIVO PARA QUE PUEDA
HACERSE PARTE Y FORMULAR SUS OBJECIONES HASTA ANTES DE LA EXPEDICIÓN DEL ACTO ADMINISTRATIVO
QUE RESUELVA LA SOLICITUD CONFORME AL ARTICULO 2.2.6.1.2.2.2 DEL DECRETO 1077 DE 2015.

De conformidad con lo dispuesto en el Artículo 53 y Subsiguientes de la Ley 1437 de 2011 Adicionado por la
Ley 2080 de 2021, y en el Artículo 2.2.6.6.6.5 del Decreto 1077 de 2015, podrán ejercer Su derecho a través
de los canales de comunicación tanto físicos como electrónicos dispuestos por esta Curaduría, los cuales 
se señalan a continuación:

* info@curaduriaurbanasmta.com
*juridica@curaduriaurbanasmta.com
*Dirección Física: Calle 25 No. 4-52, Barrio El Prado Calle 25 4 52"""

font_path = "arial.ttf"  # Ruta a la fuente TTF
font_size = 50  # Tamaño de la fuente para el primer texto
font_size_secondary = 35  # Tamaño de la fuente para el segundo texto
font_size_third = 30  # Tamaño de la fuente para el tercer texto
text_color = "black"  # Color del texto

# Crear una imagen en blanco
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# Cargar la fuente
font = ImageFont.truetype(font_path, font_size)
font_secondary = ImageFont.truetype(font_path, font_size_secondary)
font_third = ImageFont.truetype(font_path, font_size_third)

# Calcular la posición del primer texto para centrarlo en la parte superior
text1_width, text1_height = draw.textsize(text1, font=font)
x1 = (width - text1_width) // 2
y1 = 40  # Margen superior para el primer texto

# Dibujar el primer texto en la imagen
draw.text((x1, y1), text1, font=font, fill=text_color)

# Calcular la posición del segundo texto
y2 = y1 + text1_height + margin_top  # Margen de 20 píxeles debajo del primer texto

# Dibujar el segundo texto en la imagen
draw.text((40, y2), text2, font=font_secondary, fill=text_color)  # Justificado a la izquierda con un margen de 40 píxeles

# Calcular la posición del tercer texto
text2_width, text2_height = draw.textsize(text2, font=font_secondary)
y3 = y2 + text2_height + margin_between_texts  # Margen de 30 píxeles debajo del segundo texto
text3_width, text3_height = draw.textsize(text3, font=font_third)
x3 = (width - text3_width) // 2

# Dibujar el tercer texto en la imagen
draw.text((x3, y3), text3, font=font_third, fill=text_color)  # Centrado

# Guardar la imagen como JPG
image.save("output_with_three_texts.jpg")

print("Imagen creada y guardada como output_with_three_texts.jpg")
