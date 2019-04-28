import unittest
from src.FizzBuzz.ZeroRemainderRule import ZeroRemainderRule


class FizzBuzzRuleTests(unittest.TestCase):

    def test_WhenDivisorIsNegative_ThenCtorThrows(self):

        with self.assertRaises(ValueError):
            ZeroRemainderRule(-10, "message")

    def test_WhenDivisorIsZero_ThenCtorThrows(self):

        with self.assertRaises(ValueError):
            ZeroRemainderRule(0, "message")

    def test_WhenRemainderIsZero_ThenMessageIsReturned(self):

        divisor = 3
        message = "import message"
        value = 9

        rule = ZeroRemainderRule(divisor, message)

        output = rule.evaluate(value)

        self.assertEqual(output, message)

    def test_WhenRemainderIsNotZero_ThenEmptyStringIsReturned(self):

        divisor = 3
        value = 5

        rule = ZeroRemainderRule(divisor, "")

        output = rule.evaluate(value)

        self.assertEqual(output, "")
