from typing import List, Tuple

from logger import logger
from core.calculation import format_number_value


def format_difference_tuple(data: Tuple) -> Tuple:
    """
    Formatea una tupla de diferencia para su uso posterior.

    Args:
        data: Tupla con (índice, monto calculado, monto original)

    Returns:
        Tupla formateada
    """
    # Validar que data sea una tupla y tenga 3 elementos
    if not isinstance(data, tuple) or len(data) != 3:
        error_msg = "Input must be a tuple with exactly 3 elements."
        logger.error(error_msg)
        raise ValueError(error_msg)

    index, total_summed_amount, original_amount = data
    logger.debug(
        f"Formateando diferencia: línea={index}, calculado={total_summed_amount}, original={original_amount}"
    )

    # Formatear los valores usando format_number_value
    formatted_summed = format_number_value(total_summed_amount, 15)
    formatted_original = format_number_value(original_amount, 15)
    logger.debug(
        f"Valores formateados: calculado='{formatted_summed}', original='{formatted_original}'"
    )

    # Retornar la tupla con los valores procesados
    return index, formatted_summed, formatted_original


def format_difference_tuples(list_of_tuples: List[Tuple]) -> List[Tuple]:
    """
    Formatea una lista de tuplas de diferencias.

    Args:
        list_of_tuples: Lista de tuplas con diferencias

    Returns:
        Lista de tuplas formateadas
    """
    logger.info(f"Formateando {len(list_of_tuples)} tuplas de diferencias")
    # Usar list comprehension para procesar cada tupla
    return [format_difference_tuple(item) for item in list_of_tuples]


def replace_values_in_file(
    list_of_values: List[Tuple], file_name: str, output_path: str
) -> None:
    """
    Reemplaza valores en un archivo según una lista de tuplas con diferencias.

    Args:
        list_of_values: Lista de tuplas con diferencias (línea, valor nuevo, valor original)
        file_name: Ruta al archivo a modificar
        output_path: Ruta donde guardar el archivo modificado
    """
    logger.info(f"Reemplazando valores en el archivo {file_name}")
    # Format values into tuples
    list_of_values = format_difference_tuples(list_of_values)
    logger.debug(f"Valores formateados: {list_of_values}")

    try:
        # Leer todas las líneas del archivo
        with open(file_name, "r") as file:
            lines = file.readlines()
            logger.debug(f"Archivo leído: {len(lines)} líneas")

        # Reemplazar las líneas según los valores de la lista
        replacements_count = 0
        for line_num, new_value, old_value in list_of_values:
            # Convertir el número de línea a entero y ajustar al índice de lista (0-indexed)
            line_index = int(line_num) - 1

            # Verificar si la línea está dentro del rango válido
            if 0 <= line_index < len(lines):
                # Verificar si la línea contiene el valor a reemplazar
                if old_value in lines[line_index]:
                    # Reemplazar el valor antiguo por el nuevo
                    lines[line_index] = lines[line_index].replace(old_value, new_value)
                    replacements_count += 1
                    logger.debug(
                        f"Reemplazo en línea {line_num}: '{old_value}' -> '{new_value}'"
                    )
                else:
                    logger.warning(
                        f"No se encontró el valor '{old_value}' en la línea {line_num}"
                    )
            else:
                logger.warning(
                    f"Índice de línea fuera de rango: {line_index} (máx: {len(lines) - 1})"
                )

        # Generar un nuevo nombre para el archivo modificado
        modified_file_name = (
            f"{output_path}/{file_name.split('/')[-1].split('.')[0]}_modificated.txt"
        )

        # Escribir las líneas modificadas en el nuevo archivo
        with open(modified_file_name, "w", encoding="ISO-8859-1") as file:
            file.writelines(lines)
            logger.info(f"Archivo modificado guardado como {modified_file_name}")
            logger.info(f"Total de reemplazos realizados: {replacements_count}")

    except Exception as e:
        logger.exception(f"Error al reemplazar valores en el archivo: {e}")
        raise
