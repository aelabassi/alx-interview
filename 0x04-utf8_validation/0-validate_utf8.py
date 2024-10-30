#!/usr/bin/python3
""" UTF8 validation """


def validUTF8(data: any):
    """ Validate if a given data set represents a valid UTF-8 encoding
    Args:
        data: list of integers
    Returns:
        True if data is a valid UTF-8 encoding, False otherwise
    """
    n_bytes = 0
    for num in data:
        byte = format(num, '#010b')[-8:]
        if n_bytes == 0:
            for bit in byte:
                if bit == '0':
                    break
                n_bytes += 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (byte[0] == '1' and byte[1] == '0'):
                return False
        n_bytes -= 1
    return n_bytes == 0
