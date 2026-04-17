from typing import Any
import copy

class Variant:
    """Witnesses while-loop termination: tracks an integer that must strictly
    decrease each iteration and stay at or above a lower bound."""

    def __init__(self, name: str = 'Variant', *, lower_bound: int = 0, debug: bool = False):
        self.name = name
        self.value: int | None = None
        self.lower_bound = lower_bound
        self.debug = debug

    def __call__(self, new_value: int) -> None:
        assert new_value >= self.lower_bound, (
            f"{self.name} ({new_value}) dropped below lower bound {self.lower_bound}"
        )
        assert self.value is None or new_value < self.value, (
            f"{self.name} did not decrease: {self.value} → {new_value}"
        )
        self.value = new_value
        if self.debug:
            print(f"{self.name}: {new_value}")

class Invariant:
    """Witnesses while-loop invariants: tracks a value that must stay
    constant across iterations."""

    def __init__(self, name: str = 'Invariant', debug: bool = False):
        self.name = name
        self.value: Any = None
        self.debug = debug

    def __call__(self, new_value: Any) -> None:
        if self.value is None:
            self.value = copy.deepcopy(new_value)
            if self.debug:
                print(f"{self.name} initialized: {self.value}")
        else:
            assert new_value == self.value, (
                f"{self.name} changed: {self.value} → {new_value}"
            )