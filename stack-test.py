import unittest

from main import Element, Stack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.test_stack = Stack()

    def test_empty(self):
        self.assertIsNone(self.test_stack.pop())
        self.assertEqual(self.test_stack.stsize, 0)

    def test_check(self):
        for number in range (10):
            self.test_stack.push(number)
        self.test_stack.check()

    def test_size(self):
        for number in range (10):
            self.test_stack.push(number)
        self.assertTrue(self.test_stack.size() == "Stack size is 10\n")
    # Не понимаю, как сделать так, чтобы этот тест тоже работал.

    def test_pushpop(self):
        for number in range (10):
            self.test_stack.push(number)
        self.assertEqual(self.test_stack.pop(),  9)
        self.assertEqual(self.test_stack.stsize, 9)

    def test_clear(self):
        for number in range (10):
            self.test_stack.push(number)
        self.test_stack.clear()
        self.assertIsNone(self.test_stack.pop())
        self.assertEqual(self.test_stack.stsize, 0)

    def test_peek(self):
        self.test_stack.push("a")
        self.assertEqual(self.test_stack.peek(), "a")
        self.test_stack.push("b")
        self.assertEqual(self.test_stack.peek(), "b")


if __name__ == "__main__":
    unittest.main()