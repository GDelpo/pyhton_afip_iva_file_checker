from typing import Tuple

from afip_client.nit_errors_report import identify_error_documents
from logger import logger
from core.exceptions import BookProcessingError
from core.processing import process_book_file, merge_books_and_add_total_summed_amounts
from core.calculation import find_total_differences, format_len_value
from core.formatting import replace_values_in_file
from core.reporting import generate_final_report
from core.extraction import extract_documents_by_key

def set_new_document_value(document: str) -> str:
    """
    Reemplaza el valor de un documento con un nuevo valor.
    
    Args:
        document: Documento original (string)
        
    Returns:
        Documento con el nuevo valor
    """
    if document[0] == "3":
        generic_document = "30000000007"
    else:
        generic_document = "20222222223"
    return format_len_value(generic_document, 20)

def get_indexed_error_documents(document_list, error_documents_strings):
    """
    Crea una lista de tuplas que contienen el índice y el documento 
    para cada documento que aparece en la lista de documentos con errores.
    
    Args:
        document_list: Lista completa de documentos (enteros)
        error_documents_strings: Lista de documentos con errores (strings)
        
    Returns:
        Lista de tuplas (índice, documento) para documentos con errores
    """
    # Convertir error_documents a un conjunto de enteros para búsqueda eficiente
    error_docs_set = set(int(doc) for doc in error_documents_strings)
    
    indexed_error_documents = []
    for index, doc in enumerate(document_list):
        if doc in error_docs_set:
            index+= 1  # Ajustar el índice para que sea 1-based
            original_doc = format_len_value(str(doc), 20)
            new_doc = set_new_document_value(str(doc))
            # Agregar el índice y el documento a la lista
            indexed_error_documents.append((index, original_doc, new_doc))
    
    return indexed_error_documents

def process_book_comparison(
    book_1_file_path: str,
    book_1_key: str,
    book_2_file_path: str,
    book_2_key: str,
    output_folder_path: str,
) -> Tuple[bool, str]:
    """
    Realiza el proceso completo de comparación entre dos libros IVA.

    Args:
        book_1_file_path: Ruta al primer archivo de libro
        book_1_key: Clave identificadora del primer libro
        book_2_file_path: Ruta al segundo archivo de libro
        book_2_key: Clave identificadora del segundo libro
        output_folder_path: Ruta donde se guardarán los archivos de salida

    Returns:
        Tupla con (éxito, mensaje)
    """
    logger.info(f"Iniciando proceso de comparación entre {book_1_key} y {book_2_key}")

    try:
        logger.info(f"Procesando archivo {book_1_file_path}")
        list_of_book_1 = process_book_file(book_1_file_path, book_1_key)
        logger.info(f"Procesando archivo {book_2_file_path}")
        list_of_book_2 = process_book_file(book_2_file_path, book_2_key)

        if len(list_of_book_1) != len(list_of_book_2):
            difference = abs(len(list_of_book_1) - len(list_of_book_2))
            error_msg = (
                f"Las longitudes no coinciden. Hay {difference} líneas de diferencia. "
                f"El archivo {book_1_key} tiene {len(list_of_book_1)} líneas y "
                f"el archivo {book_2_key} tiene {len(list_of_book_2)} líneas."
            )
            logger.error(error_msg)
            raise BookProcessingError(error_msg)

        logger.info("Fusionando libros y calculando montos totales")
        merged_dicts = merge_books_and_add_total_summed_amounts(
            list_of_book_1, list_of_book_2, book_1_key, book_2_key
        )

        logger.info("Buscando diferencias entre los libros")
        list_of_differences = find_total_differences(merged_dicts, book_1_key)
        logger.info(f"Diferencias encontradas: {list_of_differences}")
        exit(0)
        # Search for documents in the merged dictionary
        docs_extracted = extract_documents_by_key(merged_dicts, book_1_key)
        logger.info(f"Documentos extraídos: {len(docs_extracted)}")
        # Indentify documents with errors
        docs_with_errors = identify_error_documents(docs_extracted)
        logger.info(f"Documentos {len(docs_with_errors)} con errores: {docs_with_errors}")
        # Index documents with errors
        docs_idexed_with_error = get_indexed_error_documents(docs_extracted, docs_with_errors)
        logger.info(f"Documentos indexados {len(docs_idexed_with_error)} con errores: {docs_idexed_with_error}")
        exit(0)
        logger.info(f"Generando reporte final en {output_folder_path}")
        message = generate_final_report(
            merged_dicts, list_of_differences, output_folder_path
        )

        if list_of_differences:
            logger.info(
                f"Se encontraron {len(list_of_differences)} diferencias. Actualizando archivo original."
            )
            #logger.info(list_of_differences)
            # Reemplazamos los valores en el archivo original
            replace_values_in_file(
                list_of_differences, book_1_file_path, output_folder_path
            )
        else:
            logger.info("No se encontraron diferencias entre los libros.")

        logger.info("Proceso completado exitosamente")
        return True, message

    except BookProcessingError as e:
        logger.error(f"Error en el procesamiento: {e.message}")
        raise e  # Propagamos la excepción para que la GUI la maneje
    except Exception as e:
        error_msg = f"Error inesperado: {str(e)}"
        logger.exception(error_msg)
        raise BookProcessingError(error_msg)
