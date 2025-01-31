import re
import csv

# Abrir archivo HTML
def cargar_html(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return f.read()

# Buscar productos y URLs de imágenes
def extraer_productos(html):
    # Buscar productos en la estructura de la página
    regex_producto = r'<article class="product_pod">(.*?)</article>'
    regex_nombre = r'<h3><a[^>]*title="([^"]+)"'
    regex_imagen = r'<img[^>]*src="([^"]+)"'

    # Encontrar todos los contenedores de productos
    productos_containers = re.finditer(regex_producto, html, re.DOTALL)
    productos = []

    # Debug info
    print("Analizando HTML...")

    for producto in productos_containers:
        contenido = producto.group(1)
        # Extraer el nombre
        nombre_match = re.search(regex_nombre, contenido)
        # Extraer la URL de la imagen
        imagen_match = re.search(regex_imagen, contenido)

        if nombre_match and imagen_match:
            nombre = nombre_match.group(1).strip()
            imagen_url = imagen_match.group(1)
            # Completar la URL si es relativa
            if imagen_url.startswith('../'):
                imagen_url = 'https://books.toscrape.com/' + imagen_url.replace('../', '')
            elif imagen_url.startswith('./'):
                imagen_url = 'https://books.toscrape.com/' + imagen_url.replace('./', '')
            productos.append((nombre, imagen_url))

    print(f"Productos encontrados: {len(productos)}")
    if len(productos) == 0:
        print("\nMostrando las primeras 200 caracteres del HTML para debug:")
        print(html[:500])
        print("\nBuscando cualquier tag de imagen:")
        todas_imgs = re.findall(r'<img[^>]+>', html)
        print(f"Total de tags img encontrados: {len(todas_imgs)}")
        if len(todas_imgs) > 0:
            print("Primera imagen encontrada:")
            print(todas_imgs[0])

    return productos

# Exportar resultados a CSV
def exportar_csv(productos, archivo_salida):
    with open(archivo_salida, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nombre del Producto", "URL de la Imagen"])
        writer.writerows(productos)

# Ejecutar el script
if __name__ == "__main__":
    archivo_html = "BookstoScrapehtml.html"  
    archivo_csv = "productos.csv"

    html = cargar_html(archivo_html)
    productos = extraer_productos(html)
    exportar_csv(productos, archivo_csv)

    print(f"Se han extraído {len(productos)} productos y se han guardado en {archivo_csv}")
