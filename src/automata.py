from typing import Optional


class State:
    """
    This class represents a State of an automaton
    """
    def __init__(self, name: Optional[str] = None):
        self.name: str = name

    def __eq__(self, other) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return str(self) == str(other)

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self) -> str:
        return str(self.name)