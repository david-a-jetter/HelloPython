from abc import ABC, abstractmethod


class FizzBuzzRule(ABC):

    @abstractmethod
    def evaluate(self, value: int) -> str:
        ...
