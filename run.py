import sys
import unittest

from tests.contactpagetests import ContactPageTest


if __name__ == "__main__":
    if len(sys.argv) > 1:
        ContactPageTest.ENV = sys.argv.pop()
    unittest.main()




