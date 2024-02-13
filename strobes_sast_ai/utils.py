# utils.py

import os
import json
import logging


def read_file(file_path):
    """
    Reads and returns the content of a file.

    Parameters:
    - file_path: The path to the file to read.

    Returns:
    - The content of the file as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")
    return None


def write_file(file_path, content):
    """
    Writes content to a file, overwriting it if it exists.

    Parameters:
    - file_path: The path to the file to write.
    - content: The content to write to the file.

    Returns:
    - Boolean indicating the success of the operation.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        logging.error(f"Error writing to file {file_path}: {e}")
    return False


def backup_file(file_path):
    """
    Creates a backup of the file before patching.

    Parameters:
    - file_path: The path to the file to backup.

    Returns:
    - The path to the backup file, or None if the operation failed.
    """
    backup_path = f"{file_path}.bak"
    try:
        content = read_file(file_path)
        if content is not None:
            write_file(backup_path, content)
            return backup_path
    except Exception as e:
        logging.error(f"Error creating backup for file {file_path}: {e}")
    return None


def setup_logging():
    """
    Sets up the logging configuration for the application.
    """
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
