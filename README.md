# Procesamiento de Archivos IVA AFIP  
Este proyecto permite procesar archivos relacionados con libros de IVA Ventas y Compras, utilizando una lógica avanzada para verificar la estructura, sumar valores, detectar discrepancias, y generar reportes. Incluye una interfaz gráfica (GUI) desarrollada con **Tkinter** para facilitar la interacción con el usuario.

## Estructura del Proyecto

- **`checker_file.py`**: Contiene toda la lógica del procesamiento de los libros IVA. Extrae datos, verifica formatos y genera reportes.
- **`gui.py`**: Implementa una interfaz gráfica con Tkinter para facilitar la selección de archivos y la ejecución del proceso.

---

## Requisitos Previos

1. **Python 3.8 o superior**  
2. Instalación de los paquetes necesarios:
   ```bash
   pip install tk
   ```

---

## Estructura de Archivos y Directorios

- **Archivos de Entrada**: Archivos de texto (.txt) con los formatos:
  - `ventas_cbte_YYYYMM.txt`  
  - `ventas_alicuota_YYYYMM.txt`  

- **Salida**:  
  - Un archivo modificado del libro IVA ventas.  
  - Un reporte en formato `.json` con las discrepancias detectadas.

---

## Ejecución del Proyecto

### Opción 1: Ejecución con Interfaz Gráfica  
1. Ejecuta el archivo `gui.py`:
   ```bash
   python gui.py
   ```
2. Sigue las instrucciones en la interfaz para seleccionar los archivos de IVA ventas y alícuotas, y define la carpeta de destino.  
3. Haz clic en **"Ejecutar proceso"** para completar la operación.  
4. Revisa los archivos generados en la carpeta de destino.

### Opción 2: Ejecución desde Línea de Comandos  
1. Modifica el bloque `if __name__ == "__main__"` en `checker_file.py` para proporcionar los archivos y claves de libros deseados:
   ```python
   list_of_ventas_cbte = process_file('ventas_cbte202210.txt', 'libro_iva_digital_ventas_cbte')
   list_of_ventas_alicuota = process_file('ventas_alicuota_202210.txt', 'libro_iva_digital_ventas_alicuota')
   ```
2. Ejecuta el archivo directamente:
   ```bash
   python checker_file.py
   ```

---

## Descripción de la Lógica

- **Extracción de Datos:**  
  Usa posiciones definidas en el diccionario `BOOKS` para extraer datos específicos de cada línea del archivo.

- **Cálculo de Totales:**  
  La función `calculate_total_values` suma los valores relevantes para los campos especificados.

- **Fusión de Libros:**  
  Utiliza `merge_books_by_key` para combinar los datos de ventas y alícuotas en un solo diccionario.

- **Detección de Discrepancias:**  
  Detecta diferencias entre valores calculados y reales usando `find_total_differences`.

- **Generación de Reportes:**  
  Genera un archivo `.json` con los resultados del proceso.

---

## Posibles Errores y Solución de Problemas

- **Error: "La longitud de la línea no coincide..."**  
  Verifica que el archivo tenga el formato correcto y que cada línea tenga la longitud esperada.

- **Error de Archivo no Encontrado:**  
  Asegúrate de proporcionar rutas válidas para los archivos de entrada.

---

## Ejemplo de Uso

1. Archivo de ventas: `ventas_cbte202210.txt`  
2. Archivo de alícuotas: `ventas_alicuota_202210.txt`  
3. Carpeta de salida: `/ruta/de/destino/`

---

## Contribuciones

Si encuentras errores o tienes ideas para mejorar el proyecto, no dudes en abrir un **issue** o enviar un **pull request**.
