def hex_to_bin(hex_number):
    """converts a hexadecimal number to binary"""
    return bin(int(hex_number, 16))[2:]


def str_to_bin(st):
    """converts string to binary number"""
    return ''.join(format(ord(x), 'b') for x in st)
