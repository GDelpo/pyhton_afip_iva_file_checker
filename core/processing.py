from collections import OrderedDict
from typing import List, Dict

from logger import logger
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.book_utils import get_book_length, get_book_structure, retrieve_keys_to_sum
from core.exceptions import BookProcessingError
from core.extraction import extract_values_from_string
from core.calculation import calculate_field_totals


def process_book_file(file_name: str, name_of_book: str) -> List[Dict]:
    """
    Procesa un archivo de libro IVA, extrayendo y calculando valores.

    Args:
        file_name: Ruta al archivo a procesar
        name_of_book: Clave del tipo de libro

    Returns:
        Lista de diccionarios con los datos procesados
    """
    logger.info(f"Procesando archivo {file_name} como {name_of_book}")
    list_of_data = []
    try:
        expected_length = get_book_length(name_of_book)
        logger.debug(
            f"Longitud esperada para {name_of_book}: {expected_length} caracteres"
        )

        with open(file_name, "r") as file:
            for index, line in enumerate(file, start=1):
                logger.debug(f"Procesando línea {index} (longitud: {len(line) - 1})")

                # Verificar longitud de línea
                if len(line) - 1 != expected_length:
                    error_msg = (
                        f"La longitud de la línea {index} no coincide con la longitud esperada para el libro {name_of_book}. "
                        f"Longitud actual: {len(line)}, longitud esperada: {expected_length}"
                    )
                    logger.error(error_msg)
                    raise BookProcessingError(error_msg)

                # Procesar línea
                line = line.strip()
                book_structure = get_book_structure(name_of_book)
                extracted_values = extract_values_from_string(line, book_structure)

                # Calcular totales
                keys_to_sum = retrieve_keys_to_sum(name_of_book)
                calculated_values = calculate_field_totals(
                    extracted_values, keys_to_sum
                )

                # Guardar resultados
                dict_of_line = {str(index): calculated_values}
                list_of_data.append(dict_of_line)
                logger.debug(f"Línea {index} procesada correctamente")

        logger.info(f"Archivo procesado. Total de líneas: {len(list_of_data)}")
        return list_of_data

    except FileNotFoundError:
        error_msg = f"No se encontró el archivo {file_name}."
        logger.error(error_msg)
        raise BookProcessingError(error_msg)
    except BookProcessingError as e:
        logger.error(f"Error de procesamiento: {e.message}")
        raise e
    except Exception as e:
        error_msg = f"Ocurrió un error inesperado: {str(e)}"
        logger.exception(error_msg)
        raise BookProcessingError(error_msg) from e


def merge_books_by_line_number(
    dict_list_1: List[Dict], dict_list_2: List[Dict], book_1_key: str, book_2_key: str
) -> OrderedDict:
    """
    Fusiona dos listas de diccionarios en un único diccionario ordenado por número de línea.

    Args:
        dict_list_1: Primera lista de diccionarios
        dict_list_2: Segunda lista de diccionarios
        book_1_key: Clave para identificar la primera lista
        book_2_key: Clave para identificar la segunda lista

    Returns:
        Diccionario ordenado con los datos fusionados
    """
    logger.info(f"Fusionando libros {book_1_key} y {book_2_key}")
    merged_dict = OrderedDict()

    # Recorrer la primera lista de diccionarios
    for item_1 in dict_list_1:
        for key, value in item_1.items():
            if key not in merged_dict:
                merged_dict[key] = OrderedDict()
            merged_dict[key][book_1_key] = value
            logger.debug(f"Agregando línea {key} de {book_1_key}")

    # Recorrer la segunda lista de diccionarios
    for item_2 in dict_list_2:
        for key, value in item_2.items():
            if key in merged_dict:
                merged_dict[key][book_2_key] = value
                logger.debug(f"Agregando línea {key} de {book_2_key} (existente)")
            else:
                merged_dict[key] = OrderedDict()
                merged_dict[key][book_2_key] = value
                logger.debug(f"Agregando línea {key} de {book_2_key} (nueva)")

    logger.info(f"Fusión completada. Total de líneas: {len(merged_dict)}")
    return merged_dict


def add_total_summed_amounts(
    merged_dict: OrderedDict, book_1_key: str, book_2_key: str
) -> OrderedDict:
    """
    Añade los totales sumados de ambos libros a un diccionario fusionado.

    Args:
        merged_dict: Diccionario fusionado con datos de ambos libros
        book_1_key: Clave del primer libro
        book_2_key: Clave del segundo libro

    Returns:
        Diccionario ordenado con los totales sumados añadidos
    """
    logger.info("Calculando totales sumados para el diccionario fusionado")

    for key, value in merged_dict.items():
        total_sum = 0

        # Sumar los valores de summed_amounts en el primer libro
        if book_1_key in value:
            book1_summed_amounts = value[book_1_key].get("summed_amounts", {})
            book1_total = book1_summed_amounts.get("total", 0)
            total_sum += book1_total
            logger.debug(f"Línea {key}: total de {book_1_key} = {book1_total}")

        # Sumar los valores de summed_amounts en el segundo libro
        if book_2_key in value:
            book2_summed_amounts = value[book_2_key].get("summed_amounts", {})
            book2_total = book2_summed_amounts.get("total", 0)
            total_sum += book2_total
            logger.debug(f"Línea {key}: total de {book_2_key} = {book2_total}")

        # Agregar el total sumado en el diccionario principal
        rounded_total = round(total_sum, 2)
        value["total_summed_amount"] = rounded_total
        logger.debug(f"Línea {key}: total sumado = {rounded_total}")

    logger.info("Totales sumados calculados correctamente")
    return merged_dict


def merge_books_and_add_total_summed_amounts(
    dict_list_1: List[Dict], dict_list_2: List[Dict], book_1_key: str, book_2_key: str
) -> OrderedDict:
    """
    Fusiona dos listas de diccionarios y añade los totales sumados.

    Args:
        dict_list_1: Primera lista de diccionarios
        dict_list_2: Segunda lista de diccionarios
        book_1_key: Clave para identificar la primera lista
        book_2_key: Clave para identificar la segunda lista

    Returns:
        Diccionario ordenado con los datos fusionados y totales calculados
    """
    logger.info(
        f"Fusionando libros y calculando totales para {book_1_key} y {book_2_key}"
    )
    merged_dicts = merge_books_by_line_number(
        dict_list_1, dict_list_2, book_1_key, book_2_key
    )
    merged_dicts = add_total_summed_amounts(merged_dicts, book_1_key, book_2_key)
    return merged_dicts
