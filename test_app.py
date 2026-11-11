import unittest
from app import hello, add, status


class TestApp(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello DevOps")

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_status(self):
        self.assertEqual(status()["status"], "ok")


if __name__ == "__main__":
    unittest.main()
