def aggregate_repo_data(extracted_text):
    """
    Aggregates data from extracted text.

    Args:
        extracted_text: List of dictionaries containing extracted information.

    Returns:
        A single string of aggregated data.
    """
    aggregated_data = ""
    for item in extracted_text:
        aggregated_data += f"File: {item['file_name']}\n"
        aggregated_data += f"Functions: {', '.join(item['function_names'])}\n"
        aggregated_data += f"Variables: {', '.join(item['variable_names'])}\n"
        aggregated_data += "\n"

    return aggregated_data
