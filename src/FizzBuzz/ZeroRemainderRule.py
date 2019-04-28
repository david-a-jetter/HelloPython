from .FizzBuzzRule import FizzBuzzRule


class ZeroRemainderRule(FizzBuzzRule):
    _divisor = 0
    _message = ""

    def __init__(self, divisor: int, message: str):
        if divisor <= 0:
            raise ValueError("divisor must be positive but was %s" % divisor)

        self._divisor = divisor
        self._message = message

    def evaluate(self, value: int) -> str:

        if value % self._divisor == 0:
            response = self._message
        else:
            response = ""

        return response
