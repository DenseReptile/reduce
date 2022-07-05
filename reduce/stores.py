# Encoding: UTF-8
# pylint: disable=missing-module-docstring

from dataclasses import dataclass
from typing import (
    Any,
    Callable,
    Final,
    Generic,
    Optional,
    TypeVar,
    Union,
)

S = TypeVar("S")
_NONE: Final = type


@dataclass
class Writable(Generic[S]):
    """Stores a readable/writable value."""

    state: S

    def __call__(self, state: Union[S, _NONE] = _NONE):
        if state is _NONE:
            return self.state

        self.state = state
        return None

    def get(self):
        """Get the current state."""
        return self.state

    def set(self, state: S) -> None:
        """Set the current state."""
        self.state = state


@dataclass
class Derive(Generic[S]):
    """Derive from a store's value."""

    state: Writable
    callback: Optional[Callable[[Any], Any]] = None

    def __call__(self) -> None:
        if isinstance(self.callback, Callable):
            self.callback(self.state())

        return self.state()


__all__ = ("Writable", "Derive")
