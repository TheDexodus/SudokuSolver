from abc import ABC
from pathlib import Path

from src.loader.field_loader import FieldLoader


class AbstractFileFieldLoader(FieldLoader, ABC):
    file_path: Path

    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)

        if not self.file_path.exists():
            raise FileNotFoundError(f"File {self.file_path} not found")