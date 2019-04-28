import unittest
from src.FizzBuzz.FizzBuzzEvaluator import FizzBuzzEvaluator


class FizzBuzzEvaluatorTests(unittest.TestCase):

    def test_WhenEvaluatorIsConstructed_ThenPropertiesAreSetAsExpected(self):
        fizz = 33
        buzz = 55

        evaluator = FizzBuzzEvaluator(fizz, buzz)

        self.assertEqual(evaluator._fizz, fizz)
        self.assertEqual(evaluator._buzz, buzz)

    def test_WhenNotDivisibleByEither_ThenValueIsReturned(self):
        fizz = 3
        buzz = 5
        value = 11

        evaluator = FizzBuzzEvaluator(fizz, buzz)

        result = evaluator.evaluate(value)

        self.assertEqual(result, str(value))

    def test_WhenDivisibleByFizz_ThenResponseIsFizzWithBang(self):
        fizz = 3
        buzz = 5
        value = 9

        evaluator = FizzBuzzEvaluator(fizz, buzz)

        result = evaluator.evaluate(value)

        self.assertEqual(result, "Fizz!")

    def test_WhenDivisibleByBuzz_ThenResponseIsBuzzWithBang(self):
        fizz = 3
        buzz = 5
        value = 10

        evaluator = FizzBuzzEvaluator(fizz, buzz)

        result = evaluator.evaluate(value)

        self.assertEqual(result, "Buzz!")

    def test_WhenDivisibleByFizzAndBuzz_ThenResponseIsFizzBuzzWithBang(self):
        fizz = 3
        buzz = 5
        value = 30

        evaluator = FizzBuzzEvaluator(fizz, buzz)

        result = evaluator.evaluate(value)

        self.assertEqual(result, "FizzBuzz!")

    def test_WhenFizzIsNotPositive_ThenCtorThrows(self):
        fizz = 0
        buzz = 5

        with self.assertRaises(ValueError):
            FizzBuzzEvaluator(fizz, buzz)

    def test_WhenBuzzIsNotPositive_ThenCtorThrows(self):
        fizz = 3
        buzz = 0

        with self.assertRaises(ValueError):
            FizzBuzzEvaluator(fizz, buzz)


if __name__ == '__main__':
    unittest.main()
