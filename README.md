# Web Scraping - Extracción de Productos

Este proyecto realiza **web scraping** en una página web de comercio electrónico para extraer nombres de productos y sus URLs de imagen, generando un archivo CSV con la información obtenida.

## Tecnologías Utilizadas
- **Python 3.x**
- **Expresiones Regulares (re)** para el procesamiento del HTML
- **Módulo CSV** para la exportación de datos


## Instalación y Ejecución
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. **Ejecutar el script:**
   ```bash
   python webscraping.py
   ```

## Funcionamiento del Script

1. **Carga el archivo HTML**:
   - Abre y lee el contenido de un archivo local con la estructura de la tienda en línea.

2. **Extrae los productos y sus imágenes**:
   - Utiliza **expresiones regulares (regex)** para identificar contenedores de productos.
   - Extrae los **nombres de los productos** desde el atributo `title` de los enlaces `<a>`.
   - Obtiene las **URLs de las imágenes** desde el atributo `src` de las etiquetas `<img>`.
   - Convierte URLs relativas en **URLs absolutas**.

3. **Exporta los datos a un archivo CSV**:
   - Guarda la información en `output/productos.csv` con dos columnas: `Nombre del Producto` y `URL de la Imagen`.

## Ejemplo de Salida CSV

```
Nombre del Producto,URL de la Imagen
"A Light in the Attic","https://books.toscrape.com/media/cache/..."
"Another Book","https://books.toscrape.com/media/cache/..."
```

## Posibles Errores y Soluciones
- **El script no encuentra productos:** Verifica que el archivo HTML descargado contenga la estructura correcta.
- **Las URLs de las imágenes son incorrectas:** Asegúrate de que la construcción de URLs absolutas es correcta.
- **El archivo CSV está vacío:** Revisa las expresiones regulares y prueba con `print()` para depurar.

## Mejoras Futuras
- Implementar **BeautifulSoup** en lugar de regex para mejorar la robustez del parsing.
- Agregar soporte para paginación y extracción de múltiples páginas.
- Guardar información adicional como precios y descripciones.

## Licencia
Este proyecto se distribuye bajo la licencia MIT.

---

**Autor:** Tu Nombre  
**Repositorio:** [GitHub](https://github.com/tu-usuario/tu-repositorio)

