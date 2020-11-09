import doctest


class FizzBuzz:
    def game(self, num):
        """
        >>> fizzBuzz = FizzBuzz()
        >>> fizzBuzz.game(15)
        'FizzBuzz'
        >>> fizzBuzz.game(3)
        'Fizz'
        >>> fizzBuzz.game(5)
        'Buzz'
        >>> fizzBuzz.game(1)
        Traceback (most recent call last):
          File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm/docrunner.py", line 305, in <module>
            modules = [loadSource(a[0])]
          File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm/docrunner.py", line 237, in loadSource
            module = _load_file(moduleName, fileName)
          File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm/docrunner.py", line 209, in _load_file
            return machinery.SourceFileLoader(moduleName, fileName).load_module()
          File "<frozen importlib._bootstrap_external>", line 462, in _check_name_wrapper
          File "<frozen importlib._bootstrap_external>", line 962, in load_module
          File "<frozen importlib._bootstrap_external>", line 787, in load_module
          File "<frozen importlib._bootstrap>", line 265, in _load_module_shim
          File "<frozen importlib._bootstrap>", line 702, in _load
          File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
          File "<frozen importlib._bootstrap_external>", line 783, in exec_module
          File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
          File "/Users/aleksanderwardyn/Documents/repo/laboratorium-6-melkorw/fizzBuzz.py", line 28, in <module>
            fizz.game(1)
          File "/Users/aleksanderwardyn/Documents/repo/laboratorium-6-melkorw/fizzBuzz.py", line 20, in game
            raise Exception("Error in FizzBuzz")
        Exception: Error in FizzBuzz
        >>> fizzBuzz.game(True)
        Traceback (most recent call last):
          File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm/docrunner.py", line 305, in <module>
            modules = [loadSource(a[0])]
          File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm/docrunner.py", line 237, in loadSource
            module = _load_file(moduleName, fileName)
          File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm/docrunner.py", line 209, in _load_file
            return machinery.SourceFileLoader(moduleName, fileName).load_module()
          File "<frozen importlib._bootstrap_external>", line 462, in _check_name_wrapper
          File "<frozen importlib._bootstrap_external>", line 962, in load_module
          File "<frozen importlib._bootstrap_external>", line 787, in load_module
          File "<frozen importlib._bootstrap>", line 265, in _load_module_shim
          File "<frozen importlib._bootstrap>", line 702, in _load
          File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
          File "<frozen importlib._bootstrap_external>", line 783, in exec_module
          File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
          File "/Users/aleksanderwardyn/Documents/repo/laboratorium-6-melkorw/fizzBuzz.py", line 90, in <module>
            fizz.game(True)
          File "/Users/aleksanderwardyn/Documents/repo/laboratorium-6-melkorw/fizzBuzz.py", line 83, in game
            raise Exception("Error in FizzBuzz")
        Exception: Error in FizzBuzz
        >>> fizzBuzz.game("22")
        Traceback (most recent call last):
          File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm/docrunner.py", line 305, in <module>
            modules = [loadSource(a[0])]
          File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm/docrunner.py", line 237, in loadSource
            module = _load_file(moduleName, fileName)
          File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm/docrunner.py", line 209, in _load_file
            return machinery.SourceFileLoader(moduleName, fileName).load_module()
          File "<frozen importlib._bootstrap_external>", line 462, in _check_name_wrapper
          File "<frozen importlib._bootstrap_external>", line 962, in load_module
          File "<frozen importlib._bootstrap_external>", line 787, in load_module
          File "<frozen importlib._bootstrap>", line 265, in _load_module_shim
          File "<frozen importlib._bootstrap>", line 702, in _load
          File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
          File "<frozen importlib._bootstrap_external>", line 783, in exec_module
          File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
          File "/Users/aleksanderwardyn/Documents/repo/laboratorium-6-melkorw/fizzBuzz.py", line 89, in <module>
            fizz.game("22")
          File "/Users/aleksanderwardyn/Documents/repo/laboratorium-6-melkorw/fizzBuzz.py", line 75, in game
            if (num % 15) == 0:
        TypeError: not all arguments converted during string formatting
        """
        if (num % 15) == 0:
            return "FizzBuzz"
        elif (num % 3) == 0:
            return "Fizz"
        elif (num % 5) == 0:
            return "Buzz"
        else:
            raise Exception("Error in FizzBuzz")


if __name__ == "__main__":
    print(FizzBuzz.game.__doc__)

    doctest.testmod(extraglobs={'fizzBuzz': FizzBuzz()})
