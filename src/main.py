from src.FizzBuzz.FizzBuzzEvaluator import FizzBuzzEvaluator
from src.FizzBuzz.ZeroRemainderRule import ZeroRemainderRule

rules = [
    ZeroRemainderRule(3, "Fizz"),
    ZeroRemainderRule(5, "Buzz"),
    ZeroRemainderRule(7, "Bang")
]

evaluator = FizzBuzzEvaluator(rules)

for value in range(1, 106):
    evaluated = evaluator.evaluate(value)
    print(evaluated)
