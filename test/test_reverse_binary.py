import sys
sys.path.append('./')

import unittest
from puzzles import reverse_binary as rev


class TestReverseBinary(unittest.TestCase):

    def test_reverse_number(self):
        self.assertRaises(AssertionError, rev.reverse_number, 'string')

        assert type(rev.reverse_number(1)) == int
        assert rev.reverse_number(13) == 11
        assert rev.reverse_number(11) == 13
        assert rev.reverse_number(47) == 61
        assert rev.reverse_number(61) == 47

if __name__ == '__main__':
    unittest.main()
