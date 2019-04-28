class FizzBuzzEvaluator:
    _fizz = 0
    _buzz = 0

    def __init__(self, fizz: int = 3, buzz: int = 5):
        if fizz <= 0:
            raise ValueError("fizz must be positive but was %s" % fizz)

        if buzz <= 0:
            raise ValueError("buzz must be positive but was %s" % buzz)

        self._fizz = fizz
        self._buzz = buzz

    def evaluate(self, value: int) -> str:
        fizz = value % self._fizz == 0
        buzz = value % self._buzz == 0

        response = []

        if fizz:
            response.append("Fizz")
        if buzz:
            response.append("Buzz")
        if not fizz and not buzz:
            response.append(str(value))
        else:
            response.append("!")

        return "".join(response)
