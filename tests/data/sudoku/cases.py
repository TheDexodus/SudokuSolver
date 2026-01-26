from typing import Iterator

from pathlib import Path

from src.field.rectangle_field import RectangleField
from src.loader.txt_file_field_loader import TxtFileFieldLoader

BASE_DIR = Path(__file__).parent

FINAL_CASES_PATH = BASE_DIR / 'final'
CORRECT_NOT_FINAL_CASES_PATH = BASE_DIR / 'correct_not_final'
INCORRECT_CASES_PATH = BASE_DIR / 'incorrect'

def load_final_cases() -> Iterator[RectangleField]:
    for path in FINAL_CASES_PATH.iterdir():
        if path.is_file():
            loader = TxtFileFieldLoader(path)
            yield loader.load()

def load_correct_not_final_cases() -> Iterator[RectangleField]:
    for path in CORRECT_NOT_FINAL_CASES_PATH.iterdir():
        if path.is_file():
            loader = TxtFileFieldLoader(path)
            yield loader.load()

def load_incorrect_cases() -> Iterator[RectangleField]:
    for path in INCORRECT_CASES_PATH.iterdir():
        if path.is_file():
            loader = TxtFileFieldLoader(path)
            yield loader.load()
