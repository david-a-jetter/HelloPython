from src.FizzBuzz.FizzBuzzEvaluator import FizzBuzzEvaluator

evaluator = FizzBuzzEvaluator(3, 5)

for value in range(1, 101):
    evaluated = evaluator.evaluate(value)
    print(evaluated)
