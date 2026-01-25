from src.loader.field_loader import FieldLoader
from pathlib import Path


class AbstractFileFieldLoader(FieldLoader):
    file_path: Path

    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)

        if not self.file_path.exists():
            raise FileNotFoundError(f"File {self.file_path} not found")