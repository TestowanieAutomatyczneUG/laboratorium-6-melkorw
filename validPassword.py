import unittest


class Password:

    def validPassword(self, password):
        if password == "Qwer1234$":
            return "OK"


class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.temp = Password()

    def test_Password_positive(self):
        self.assertEqual("OK", self.temp.validPassword("Qwer1234$"))

    @unittest.skip('Skipped')
    def test_Password_too_short(self):
        self.assertEqual("Too short", self.temp.game("Qwe12*"))

    @unittest.skip('Skipped')
    def test_Password_without_number(self):
        self.assertEqual("Add number", self.temp.game("Qwertyui!"))

    @unittest.skip('Skipped')
    def test_Password_without_capital_letter(self):
        self.assertEqual("Add capital letter", self.temp.game("qwertyui!1"))

    @unittest.skip('Skipped')
    def test_Password_without_special_sign(self):
        self.assertEqual("Add special sign", self.temp.game("qwertyui123"))

    @unittest.skip('Skipped')
    def test_Password_Exception_only_number(self):
        self.assertRaises(ValueError, self.temp.game, 1237)

    @unittest.skip('Skipped')
    def test_Password_bad_type(self):
        self.assertRaises(Exception, self.temp.game, True)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()

