import sys
sys.path.append('./')

import unittest
from puzzles import zipfsong


class TestZipfSong(unittest.TestCase):
    '''
    Since the requirements is restricted to python 2.6 I only use
    unittest with it's basic assertions
    '''

    def test_get_songs(self):
        mocked = ['2 2\n', '10 songname\n', '5 another_name\n']
        num_outputs, songs = zipfsong.get_songs(lambda: mocked)

        print songs

        int(num_outputs)
        assert num_outputs == 2

        name1 = songs[0][1]
        played1 = int(songs[0][0])

        played2 = int(songs[1][0])
        name2 = songs[1][1]

        assert played1 == 10
        assert name1 == 'songname'

        assert played2 == 5
        assert name2 == 'another_name'

    def test_validate_inputs_numbers(self):
        zipfsong.validate_inputs_numbers(4, 3)

        self.assertRaises(AssertionError,
                          zipfsong.validate_inputs_numbers,
                          1, 2)

        self.assertRaises(AssertionError,
                          zipfsong.validate_inputs_numbers,
                          0, 2)

        self.assertRaises(AssertionError,
                          zipfsong.validate_inputs_numbers,
                          50001, 3)

        self.assertRaises(AssertionError,
                          zipfsong.validate_inputs_numbers,
                          6, 0)

        self.assertRaises(ValueError,
                          zipfsong.validate_inputs_numbers,
                          'string', 0)

        self.assertRaises(ValueError,
                          zipfsong.validate_inputs_numbers,
                          4, 'string')

    def test_validate_play_count(self):
        zipfsong.validate_play_count(3)

        self.assertRaises(AssertionError,
                          zipfsong.validate_play_count,
                          -1)

        self.assertRaises(AssertionError,
                          zipfsong.validate_play_count,
                          10**13)

        self.assertRaises(ValueError,
                          zipfsong.validate_play_count,
                          'string')

    def test_validate_song_name(self):
        zipfsong.validate_song_name('abc')
        zipfsong.validate_song_name('123')
        zipfsong.validate_song_name('abc123')
        zipfsong.validate_song_name('1_2')

        self.assertRaises(AssertionError,
                          zipfsong.validate_song_name,
                          '#$&')

        self.assertRaises(AssertionError,
                          zipfsong.validate_song_name,
                          '#$&special')

        self.assertRaises(AssertionError,
                          zipfsong.validate_song_name,
                          '.dot')

        self.assertRaises(AssertionError,
                          zipfsong.validate_song_name,
                          'dot..')

        self.assertRaises(AssertionError,
                          zipfsong.validate_song_name,
                          'sp ace')

        # 30 chars should pass
        zipfsong.validate_song_name('111111111111111111111111111111')

        # 31 should fail
        self.assertRaises(AssertionError,
                          zipfsong.validate_song_name,
                          '1111111111111111111111111111111')

    def test_get_best_songs(self):
        songs1 = [(30, 'one'),
                  (30, 'two'),
                  (15, 'three'),
                  (25, 'four'), ]

        songs2 = [(197812, 're_hash'),
                  (78906, '5_4'),
                  (189518, 'tomorrow_comes_today'),
                  (39453, 'new_genious'),
                  (210492, 'clint_eastwood'),
                  (26302, 'man_research'),
                  (22544, 'punk'),
                  (19727, 'sound_check'),
                  (17535, 'double_bass'),
                  (18782, 'rock_the_house'),
                  (198189, '19_2000'),
                  (13151, 'latin_simone'),
                  (12139, 'starshine'),
                  (11272, 'slow_country'),
                  (10521, 'm1_a1'), ]


        songs3 = [(1000, 'd'),
                    (500, 'c'),
                    (250, 'b'),
                    (125, 'a')]

        result1 = zipfsong.get_best_songs(2, songs1)
        result2 = zipfsong.get_best_songs(3, songs2)
        result3 = zipfsong.get_best_songs(4, songs3)

        assert result1 == ['four', 'two']
        assert result2 == ['19_2000', 'clint_eastwood', 'tomorrow_comes_today']
        assert result3 == ['d', 'c', 'b', 'a']


if __name__ == '__main__':
    unittest.main()
