import unittest
import unittest as u
from main4 import *


class Test(u.TestCase):
    def ap(self):
        res = add(2, 3)
        self.assertEquals(res, 5)


if __name__ == "__main__":
    u.main()
