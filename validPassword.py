import unittest
import string
import doctest

special_chars = string.punctuation


class Password:

    def validPassword(self, password):
        """
        >>> p = Password()
        >>> p.validPassword("Qwer1234$")
        'OK'
        >>> p.validPassword("Qwe12!")
        'Too short'
        >>> p.validPassword("Q*wertysttt")
        'Add number'
        >>> p.validPassword("qwertyst!111")
        'Add capital letter'
        >>> p.validPassword("Qwertst1234")
        'Add special sign'
        >>> p.validPassword(123)
        Traceback (most recent call last):
          File "/Users/aleksanderwardyn/Documents/repo/laboratorium-6-melkorw/validPassword.py", line 51, in <module>
            p.validPassword(123)
          File "/Users/aleksanderwardyn/Documents/repo/laboratorium-6-melkorw/validPassword.py", line 25, in validPassword
            raise Exception('Cannot be integer')
        Exception: Cannot be integer
        >>> p.validPassword(True)
        Traceback (most recent call last):
          File "/Users/aleksanderwardyn/Documents/repo/laboratorium-6-melkorw/validPassword.py", line 60, in <module>
            p.validPassword(True)
          File "/Users/aleksanderwardyn/Documents/repo/laboratorium-6-melkorw/validPassword.py", line 36, in validPassword
            raise TypeError('Wrong type')
        TypeError: Wrong type
        """
        if type(password) is int:
            raise Exception('Cannot be integer')
        if type(password) is not str:
            raise TypeError('Wrong type')
        if len(password) < 8:
            return "Too short"
        special_sign = False
        capital_letter = False
        number = False
        for letter in password:
            if letter.isnumeric():
                number = True
            elif letter in special_chars:
                special_sign = True
            elif letter.isupper():
                capital_letter = True

        if number and special_sign and capital_letter:
            return "OK"
        if not number:
            return "Add number"
        if not capital_letter:
            return "Add capital letter"
        else:
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
        self.assertRaises(Exception, self.temp.validPassword, 1237)

    def test_Password_Exception_bad_type(self):
        self.assertRaises(TypeError, self.temp.validPassword, True)

    def tearDown(self):
        self.temp = None


if __name__ == "__main__":
    print(Password.validPassword.__doc__)
    doctest.testmod(extraglobs={'p': Password()})
