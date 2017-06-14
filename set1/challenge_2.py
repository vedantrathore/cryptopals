def xor(x, y):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(x, y)).encode('hex')


a = "1c0111001f010100061a024b53535009181c".decode('hex')
b = "686974207468652062756c6c277320657965".decode('hex')

if xor(a, b) == '746865206b696420646f6e277420706c6179':
    print "Passed"
else:
    print "Failed"
