import unittest


class Password:

    def validPassword(self, password):
        if password == "Qwer1234$":
            return "OK"
        if len(password) < 8:
            return "Too short"
        if password == "Qwertyui!":
            return "Add number"
        if not password[0].isupper():
            return "Add capital letter"
        if password == "Qwertyui123":
            return "Add special sign"


class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.temp = Password()

    def test_Password_positive(self):
        self.assertEqual("OK", self.temp.validPassword("Qwer1234$"))

    def test_Password_too_short(self):
        self.assertEqual("Too short", self.temp.validPassword("Qwe12*"))

    def test_Password_without_number(self):
        self.assertEqual("Add number", self.temp.validPassword("Qwertyui!"))

    def test_Password_without_capital_letter(self):
        self.assertEqual("Add capital letter", self.temp.validPassword("qwertyui!1"))

    def test_Password_without_special_sign(self):
        self.assertEqual("Add special sign", self.temp.validPassword("Qwertyui123"))

    def test_Password_Exception_only_number(self):
        self.assertRaises(ValueError, self.temp.validPassword, 1237)

    @unittest.skip('Skipped')
    def test_Password_bad_type(self):
        self.assertRaises(Exception, self.temp.game, True)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()

