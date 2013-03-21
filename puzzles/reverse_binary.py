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


if __name__ == "__main__":

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

