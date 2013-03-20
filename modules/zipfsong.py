# -*- coding: utf-8 -*-

import sys
import re


def get_arguments():
    '''
        n = number of songs on album 1 ≤ n ≤ 50000,
        m = 1 ≤ m ≤ n
    '''
    setup = sys.stdin.readline()
    n, m = setup.split(' ', 1)

    n = validate_num(n)
    m = validate_num(m)

    assert n >= 1
    assert n <= 50000
    assert m >= 1
    assert m <= n

    songs = []
    for i in range(0, n):
        track = sys.stdin.readline()
        played, song = track.split(' ', 1)
        played = validate_num(played)

        '''
        played must be: 0 ≤ fi ≤ 10**12
        '''
        assert played >= 0
        assert played <= 10**12

        validate_song_name(song)

        songs.append((played, song))

    return n, m, songs


def validate_num(num):
    try:
        number = int(num)
    except ValueError, e:
        print 'Number not valid: %s' % e
        exit(1)
    return number

##FIX THE UNDERSCORE

def validate_song_name(song):
    '''
    String must be: ‘a’-‘z’, ‘0’-‘9’ _
    and not longer than 30
    '''
    assert len(song) <= 30
    assert re.search('[a-z0-9_]', song) is not None



def get_best_song(n, m, songs):
    result = []
    for i in songs:
        q = i[0] / 
        result.append()

if __name__ == "__main__":
    n, m, songs = get_arguments()
    get_best_song(n, m, songs)

