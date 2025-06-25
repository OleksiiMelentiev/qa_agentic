import logging
import sys
import json
from typing import List

from src.models.test_case import TestCase


def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            result = file.read()
            return result
    except FileNotFoundError:
        print(f"Error: Script file '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading script file: {e}")
        sys.exit(1)


def save_to_file(filename: str, data: str):
    try:
        with open(filename, 'w') as file:
            file.write(data)
        logging.info(f"Data successfully saved to {filename}")
    except Exception as e:
        logging.error(f"Error saving file {filename}: {e}")


def read_test_cases_from_file(filename: str) -> List[TestCase]:
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return [TestCase(**item) for item in data]
    except FileNotFoundError:
        print(f"Error: Test cases file '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading test cases file: {e}")
        sys.exit(1)
