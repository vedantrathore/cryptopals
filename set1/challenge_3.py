def score_alphatext(txt):
    # if len(txt) == 0:
    #     return
    scr = filter(lambda x: 'a' <= x <= 'z' or 'A' <= x <= 'Z' or x == ' ', txt)
    return float(len(scr)) / len(txt)


def solve_single_key_xor(ba):
    res = []
    for i in range(256):
        characters = [chr(c ^ i) for c in ba]
        res.append([score_alphatext(characters), ''.join(characters), i])
    return max(res, key=lambda x: x[0])


def main():
    cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    print solve_single_key_xor(bytearray(cipher.decode('hex')))


if __name__ == "__main__":
    main()
