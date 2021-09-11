import unittest

import main


class MainTest(unittest.TestCase):
    def test_hello_world(self):
        ret = main.hello_world("Test")
        self.assertEqual(ret, "Hello World! Test!")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
