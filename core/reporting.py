from datetime import datetime
import json
from typing import Dict, List, Tuple, Any, Union
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.exceptions import BookProcessingError

def generate_final_report(
    processed_data: Dict[str, Any],
    difference_tuples: List[Tuple[int, Any, Any]],
    output_path: Union[str, None] = None,
) -> str:
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
        str: Message indicating the results of the report generation
    """
    message = ""
    try:
        # Create the base structure of the report
        final_output = {
            "processed_data": {"total": len(processed_data), "data": processed_data},
            "query_date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        }

        # Add differences if they exist
        if difference_tuples:
            differences_report = {
                t[0]: {"correct_value": t[1], "actual_value": t[2]}
                for t in difference_tuples
            }
            final_output["differences_into_data"] = {
                "total": len(difference_tuples),
                "lines_with_error": differences_report,
            }
            message += (
                f"{len(difference_tuples)} differences found and added to the report. "
            )
        else:
            message += "No differences found. Report will contain only processed data. "

        # Use a default filename if no path is provided
        output_path += f"/final_report_{datetime.now().strftime('%Y-%m-%d')}.json"

        # Save the report as a JSON file
        with open(output_path, "w") as output_file:
            json.dump(final_output, output_file, indent=1)

        message += f"Report successfully saved to {output_path}."
        return message

    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        raise BookProcessingError(error_message) from e
