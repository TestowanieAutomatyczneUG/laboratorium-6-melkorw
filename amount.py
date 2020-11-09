import math
import unittest


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        if play['type'] == "tragedy":
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)

            this_amount += 300 * perf['audience']

        else:
            raise ValueError(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf['audience'] / 5)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {format_as_dollars(total_amount/100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result


class StatmentTest(unittest.TestCase):

    def test_statment_empty_performances(self):
        self.assertEqual("Statement for lolo\nAmount owed is $0.00\nYou earned 0 credits\n", statement({"customer": "lolo", "performances": []}, {}))

    def test_statment_tragedy_audience_less_or_equal_30(self):
        self.assertEqual("Statement for lolo\n Antoni: $400.00 (30 seats)\nAmount owed is $400.00\nYou earned 0 credits\n", statement({"customer": "lolo", "performances": [{"playID": "hamlet", "audience": 30}]}, {"hamlet": {"type": "tragedy", "name": "Antoni"}}))

    def test_statment_comedy_audience_less_or_equal_20(self):
        self.assertEqual(
            "Statement for lolo\n Antoni: $357.00 (19 seats)\nAmount owed is $357.00\nYou earned 3 credits\n",
            statement({"customer": "lolo", "performances": [{"playID": "hamlet", "audience": 19}]},
                      {"hamlet": {"type": "comedy", "name": "Antoni"}}))

    def test_statment_tragedy_audience_greater_than_30(self):
        self.assertEqual("Statement for lolo\n Antoni: $550.00 (45 seats)\nAmount owed is $550.00\nYou earned 15 credits\n", statement({"customer": "lolo", "performances": [{"playID": "hamlet", "audience": 45}]}, {"hamlet": {"type": "tragedy", "name": "Antoni"}}))

    def test_statment_comedy_audience_greater_than_20(self):
        self.assertEqual(
            "Statement for lolo\n Antoni: $492.00 (24 seats)\nAmount owed is $492.00\nYou earned 4 credits\n",
            statement({"customer": "lolo", "performances": [{"playID": "hamlet", "audience": 24}]},
                      {"hamlet": {"type": "comedy", "name": "Antoni"}}))

    def test_statment_performance_key_error(self):
        self.assertRaises(KeyError, statement, {"customer": "lolo"}, {})

    def test_statment_customer_key_error(self):
        self.assertRaises(KeyError, statement, {"cust": "lolo"}, {})

    def test_statment_playid_key_error(self):
        self.assertRaises(KeyError, statement, {"customer": "lolo", "performances": [{"play": "hamlet"}]}, {})

    def test_statment_play_type_key_error(self):
        self.assertRaises(KeyError, statement, {"customer": "lolo", "performances": [{"playID": "hamlet"}]}, {"hamlet": {}})

    def test_statment_play_type_unknown_name_error(self):
        self.assertRaises(ValueError, statement, {"customer": "lolo", "performances": [{"playID": "hamlet"}]}, {"hamlet": {"type": "Unknown"}})

    def test_statment_audience_key_error(self):
        self.assertRaises(KeyError, statement, {"customer": "lolo", "performances": [{"playID": "hamlet"}]}, {"hamlet": {"type": "tragedy"}})

    def test_statment_play_name_key_error(self):
        self.assertRaises(KeyError, statement, {"customer": "lolo", "performances": [{"playID": "hamlet", "audience": 30}]}, {"hamlet": {"type": "tragedy"}})


if __name__ == "__main__":
    unittest.main()
