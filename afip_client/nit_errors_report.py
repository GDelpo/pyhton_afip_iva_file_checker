import logging
import os

from dotenv import load_dotenv

from afip_client.afip_service import AFIPService
from afip_client.utils import INSCRIPTION_ERROR_KEYS

# Load environment variables from the .env file
load_dotenv()

logger = logging.getLogger(__name__)


def filter_errors(dictionary, error_msgs):
    """
    Receives a dictionary and an error message (or a list of error messages),
    and returns a list of keys whose values (or any element within them, if they're lists)
    contain one or more of the error messages.

    Args:
        dictionary (dict): The dictionary with data.
        error_msgs (str or list): The error message or list of error messages to search for.

    Returns:
        list: A list of keys that contain at least one of the error messages.
    """
    # If error_msgs is not a list, convert it to a list
    if not isinstance(error_msgs, list):
        error_msgs = [error_msgs]

    keys_with_error = []

    for key, value in dictionary.items():
        if isinstance(value, list):
            for error_msg in error_msgs:
                if any(error_msg in item for item in value):
                    keys_with_error.append(key)
                    break  # Stop checking further messages for this key
        elif isinstance(value, str):
            for error_msg in error_msgs:
                if error_msg in value:
                    keys_with_error.append(key)
                    break  # Stop checking further messages for this key

    return keys_with_error


def identify_error_documents(nit_list) -> None:
    """
    Main function that reads configuration, processes the data from AFIPService,
    accumulates errors, filters successful records, and saves JSON reports.
    """
    try:
        # Read parameters from environment variables (or use default values if
        # needed)
        username = os.getenv("AFIP_USERNAME")
        password = os.getenv("AFIP_PASSWORD")
        base_url = os.getenv("AFIP_BASE_URL")
        chunk_size = int(os.getenv("AFIP_CHUNK_SIZE"))
        max_calls = int(os.getenv("AFIP_MAX_CALLS"))
        pause_duration = int(os.getenv("AFIP_PAUSE_DURATION"))
        max_retries = int(os.getenv("AFIP_MAX_RETRIES"))
        retry_delay = int(os.getenv("AFIP_RETRY_DELAY"))
        # For 'AFIP_SERVICES_AVAILABLE', assume it's a comma-separated list in
        # the .env file
        services_available = os.getenv("AFIP_SERVICES_AVAILABLE", "").split(",")
        # Log the total number of NITs to consult
        logger.info("Total NITs to consult: %d", len(nit_list))
    except Exception as e:
        logger.error("Error reading configuration or Excel file: %s", str(e))
        return

    # Create an instance of AFIPService with the provided parameters
    service = AFIPService(
        username=username,
        password=password,
        base_url=base_url,
        chunk_size=chunk_size,
        max_calls=max_calls,
        pause_duration=pause_duration,
        max_retries=max_retries,
        retry_delay=retry_delay,
        services_available=services_available,
    )
    # Fetch data from the AFIP service
    fetched_data = service.fetch_data_service("inscription", nit_list)
    logger.info("Data fetched: %d records", len(fetched_data))

    # Accumulate errors found in the fetched data
    data_with_error = service.accumulate_errors_in_data(
        fetched_data, INSCRIPTION_ERROR_KEYS
    )
    logger.info("Records with errors: %d", len(data_with_error))
    # Filter out the records with errors from the fetched data
    error_message = ["No existe persona con ese Id", "La clave se encuentra inactiva"]
    key_with_error_msg = filter_errors(data_with_error, error_message)
    logger.info("Records with errors message: %s", key_with_error_msg)
    logger.info("Process completed.")
    return key_with_error_msg
