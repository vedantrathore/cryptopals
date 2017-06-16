from challenge_3 import *


def get_data():
    with open('data/4.txt', 'r') as fp:
        return fp.read().split('\n')


def check_single_key_xor(key):
    key = solve_single_key_xor(key)
    text = key[1]
    try:
        print text.encode('ascii')
    except Exception:
        pass


def main():
    keys = get_data()
    for key in keys:
        if len(key) == 0:
            continue
        check_single_key_xor(bytearray(key.strip().decode('hex')))


if __name__ == '__main__':
    main()
