import unittest

import main


class MainTest(unittest.TestCase):
    def test_hello_world(self):
        ret = main.hello_world("Test")
        self.assertEqual(ret, "Hello World! jinmang2!")


if __name__ == "__main__":
    unittest.main()
