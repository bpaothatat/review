from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
from generic_search import Node, dfs, node_to_path

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
    
    def mark(self, path: List[MazePosition]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path: List[MazePosition]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

if __name__ == "__main__":
    m: Maze = Maze()
    print(m)
    solution1: Optional[Node[MazePosition]] = dfs(m.start, m.goal_test,
    m.successors)
    if solution1 is None:
        print("No solution found using depth-first search!")
    else:
        path1: List[MazePosition] = node_to_path(solution1)
        m.mark(path1)
        print(m)
        m.clear(path1)