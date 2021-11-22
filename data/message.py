from dataclasses import asdict
from typing import Any, Optional

from pydantic.dataclasses import dataclass


@dataclass
class Sender:
    """
    Sender class
    """
    id: str
    name: str


@dataclass
class Message:
    id: int
    type: str
    content: Any
    sender: Optional[Sender] = None

    @property
    def dict(self):
        return asdict(self)
