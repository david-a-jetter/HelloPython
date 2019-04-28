from src.FizzBuzz import FizzBuzzRule


class FizzBuzzEvaluator:
    _rules = [FizzBuzzRule]

    def __init__(self, rules: [FizzBuzzRule]):
        if rules is None:
            raise ValueError("rules must not be none")

        self._rules = rules

    def evaluate(self, value: int) -> str:

        response = []

        for rule in self._rules:
            result = rule.evaluate(value)

            if result != "":
                response.append(result)

        if len(response) == 0:
            response.append(str(value))

        return "".join(response)
