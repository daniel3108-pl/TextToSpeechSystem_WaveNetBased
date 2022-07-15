"""Moduł związany z pomocniczymi klasami, funkcjami do programowania funkcyjnego
"""

from __future__ import annotations

from typing import TypeVar, Generic, Callable

T = TypeVar("T")
U = TypeVar("U")


class Monad(Generic[T]):

    __internal_init = object()

    def __init__(self, internal_init, value: T) -> None:
        assert internal_init == Monad.__internal_init, "Cannot use Monad's initializer explicitly"
        self.value: T = value

    def flat_map(self, func: Callable[T, Monad[U]]) -> Monad[U]:
        return func(self.value)

    def map(self, func: Callable[T, U]) -> Monad[U]:
        return Monad.some(func(self.value))

    @classmethod
    def some(cls, value: T):
        return Monad(cls.__internal_init, value)

    def unbind(self) -> T:
        return self.value
