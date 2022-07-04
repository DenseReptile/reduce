# Encoding: UTF-8


from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Final,
    Generic,
    Optional,
    TypeVar,
    Union,
)

if TYPE_CHECKING:
    S = TypeVar("S")
_NONE: Final = type


@dataclass
class Writable(Generic[S]):
    state: S

    def __call__(self, state: Union[S, _NONE] = _NONE):
        """# TODO: Documentation."""
        if state is _NONE:
            return self.state

        self.state = state
        return None

    def get(self):
        """# TODO: Documentation."""
        return self.state

    def set(self, state: S) -> None:
        """# TODO: Documentation."""
        self.state = state


@dataclass
class Derive(Generic[S]):
    state: Writable
    callback: Optional[Callable[[Any], Any]] = None

    def __call__(self) -> None:
        """# TODO: Documentation."""
        if isinstance(self.callback, Callable):
            self.callback(self.state())

        return self.state()


__all__ = ("Writable", "Derive")
