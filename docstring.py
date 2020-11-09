# Działa na Pythonie 3.8.X
import doctest
class Calculate:
    def add(self, x, y):
        """
        >>> c = Calculate()
        >>> c.add(1,1)
        2
        >>> c.add(25.25,125)
        150.25
        >>> c.add("1", "2")
        '12'
        >>> c.add("1", 2)
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
          File "/Users/aleksanderwardyn/Documents/repo/laboratorium-6-melkorw/docstring.py", line 50, in <module>
            print(c.add("1", 2))
          File "/Users/aleksanderwardyn/Documents/repo/laboratorium-6-melkorw/docstring.py", line 13, in add
            return x + y
        TypeError: can only concatenate str (not "int") to str
        >>> c.add(True, False)
        1
        """
        return x + y

    def addWithDocString(self, x, y):
        """Takes two integers and adds them together to produce the result
        >>> c = Calculate()
        >>> c.addWithDocString(1,1)
        2
        >>> c.addWithDocString(25,125)
        150
        >>> c.addWithDocString(1.5656, 1.755)
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
          File "/Users/aleksanderwardyn/Documents/repo/laboratorium-6-melkorw/docstring.py", line 71, in <module>
            print(c.addWithDocString(1.5656, 1.755))
          File "/Users/aleksanderwardyn/Documents/repo/laboratorium-6-melkorw/docstring.py", line 56, in addWithDocString
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))
        TypeError: Invalid type: <class 'float'> and <class 'float'>
        """
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))


if __name__ == "__main__":
    print(Calculate.addWithDocString.__doc__)

    doctest.testmod(extraglobs={'c': Calculate()})
