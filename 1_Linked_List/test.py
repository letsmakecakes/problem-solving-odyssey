"""
Unit tests for the LinkedList class.
"""

import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    """Unit tests for the LinkedList class."""

    def setUp(self):
        """Set up a linked list for testing."""
        self.ll = LinkedList(1)

    def test_append(self):
        """Test appending elements to the linked list."""
        self.ll.append(2)
        self.ll.append(3)
        self.assertEqual(self.ll.tail.value, 3)
        self.assertEqual(self.ll.length, 3)

    def test_prepend(self):
        """Test prepending elements to the linked list."""
        self.ll.prepend(0)
        self.assertEqual(self.ll.head.value, 0)
        self.assertEqual(self.ll.length, 2)

    def test_pop(self):
        """Test popping the last element from the linked list."""
        self.ll.append(2)
        self.ll.append(3)
        value = self.ll.pop()
        self.assertEqual(value, 3)
        self.assertEqual(self.ll.tail.value, 2)
        self.assertEqual(self.ll.length, 2)

    def test_pop_first(self):
        """Test popping the first element from the linked list."""
        self.ll.append(2)
        value = self.ll.pop_first()
        self.assertEqual(value, 1)
        self.assertEqual(self.ll.head.value, 2)
        self.assertEqual(self.ll.length, 1)

    def test_get(self):
        """Test getting the value of a node at a specific index."""
        self.ll.append(2)
        self.ll.append(3)
        value = self.ll.get(1)
        self.assertEqual(value, 2)
        value = self.ll.get(2)
        self.assertEqual(value, 3)
        value = self.ll.get(3)
        self.assertIsNone(value)


if __name__ == '__main__':
    unittest.main()
