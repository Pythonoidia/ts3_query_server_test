import unittest
from unittest.mock import MagicMock
from inserting import RawManipulation

class TestRawManipulation(unittest.TestCase):
    def test_adding_channel(self):
        raw = RawManipulation('filename')
        payload = []
        self.assertEqual(payload, ['something in'])

if __name__ == '__main__':
    unittest.main()
