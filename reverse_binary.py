import sys


def reverse_number(num):
    assert type(num) == int

    '''
    bin() return a string representation of the number on the for 0bxxx.
    remove 0b from the string
    '''
    rev_num = bin(num)[2:]

    '''
    Reverse the string
    '''
    rev_num = rev_num[::-1]

    '''
    Add 0b back to the reversed string
    '''
    rev_num = '0b%s' % rev_num

    return int(rev_num, 2)


def test_reverse_number():
    '''
    Test that the examples work back and forth
    '''
    assert type(reverse_number(1)) == int
    assert reverse_number(13) == 11
    assert reverse_number(11) == 13
    assert reverse_number(47) == 61
    assert reverse_number(61) == 47


if __name__ == "__main__":
    try:
        test_reverse_number()
    except AssertionError, e:
        print 'Test failed: %s' % str(e)

    '''
    Read from stdin
    '''
    num = sys.stdin.readline()

    try:
        # cast to int
        num = int(num)
    except ValueError, e:
        print e
        exit(1)

    print reverse_number(num)

