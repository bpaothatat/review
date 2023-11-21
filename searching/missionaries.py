from __future__ import annotations
from typing import List, Optional
from generic_search import bfs, Node, node_to_path

MAX_NUM: int = 3
class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.wm: int = missionaries # west bank missionaries
        self.wc: int = cannibals # west bank cannibals
        self.em: int = MAX_NUM - self.wm # east bank missionaries
        self.ec: int = MAX_NUM - self.wc # east bank cannibals
        self.boat: bool = boat
    
    def __str__(self) -> str:
        return ("On the west bank there are {} missionaries and {}cannibals.\n"
                "On the east bank there are {} missionaries and {}cannibals.\n"
                "The boat is on the {} bank.").format(self.wm, self.wc, self.em, self.ec, ("west" if self.boat else "east"))