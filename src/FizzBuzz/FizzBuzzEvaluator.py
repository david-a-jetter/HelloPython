from src.FizzBuzz import FizzBuzzRule


class FizzBuzzEvaluator:

    _rules: [FizzBuzzRule]
    _suffix: str

    def __init__(self, rules: [FizzBuzzRule], suffix: str):
        if rules is None:
            raise ValueError("rules must not be none")

        self._rules = rules
        self._suffix = suffix

    def evaluate(self, value: int) -> str:

        response = []

        for rule in self._rules:
            result = rule.evaluate(value)

            if result != "":
                response.append(result)

        if len(response) == 0:
            response.append(str(value))
        else:
            response.append(self._suffix)

        return "".join(response)
