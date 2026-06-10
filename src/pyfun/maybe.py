from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, assert_never


@dataclass(frozen=True, slots=True)
class Some[T]:
    value: T


@dataclass(frozen=True, slots=True)
class Nothing:
    pass


type Maybe[T] = Some[T] | Nothing


def fmap[T, U](container: Maybe[T], func: Callable[[T], U]) -> Maybe[U]:
    match container:
        case Some(v):
            return Some(func(v))
        case Nothing():
            return Nothing()
        case _ as unreachable:
            assert_never(unreachable)


def unwrap[T](container: Maybe[T]) -> T:
    match container:
        case Some(v):
            return v
        case Nothing():
            raise RuntimeError("nothing to unwrap")
        case _ as never:
            assert_never(never)


def bind[T, U](container: Maybe[T], func: Callable[[T], Maybe[U]]) -> Maybe[U]:
    match container:
        case Some(v):
            return func(v)
        case Nothing():
            return Nothing()
        case _ as unreachable:
            assert_never(unreachable)
