from abc import ABC


class FizzBuzzRule(ABC):

    @abstractmethod
    def evaluate(self, value: int) -> str:
        ...
