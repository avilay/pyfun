from functools import partial
from typing import Callable, assert_never

from pyfun import Maybe, Nothing, Pipe, Some, bind, fmap


def safe_div(a: float, b: float) -> Maybe[float]:
    return Nothing() if b == 0 else Some(a / b)


match fmap(safe_div(10, 2), lambda x: x / 5):
    case Some(v):
        print(v)
    case Nothing():
        print("undefined")
    case _ as unreachable:
        assert_never(unreachable)


match bind(safe_div(10, 0), lambda x: safe_div(x, 5)):
    case Some(v):
        print(v)
    case Nothing():
        print("undefined")
    case _ as never:
        assert_never(never)


def is_even(x: int) -> bool:
    return x % 2 == 0


def to_str(x: int) -> str:
    return str(x)


x = list(map(str, filter(is_even, range(6))))
print(x)

y = (Pipe(range(6)) | partial(filter, is_even) | partial(map, to_str) | list).value
print(y)

z = (
    Pipe(range(6)) | (lambda it: filter(is_even, it)) | (lambda it: map(str, it)) | list
).value
print(z)


def mapping[T, U](f: Callable[[T], U]) -> Callable[[Maybe[T]], Maybe[U]]:
    return lambda m: fmap(m, f)


def halve(x: float) -> float:
    return x / 5


def inc(x: float) -> float:
    return x + 1.0


result = (
    Pipe(safe_div(10, 2)) | mapping(halve) | mapping(inc)
).value  # Maybe[float], clean
print(result)
