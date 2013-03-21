# -*- coding: utf-8 -*-

import sys
import re


def reader():
    '''
    Reader function that will be passed to functions that needs to read input.
    Extract this to make code more testable
    '''
    inputs = []
    for i in sys.stdin.readlines():
        inputs.append(i)
    return inputs


def get_songs(reader):
    '''
    n = number of songs on album = 1 ≤ n ≤ 50000,
    m = amout of songs in result = 1 ≤ m ≤ n
    '''
    inputs = reader()
    n, m = inputs[0].split(' ', 1)

    # remove the first input from the list
    inputs = inputs[1:]

    # make sure that input can be casted to int
    n = int(n)
    m = int(m)
    validate_inputs_numbers(n, m)

    # Read songs from 0 - n
    songs = []
    for track in inputs:
        played, song = track.split(' ', 1)
        played = int(played)

        validate_play_count(played)

        # remove new line
        song = song.replace('\n', '')
        validate_song_name(song)

        # list format: [('how many times played', 'song name'),..]
        songs.append((played, song))

    return m, songs


def validate_inputs_numbers(n, m):
    '''
    Validate the first two number a user enter
    '''
    int(n)
    int(m)
    assert n >= 1
    assert n <= 50000
    assert m >= 1
    assert m <= n


def validate_play_count(played):
    '''
    The amount of times a song has been played: 0 ≤ fi ≤ 10**12
    '''

    int(played)
    assert played >= 0
    assert played <= 10**12


def validate_song_name(song):
    '''
    String must be: ‘a’-‘z’, ‘0’-‘9’ _
    and not longer than 30
    '''
    assert len(song) <= 30
    assert re.match(r'^[a-z0-9_]*$', song) is not None


def get_best_songs(m, songs):
    '''
    songs: [('how many times played', 'song name'),...]
    zi = 1 / ith song
    fi = how many times played
    q = quality = fi / zi
    '''

    result = []
    final_list = []
    for idx, song in enumerate(songs):
        zi = float(1) / float(idx + 1)
        fi = song[0]
        q = float(fi) / float(zi)
        result.append((q, song[1]))

    # sort list by q index
    result = sorted(result, key=lambda name: name[0], reverse=True)
    result = result[:m]

    for i in result:
        final_list.append(i[1])

    # return the only the m first results
    return final_list

if __name__ == "__main__":
    '''
    Perform all calls and prints the result
    '''
    # pass the reader for better testability
    m, songs = get_songs(reader)
    result = get_best_songs(m, songs)

    # print the result
    for i in result:
        print i

