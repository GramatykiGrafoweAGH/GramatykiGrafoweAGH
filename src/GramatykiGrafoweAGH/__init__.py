from dataclasses import dataclass, field
from itertools import count


@dataclass(eq=True, frozen=True)
class Node:
    label: str
    x: float
    y: float
    level: int
    id: int = field(default_factory=count().__next__, init=False)
