from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt

class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class MazePosition(NamedTuple):
    row: int
    column: int

class Maze:
    def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.2, start: MazePosition = MazePosition(0, 0), end: MazePosition = MazePosition(9, 9)) -> None:
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazePosition = start
        self.end: MazePosition = end 
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        self.__randomly_fill(rows, columns, sparseness)
        self._grid[start.row][start.column] = Cell.START
        self._grid[end.row][end.column] = Cell.GOAL

    def __randomly_fill(self, rows: int, columns: int, sparseness: float):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += "".join([column.value for column in row]) + "\n"
        return output
    
    def goal_test(self, position: MazePosition) -> bool:
        return position == self.end
    
    def successors(self, position: MazePosition) -> List[MazePosition]:
        positions: List[MazePosition] = []
        if position.row + 1 < self._rows and self._grid[position.row + 1][position.column] != Cell.BLOCKED:
            positions.append(MazePosition[position.row + 1][position.column])
        if position.row - 1 >= self._rows and self._grid[position.row - 1][position.column] != Cell.BLOCKED:
            positions.append(MazePosition[position.row - 1][position.column])
        if position.column + 1 < self._rows and self._grid[position.row][position.column + 1] != Cell.BLOCKED:
            positions.append(MazePosition[position.row][position.column + 1])
        if position.colum - 1 >= self._rows and self._grid[position.row][position.column - 1] != Cell.BLOCKED:
            positions.append(MazePosition[position.row][position.column - 1])
        return positions