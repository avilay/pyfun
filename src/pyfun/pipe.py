from __future__ import annotations

from typing import Callable


class Pipe[T]:
    __slots__ = ("value",)

    def __init__(self, value: T) -> None:
        self.value = value

    def __or__[U](self, func: Callable[[T], U]) -> Pipe[U]:
        return Pipe(func(self.value))
