from datetime import datetime
import json
from typing import Dict, List, Tuple, Any, Union
import math
from collections import OrderedDict

class BookProcessingError(Exception):
    """Excepción personalizada para errores durante el procesamiento de libros."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message


BOOKS = {
    'libro_iva_digital_ventas_cbte':{
        1: {
        "Campo": "Fecha de comprobante",
        "Posiciones": (0, 7),
        "Tipo de Dato": "Numérico",
        "Longitud": 8,
        "Observaciones": "AAAAMMDD"
        },
        2: {
            "Campo": "Tipo de comprobante",
            "Posiciones": (8, 10),
            "Tipo de Dato": "Numérico",
            "Longitud": 3,
            "Observaciones": "Según tabla Comprobantes Ventas"
        },
        3: {
            "Campo": "Punto de venta",
            "Posiciones": (11, 15),
            "Tipo de Dato": "Numérico",
            "Longitud": 5,
            "Observaciones": None
        },
        4: {
            "Campo": "Número de comprobante",
            "Posiciones": (16, 35),
            "Tipo de Dato": "Numérico",
            "Longitud": 20,
            "Observaciones": None
        },
        5: {
            "Campo": "Número de comprobante hasta",
            "Posiciones": (36, 55),
            "Tipo de Dato": "Numérico",
            "Longitud": 20,
            "Observaciones": None
        },
        6: {
            "Campo": "Código de documento del comprador",
            "Posiciones": (56, 57),
            "Tipo de Dato": "Numérico",
            "Longitud": 2,
            "Observaciones": "Según tabla Documentos"
        },
        7: {
            "Campo": "Número de identificación del comprador",
            "Posiciones": (58, 77),
            "Tipo de Dato": "Alfaumérico",
            "Longitud": 20,
            "Observaciones": "Completar con ceros a la izquierda"
        },
        8: {
            "Campo": "Apellido y nombre o denominación del comprador",
            "Posiciones": (78, 107),
            "Tipo de Dato": "Alfanumérico",
            "Longitud": 30,
            "Observaciones": None
        },
        9: {
            "Campo": "Importe total de la operación",
            "Posiciones": (108, 122),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        10: {
            "Campo": "Importe total de conceptos que no integran el precio neto gravado",
            "Posiciones": (123, 137),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        11: {
            "Campo": "Percepción a no categorizados",
            "Posiciones": (138, 152),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        12: {
            "Campo": "Importe de operaciones exentas",
            "Posiciones": (153, 167),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        13: {
            "Campo": "Importe de percepciones o pagos a cuenta de impuestos nacionales",
            "Posiciones": (168, 182),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        14: {
            "Campo": "Importe de percepciones de ingresos brutos",
            "Posiciones": (183, 197),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        15: {
            "Campo": "Importe de percepciones de impuestos municipales",
            "Posiciones": (198, 212),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        16: {
            "Campo": "Importe de impuestos internos",
            "Posiciones": (213, 227),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        17: {
            "Campo": "Código de moneda",
            "Posiciones": (228, 230),
            "Tipo de Dato": "Alfaumérico",
            "Longitud": 3,
            "Observaciones": "Según tabla Tipo de Monedas"
        },
        18: {
            "Campo": "Tipo de cambio",
            "Posiciones": (231, 240),
            "Tipo de Dato": "Numérico",
            "Longitud": 10,
            "Observaciones": "4 enteros 6 decimales sin punto decimal"
        },
        19: {
            "Campo": "Cantidad de alícuotas de IVA",
            "Posiciones": (241,),
            "Tipo de Dato": "Numérico",
            "Longitud": 1,
            "Observaciones": None
        },
        20: {
            "Campo": "Código de operación",
            "Posiciones": (242,),
            "Tipo de Dato": "Alfabético",
            "Longitud": 1,
            "Observaciones": "Según tabla Código de Operación"
        },
        21: {
            "Campo": "Otros tributos",
            "Posiciones": (243, 257),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        22: {
            "Campo": "Fecha de Vencimiento o Pago",
            "Posiciones": (258, 265),
            "Tipo de Dato": "Numérico",
            "Longitud": 8,
            "Observaciones": "AAAAMMDD"
        }
    },
    'libro_iva_digital_ventas_alicuota': {
        1: {
        "Campo": "Tipo de comprobante",
        "Posiciones": (0, 2),
        "Tipo de Dato": "Numérico",
        "Longitud": 3,
        "Observaciones": "Según tabla de Comprobantes"
        },
        2: {
            "Campo": "Punto de venta",
            "Posiciones": (3, 7),
            "Tipo de Dato": "Numérico",
            "Longitud": 5,
            "Observaciones": None
        },
        3: {
            "Campo": "Número de comprobante",
            "Posiciones": (8, 27),
            "Tipo de Dato": "Numérico",
            "Longitud": 20,
            "Observaciones": None
        },
        4: {
            "Campo": "Importe neto gravado",
            "Posiciones": (28, 42),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        5: {
            "Campo": "Alícuota de IVA",
            "Posiciones": (43, 46),
            "Tipo de Dato": "Numérico",
            "Longitud": 4,
            "Observaciones": "Según tabla Alícuotas"
        },
        6: {
            "Campo": "Impuesto Liquidado",
            "Posiciones": (47, 61),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        }
    },
    'libro_iva_digital_compras_cbte':{
        1: {
        "Campo": "Fecha de comprobante",
        "Posiciones": (0, 7),
        "Tipo de Dato": "Numérico",
        "Longitud": 8,
        "Observaciones": "AAAAMMDD"
        },
        2: {
            "Campo": "Tipo de comprobante",
            "Posiciones": (8, 10),
            "Tipo de Dato": "Numérico",
            "Longitud": 3,
            "Observaciones": "Según tabla Comprobantes Compra"
        },
        3: {
            "Campo": "Punto de venta",
            "Posiciones": (11, 15),
            "Tipo de Dato": "Numérico",
            "Longitud": 5,
            "Observaciones": None
        },
        4: {
            "Campo": "Número de comprobante",
            "Posiciones": (16, 35),
            "Tipo de Dato": "Numérico",
            "Longitud": 20,
            "Observaciones": None
        },
        5: {
            "Campo": "Despacho de importación",
            "Posiciones": (36, 51),
            "Tipo de Dato": "Alfaumérico",
            "Longitud": 16,
            "Observaciones": None
        },
        6: {
            "Campo": "Código de documento del vendedor",
            "Posiciones": (52, 53),
            "Tipo de Dato": "Numérico",
            "Longitud": 2,
            "Observaciones": "Según tabla Documentos"
        },
        7: {
            "Campo": "Número de identificación del vendedor",
            "Posiciones": (54, 73),
            "Tipo de Dato": "Alfaumérico",
            "Longitud": 20,
            "Observaciones": "Completar con ceros a la izquierda"
        },
        8: {
            "Campo": "Apellido y nombre o denominación del vendedor",
            "Posiciones": (74, 103),
            "Tipo de Dato": "Alfanumérico",
            "Longitud": 30,
            "Observaciones": None
        },
        9: {
            "Campo": "Importe total de la operación",
            "Posiciones": (104, 118),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        10: {
            "Campo": "Importe total de conceptos que no integran el precio neto gravado",
            "Posiciones": (119, 133),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        11: {
            "Campo": "Importe de operaciones exentas",
            "Posiciones": (134, 148),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        12: {
            "Campo": "Importe de percepciones o pagos a cuenta del Impuesto al Valor Agregado",
            "Posiciones": (149, 163),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        13: {
            "Campo": "Importe de percepciones o pagos a cuenta de impuestos nacionales",
            "Posiciones": (164, 178),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        14: {
            "Campo": "Importe de percepciones de ingresos brutos",
            "Posiciones": (179, 193),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        15: {
            "Campo": "Importe de percepciones de impuestos municipales",
            "Posiciones": (194, 208),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        16: {
            "Campo": "Importe de impuestos internos",
            "Posiciones": (209, 223),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        17: {
            "Campo": "Código de moneda",
            "Posiciones": (224, 226),
            "Tipo de Dato": "Alfaumérico",
            "Longitud": 3,
            "Observaciones": "Según tabla Tipo de Monedas"
        },
        18: {
            "Campo": "Tipo de cambio",
            "Posiciones": (227, 236),
            "Tipo de Dato": "Numérico",
            "Longitud": 10,
            "Observaciones": "4 enteros 6 decimales sin punto decimal"
        },
        19: {
            "Campo": "Cantidad de alícuotas de IVA",
            "Posiciones": (237,),
            "Tipo de Dato": "Numérico",
            "Longitud": 1,
            "Observaciones": None
        },
        20: {
            "Campo": "Código de operación",
            "Posiciones": (238,),
            "Tipo de Dato": "Alfabético",
            "Longitud": 1,
            "Observaciones": "Según tabla Código de Operación"
        },
        21: {
            "Campo": "Crédito Fiscal Computable",
            "Posiciones": (239, 253),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        22: {
            "Campo": "Otros Tributos",
            "Posiciones": (254, 268),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        23: {
            "Campo": "CUIT emisor/corredor",
            "Posiciones": (269, 279),
            "Tipo de Dato": "Numérico",
            "Longitud": 11,
            "Observaciones": None
        },
        24: {
            "Campo": "Denominación del emisor/corredor",
            "Posiciones": (280, 309),
            "Tipo de Dato": "Alfanumérico",
            "Longitud": 30,
            "Observaciones": None
        },
        25: {
            "Campo": "IVA comisión",
            "Posiciones": (310, 324),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        }
    },
    'libro_iva_digital_compras_alicuota': {
        1: {
        "Campo": "Tipo de comprobante",
        "Posiciones": (0, 2),
        "Tipo de Dato": "Numérico",
        "Longitud": 3,
        "Observaciones": "Según tabla de Comprobantes"
        },
        2: {
            "Campo": "Punto de venta",
            "Posiciones": (3, 7),
            "Tipo de Dato": "Numérico",
            "Longitud": 5,
            "Observaciones": None
        },
        3: {
            "Campo": "Número de comprobante",
            "Posiciones": (8, 27),
            "Tipo de Dato": "Numérico",
            "Longitud": 20,
            "Observaciones": None
        },
        4: {
            "Campo": "Código de documento del vendedor",
            "Posiciones": (28, 29),
            "Tipo de Dato": "Numérico",
            "Longitud": 2,
            "Observaciones": "Según tabla Documentos"
        },
        5: {
            "Campo": "Número de identificación del Vendedor",
            "Posiciones": (30, 49),
            "Tipo de Dato": "Alfanumérico",
            "Longitud": 20,
            "Observaciones": "Completar con ceros a izquierda"
        },
        6: {
            "Campo": "Importe neto gravado",
            "Posiciones": (50, 64),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        },
        7: {
            "Campo": "Alícuota de IVA",
            "Posiciones": (65, 68),
            "Tipo de Dato": "Numérico",
            "Longitud": 4,
            "Observaciones": "Según tabla de Alícuotas"
        },
        8: {
            "Campo": "Impuesto liquidado",
            "Posiciones": (69, 83),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal"
        }
    },
}

def extract_value_by_positions(data_string, positions):
    if len(positions) == 2:
        start_position, end_position = positions
        return data_string[start_position:end_position + 1]
    else:
        start_position = positions[0]
        return data_string[start_position]
    
def format_value_by_observation(value, decimal_index):
    value = value.strip()
    integer_part = value[:-decimal_index]
    decimal_part = value[-decimal_index:]
    return f"{int(integer_part)}.{decimal_part}"

# Función para extraer valores de una cadena utilizando el diccionario
def extract_values_from_string(data_string, field_structure):
    """
    Extrae valores de una cadena de acuerdo a una estructura de campo definida, aplicando 
    formateo para los casos de decimales sin punto (13 enteros y 2 decimales, 4 enteros y 6 decimales).
    
    Args:
        data_string (str): Cadena de datos que contiene los valores a extraer.
        field_structure (dict): Diccionario que define las posiciones y observaciones de cada campo.
    
    Returns:
        dict: Un diccionario que contiene el número de campo, el nombre y el valor formateado.
    """
    extracted_values = {}
    
    for field_number, field_info in field_structure.items():
        field_positions = field_info["Posiciones"]
        field_name = field_info["Campo"]
        field_observations = field_info.get("Observaciones")  # Usamos .get() para evitar errores si no hay observaciones

        field_value = extract_value_by_positions(data_string, field_positions)

        # Verificamos si hay observaciones que requieren un formato específico
        if field_observations:
            match field_observations:
                case '13 enteros 2 decimales sin punto decimal':
                    decimal_index = 2  # Para valores con 13 enteros y 2 decimales
                case '4 enteros 6 decimales sin punto decimal':
                    decimal_index = 6  # Para valores con 4 enteros y 6 decimales
                case 'Completar con ceros a izquierda':
                    field_value = field_value.lstrip('0')
                case _:
                    decimal_index = None  # Si no coincide con ninguno, no hacemos formateo especial

            if decimal_index is not None:
                # Formateamos el valor como un número decimal
                field_value = format_value_by_observation(field_value, decimal_index)            
        
        # Guardamos el resultado en el diccionario de valores extraídos
        extracted_values[field_number] = {"field_name": field_name, "value": field_value.strip()}  # Elimina espacios adicionales

    return extracted_values

def calculate_total_values(data_dict, keys_to_sum):
    total_sum = 0
    for key in keys_to_sum:
        total_sum += float(data_dict[key]['value'])
    
    data_dict['summed_amounts'] = {
        'referenced_fields': ', '.join(map(str, keys_to_sum)).strip(),
        'total': round(total_sum, 2)
    }
    
    return data_dict

def retrieve_keys_to_sum(name_of_book):
    list_of_keys = []

    match name_of_book:
        case 'libro_iva_digital_ventas_cbte':
            list_of_keys = [10, 11, 12, 13, 14, 15, 16, 21]
        case 'libro_iva_digital_ventas_alicuota':
            list_of_keys = [4, 6]
        case 'libro_iva_digital_compras_cbte':
            list_of_keys = [10, 11, 12, 13, 14, 15, 16, 21, 22, 25]
        case 'libro_iva_digital_compras_alicuota':
            list_of_keys = [6, 8]

    return list_of_keys

def get_book_structure(name_of_book):
    return BOOKS[name_of_book]

def get_book_len(name_of_book):
    len_of_book = 0
    match name_of_book:
        case 'libro_iva_digital_ventas_cbte':
            len_of_book = 266
        case 'libro_iva_digital_ventas_alicuota':
            len_of_book = 62
        case 'libro_iva_digital_compras_cbte':
            len_of_book = 325
        case 'libro_iva_digital_compras_alicuota':
            len_of_book = 84
    return len_of_book


def process_file(file_name, name_of_book):
    list_of_data = []
    try:
        with open(file_name, 'r') as file:
            for index, line in enumerate(file, start=1):
                if len(line) - 1 != get_book_len(name_of_book):
                    raise BookProcessingError(
                        f"La longitud de la línea {index} no coincide con la longitud esperada para el libro {name_of_book}. "
                        f"Longitud actual: {len(line)}, longitud esperada: {get_book_len(name_of_book)}"
                    )
                line = line.strip()
                line = extract_values_from_string(line, get_book_structure(name_of_book))
                line = calculate_total_values(line, retrieve_keys_to_sum(name_of_book))
                dict_of_line = {str(index): line}
                list_of_data.append(dict_of_line)

        return list_of_data

    except FileNotFoundError:
        raise BookProcessingError(f"No se encontró el archivo {file_name}.")
    except BookProcessingError as e:
        raise e
    except Exception as e:
        raise BookProcessingError(f"Ocurrió un error inesperado: {str(e)}")


def merge_books_by_key(dict_list_1, dict_list_2, book_1_key, book_2_key):
    merged_dict = OrderedDict()

    # Recorrer la primera lista de diccionarios
    for item_1 in dict_list_1:
        for key, value in item_1.items():
            if key not in merged_dict:
                merged_dict[key] = OrderedDict()
            merged_dict[key][book_1_key] = value

    # Recorrer la segunda lista de diccionarios
    for item_2 in dict_list_2:
        for key, value in item_2.items():
            if key in merged_dict:
                merged_dict[key][book_2_key] = value
            else:
                merged_dict[key] = OrderedDict()
                merged_dict[key][book_2_key] = value

    return merged_dict

def add_total_summed_amounts(merged_dict, book_1_key, book_2_key):
    for key, value in merged_dict.items():
        total_sum = 0

        # Sumar los valores de summed_amounts en el primer libro
        if book_1_key in value:
            cbte_summed_amounts = value[book_1_key].get('summed_amounts', {})
            total_sum += cbte_summed_amounts.get('total', 0)

        # Sumar los valores de summed_amounts en el segundo libro
        if book_2_key in value:
            alicuota_summed_amounts = value[book_2_key].get('summed_amounts', {})
            total_sum += alicuota_summed_amounts.get('total', 0)

        # Agregar el total sumado en el diccionario principal
        value['total_summed_amount'] = round(total_sum, 2)

    return merged_dict


def check_difference_exceeds_threshold(value1, value2, threshold=1):
    return get_difference(value1, value2) > threshold

def find_total_differences(merged_dict, book_key, field_number=9):
    differences = []

    for key, value in merged_dict.items():
        # Obtener el total_summed_amount
        total_summed_amount = value.get('total_summed_amount', 0)

        # Obtener el valor del campo especificado en el libro proporcionado
        field_value = None
        if book_key in value:
            field_data = value[book_key].get(field_number, {})
            field_value = float(field_data.get('value', 0))

        # Comparar los valores
        if total_summed_amount != field_value:
            if check_difference_exceeds_threshold(total_summed_amount, field_value):
                # Si no coinciden, añadir una tupla con: número de fila (key), total_summed_amount, y field_value
                differences.append((key, total_summed_amount, field_value))

    return differences

def get_difference(value1, value2):
    return abs(value1 - value2)

def format_value(value):
    try:
        # Descomponer el valor en parte decimal y parte entera
        decimals, integer = math.modf(value)

        # Redondear la parte decimal a dos decimales
        decimals = abs(round(decimals, 2))

        # Convertir a string y eliminar el punto decimal
        str_value = f"{int(integer)}{str(decimals)[2:].ljust(2, '0')}"

        # Ajustar a longitud 15
        if len(str_value) < 15:
            diff = 15 - len(str_value)
            str_value = f"{'0' * diff}{str_value}"

        return str_value

    except (ValueError, TypeError) as e:
        print(f"Error: {e}. Asegúrate de que el valor sea numérico.")
        return None
    
def format_difference_tuple(data):
    # Validar que data sea una tupla y tenga 3 elementos
    if not isinstance(data, tuple) or len(data) != 3:
        raise ValueError("Input must be a tuple with exactly 3 elements.")

    index, total_summed_amount, original_amount = data

    # Formatear los valores usando format_value
    total_summed_amount = format_value(total_summed_amount)
    original_amount = format_value(original_amount)
    
    # Retornar la tupla con los valores procesados
    return index, total_summed_amount, original_amount

def format_difference_tuples(list_of_tuples):
    # Usar list comprehension para procesar cada tupla
    return [format_difference_tuple(item) for item in list_of_tuples]

def replace_values_in_file(list_of_values, file_name, output_path):
    # Format values into tuples
    list_of_values = format_difference_tuples(list_of_values)
    # Leer todas las líneas del archivo
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Reemplazar las líneas según los valores de la lista
    for line_num, new_value, old_value in list_of_values:
        # Convertir el número de línea a entero y ajustar al índice de lista (0-indexed)
        line_index = int(line_num) - 1
        # Verificar si la línea contiene el valor a reemplazar
        if old_value in lines[line_index]:
            # Reemplazar el valor antiguo por el nuevo
            lines[line_index] = lines[line_index].replace(old_value, new_value)
    
    # Generar un nuevo nombre para el archivo modificado
    modified_file_name = f'{output_path}/{file_name.split("/")[-1].split(".")[0]}_modificated.txt'
    
    # Escribir las líneas modificadas en el nuevo archivo
    with open(modified_file_name, 'w', encoding='ISO-8859-1') as file:
        file.writelines(lines)



def generate_final_report(
    processed_data: Dict[str, Any], 
    difference_tuples: List[Tuple[int, Any, Any]], 
    output_path: Union[str, None] = None
) -> Tuple[bool, str]:
    """
    Generates a final report with processed data and detected differences,
    and saves it as a JSON file.

    Args:
        processed_data (Dict[str, Any]): Dictionary with merged and processed data.
        difference_tuples (List[Tuple[int, Any, Any]]): List of tuples with differences 
                                                        (line, correct_value, actual_value).
        output_path (Union[str, None], optional): Full path of the output file. If None, 
                                                  a default name with timestamp will be used.

    Returns:
        Tuple[bool, str]: (True, message) if the report is generated successfully, 
                          (False, error message) otherwise.
    """
    message = ""
    try:
        # Create the base structure of the report
        final_output = {
            'processed_data': {
                'total': len(processed_data),
                'data': processed_data
            },
            'query_date': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

        # Add differences if they exist
        if difference_tuples:
            differences_report = {
                t[0]: {'correct_value': t[1], 'actual_value': t[2]} 
                for t in difference_tuples
            }
            final_output['differences_into_data'] = {
                'total': len(difference_tuples),
                'lines_with_error': differences_report
            }
            message += f"{len(difference_tuples)} differences found and added to the report. "
        else:
            message += "No differences found. Report will contain only processed data. "

        # Use a default filename if no path is provided
        output_path+= f"/final_report_{datetime.now().strftime("%Y-%m-%d")}.json"
    
        # Save the report as a JSON file
        with open(output_path, "w") as output_file:
            json.dump(final_output, output_file, indent=1)

        message += f"Report successfully saved to {output_path}."
        return message

    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        raise BookProcessingError(error_message) from e

def complete_process(
    book_1_file_path: str, 
    book_1_key: str, 
    book_2_file_path: str, 
    book_2_key: str,
    output_folder_path: str
) -> bool:
    try:
        list_of_book_1 = process_file(book_1_file_path, book_1_key)
        list_of_book_2 = process_file(book_2_file_path, book_2_key)

        merged_dicts = merge_books_by_key(list_of_book_1, list_of_book_2, book_1_key, book_2_key)
        merged_dicts = add_total_summed_amounts(merged_dicts, book_1_key, book_2_key)
        list_of_differences = find_total_differences(merged_dicts, book_1_key)

        message = generate_final_report(merged_dicts, list_of_differences, output_folder_path)

        if list_of_differences:
            replace_values_in_file(list_of_differences, book_1_file_path, output_folder_path)

        return True, message

    except BookProcessingError as e:
        print(f"Error: {e.message}")
        raise e  # Propagamos la excepción para que la GUI la maneje
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        raise BookProcessingError(f"Error inesperado: {str(e)}")


    
if __name__ == "__main__":
    
    list_of_ventas_cbte = process_file('ventas_cbte202210.txt', 'libro_iva_digital_ventas_cbte')
    list_of_ventas_alicuota = process_file('ventas_alicuota_202210.txt', 'libro_iva_digital_ventas_alicuota')
    merged_dicts = merge_books_by_key(list_of_ventas_cbte, list_of_ventas_alicuota, 'libro_iva_digital_ventas_cbte', 'libro_iva_digital_ventas_alicuota')
    merged_dicts = add_total_summed_amounts(merged_dicts, 'libro_iva_digital_ventas_cbte', 'libro_iva_digital_ventas_alicuota')
    list_of_diferences = find_total_differences(merged_dicts, 'libro_iva_digital_ventas_cbte')
    generate_final_report(merged_dicts, list_of_diferences)
    replace_values_in_file('ventas_cbte202210.txt', list_of_diferences)
    
    