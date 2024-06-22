import os
import glob
import re
import json
from aggregator import aggregate_repo_data  # Ensure this path is correct

def extract_text_from_python_files(directory):
    """
    Extracts text data (function and variable names) from Python files in a directory.

    Args:
        directory: The path to the directory containing Python files.

    Returns:
        A list of dictionaries, where each dictionary holds extracted information
        for a single processed file.
    """
    file_paths = glob.glob(os.path.join(directory, '*.py'))
    extracted_text = []

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # Remove comments (single-line and multi-line)
            content = re.sub(r'#.*?\n', '', content)  # Remove single-line comments
            content = re.sub(r'""".*?"""', '', content, flags=re.DOTALL)  # Remove multi-line comments

            # Extract function and variable names
            function_names = re.findall(r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', content)
            variable_names = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=', content)

            # Combine extracted text elements
            extracted_text.append({
                'file_name': os.path.basename(file_path),
                'content': content,
                'function_names': function_names,
                'variable_names': variable_names
            })

    return extracted_text

if __name__ == "__main__":
    directory = r'C:\Users\lunch#\Documents\GitHub\PCAP_Enumeration'  # Replace with your repository directory path
    extracted_text = extract_text_from_python_files(directory)

    # Call the aggregation function to get a single string
    aggregated_data_string = aggregate_repo_data(extracted_text)

    # Example: Print the aggregated data
    print(aggregated_data_string)

    # Example: Saving extracted text to a JSON file
    output_file = 'extracted_text.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(extracted_text, f, ensure_ascii=False, indent=4)

    print(f"Extracted text saved to {output_file}")
