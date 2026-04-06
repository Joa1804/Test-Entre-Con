import unittest

class TestMain(unittest.TestCase):

    def test_example(self):
        self.assertEqual(1 + 1, 2)

    def test_another_example(self):
        self.assertTrue(isinstance('Hello', str))

if __name__ == '__main__':
    unittest.main()