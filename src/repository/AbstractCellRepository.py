from src.cell.CellInteface import CellInterface
from src.repository.CellRepositoryInterface import CellRepositoryInterface

class AbstractCellRepository(CellRepositoryInterface):
    _cells: dict[str, CellInterface]

