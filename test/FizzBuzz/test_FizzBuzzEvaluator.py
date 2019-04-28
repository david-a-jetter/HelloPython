import unittest
from src.FizzBuzz.FizzBuzzEvaluator import FizzBuzzEvaluator
from src.FizzBuzz.ZeroRemainderRule import ZeroRemainderRule


class FizzBuzzEvaluatorTests(unittest.TestCase):

    def test_WhenRulesIsNone_ThenCtorThrows(self):

        with self.assertRaises(ValueError):
            FizzBuzzEvaluator(None, "")

    def test_WhenOneRuleIsMatched_ThenOutputHasMessageAndValue(self):

        message = "3 ZeroRemainder"
        suffix = "!"
        rule1 = ZeroRemainderRule(3, message)
        rule2 = ZeroRemainderRule(5, "5 ZeroRemainder")

        evaluator = FizzBuzzEvaluator([rule1, rule2], suffix)

        response = evaluator.evaluate(3)

        self.assertEqual(response, message + suffix)

    def test_WhenTwoRulesAreMatched_ThenOutputHasBothMessages(self):

        message1 = "basic boring message"
        message2 = "AWESOME MESSAGE"
        suffix = "!"
        expected = message1 + message2 + suffix

        rule1 = ZeroRemainderRule(3, message1)
        rule2 = ZeroRemainderRule(5, message2)

        evaluator = FizzBuzzEvaluator([rule1, rule2], suffix)

        response = evaluator.evaluate(15)
        self.assertEqual(response, expected)

    def test_WhenNoRulesAreMatched_ThenOutputIsInput(self):

        value = 7
        rule1 = ZeroRemainderRule(3, "one")
        rule2 = ZeroRemainderRule(5, "two")

        evaluator = FizzBuzzEvaluator([rule1, rule2], suffix="!")

        response = evaluator.evaluate(value)

        self.assertEqual(response, str(value))
