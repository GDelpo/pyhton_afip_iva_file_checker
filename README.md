# Procesamiento de Libros IVA (AFIP)

Este proyecto permite procesar archivos de libros de IVA Ventas y Compras, validando formatos, calculando totales, detectando discrepancias (incluyendo validaciones contra los servicios de AFIP) y generando reportes automáticos. Incluye:

- **Lógica modular** en `core/` para parsing, cálculos, formateo de diferencias y generación de reportes.  
- **Cliente HTTP** en `afip_client/` con retries y limpieza de respuestas para verificar documentos en los servicios “inscription” y “padron” de AFIP.  
- **Interfaz de línea de comandos** vía `orchestrator.py`.  
- **Interfaz gráfica** (GUI) basada en Tkinter en `ui.py`.  
- **Logging estructurado** en consola y archivo diario (`logs/afip_iva_checker_YYYYMMDD.log`).

---

## 🗂️ Estructura del Proyecto

```
.
├── .env                  # Variables de configuración y credenciales (no versionar)
├── .env.example          # Ejemplo de archivo .env
├── .gitignore
├── README.md
├── logger.py             # Configuración central de logging
├── orchestrator.py       # Punto de entrada CLI
├── ui.py                 # GUI con Tkinter
├── afip\_client/         # Cliente HTTP a servicios AFIP
│   ├── afip\_service.py
│   ├── error\_detector.py
│   └── error\_utils.py
├── core/                 # Procesamiento de libros IVA
│   ├── book\_parser.py
│   ├── book\_merger.py
│   ├── diff\_formatter.py
│   ├── error\_document\_mapper.py
│   ├── field\_calculator.py
│   ├── file\_writer.py
│   ├── report\_generator.py
│   ├── string\_utils.py
│   ├── value\_extractor.py
│   └── exceptions.py
├── models/               # Utilidades y definiciones de estructura de libros
│   ├── book\_utils.py
│   └── models.py
└── logs/                 # Directorio donde se almacenan los archivos de log

````

---

## ⚙️ Requisitos

- **Python 3.8+**  
- Paquetes en `requirements.txt` (crear con `pip freeze > requirements.txt`), entre ellos:
  ```bash
  requests
  python-dotenv
````

* **Tkinter** (viene con la mayoría de distribuciones de Python).

---

## 🔧 Configuración

1. Copia `.env.example` a `.env`:

   ```bash
   cp .env.example .env
   ```
2. Edita `.env` con tus credenciales y parámetros:

   ```ini
   AFIP_USERNAME=mi_usuario
   AFIP_PASSWORD=mi_clave
   AFIP_BASE_URL=https://api.afip.gob.ar
   AFIP_CHUNK_SIZE=100
   AFIP_MAX_CALLS=5
   AFIP_PAUSE_DURATION=2
   AFIP_MAX_RETRIES=3
   AFIP_RETRY_DELAY=1
   AFIP_SERVICES_AVAILABLE=inscription,padron
   ```
3. Instala dependencias:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Uso

### 1. Desde Línea de Comandos

```bash
python orchestrator.py \
  <ruta_libro_ventas.txt> <clave_libro_ventas> \
  <ruta_libro_compras.txt> <clave_libro_compras> \
  <carpeta_salida>
```

* `<clave_libro_ventas>` y `<clave_libro_compras>` corresponden a las claves esperadas (p. ej. `libro_iva_digital_ventas_cbte`).
* Se generará en la carpeta de salida:

  * El archivo modificado con sufijo `_modificated`.
  * Un reporte JSON `final_report_YYYY-MM-DD.json`.

> **Tip**: Si quieres personalizar nombres o integrarlo en otro CLI, edita el bloque `if __name__ == "__main__":` de `orchestrator.py`.

---

### 2. Interfaz Gráfica (Tkinter)

```bash
python ui.py
```

1. Selecciona los archivos de ventas y compras.
2. Define la carpeta de destino.
3. Haz clic en **“Ejecutar proceso”**.

Los resultados aparecerán en la carpeta seleccionada.

---

## 📑 Detalles Internos

1. **Parsing** (`core/book_parser.py`):

   * Valida longitud de cada línea según la definición en `models/book_utils.py`.
   * Extrae y formatea campos con `value_extractor`.
   * Calcula totales parciales con `field_calculator`.

2. **Fusión y Cálculos** (`core/book_merger.py`):

   * Combina línea a línea los dos libros.
   * Añade el total sumado de campos específicos.

3. **Detección de discrepancias** (`core/diff_formatter.py` / `core/field_calculator.py`):

   * Compara totales calculados vs. originales.
   * Formatea los valores para escritura directa en el archivo de origen.

4. **Validación AFIP** (`afip_client/`):

   * Consulta los servicios `inscription`/`padron`.
   * Reintentos con backoff exponencial y pausa tras X llamadas.
   * Limpieza de la respuesta y acumulación de errores.

5. **Reemplazo de valores** (`core/file_writer.py`):

   * Lee y sobreescribe las líneas que difieren, generando un nuevo archivo.

6. **Reporte final** (`core/report_generator.py`):

   * JSON con datos procesados, discrepancias y fecha de ejecución.

---

## 🐞 Errores Comunes

* **Longitud de línea incorrecta**:
  El parser lanzará `ProcessingError` si la línea no coincide con la longitud esperada.
* **Credenciales AFIP inválidas**:
  Verifica tus variables en `.env` y la conectividad a `AFIP_BASE_URL`.
* **Sin diferencias detectadas**:
  No se generará archivo modificado, pero sí un reporte con `"No differences found"`.

---

## 🤝 Contribuciones

¡Todas las mejoras son bienvenidas! Para colaborar:

1. Abre un **issue** describiendo tu propuesta.
2. Crea un **branch** y envía un **pull request**.

Por favor, asegúrate de incluir siempre **tests** y actualizar la documentación.