import unittest
from src.FizzBuzz.FizzBuzzRule import FizzBuzzRule


class FizzBuzzRuleTests(unittest.TestCase):

    def test_WhenDivisorIsNegative_ThenCtorThrows(self):

        with self.assertRaises(ValueError):
            FizzBuzzRule(-10, "message")

    def test_WhenDivisorIsZero_ThenCtorThrows(self):

        with self.assertRaises(ValueError):
            FizzBuzzRule(0, "message")

    def test_WhenRemainderIsZero_ThenMessageIsReturned(self):

        divisor = 3
        message = "import message"
        value = 9

        rule = FizzBuzzRule(divisor, message)

        output = rule.evaluate(value)

        self.assertEqual(output, message)

    def test_WhenRemainderIsNotZero_ThenValueIsReturned(self):

        divisor = 3
        value = 5

        rule = FizzBuzzRule(divisor, "")

        output = rule.evaluate(value)

        self.assertEqual(output, str(value))

if __name__ == '__main__':
    unittest.main()
