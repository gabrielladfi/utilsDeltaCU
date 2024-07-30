import pdfkit
from jinja2 import Template
from html_template1 import html_template


# Datos para reemplazar en la plantilla
data = {
    "dia": "Lunes",
    "num_dia": "5",
    "nombre_radicador": "Juan Pérez",
    "tel_radicador": "555-555-555"
}

# Renderizar la plantilla con los datos
template = Template(html_template)
html_out = template.render(data)

# Guardar la salida HTML a un archivo (opcional)
with open("output.html", "w") as file:
    file.write(html_out)


# Opciones para pdfkit (especificar el tamaño de la página y habilitar acceso a archivos locales)
options = {
    'page-size': 'Letter',
    'encoding': 'UTF-8',
    'enable-local-file-access': None
}

# Convertir HTML a PDF
pdfkit.from_string(html_out, 'output.pdf',  options=options)
