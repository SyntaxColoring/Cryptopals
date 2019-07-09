def hex_to_base64(hex_string):
    import base64
    return str(base64.b64encode(bytes.fromhex(hex_string)), encoding="utf-8")

def fixed_xor(bytes_a, bytes_b):
    return bytes(a^b for a, b in zip(bytes_a, bytes_b))

def letter_frequencies(decoding):
    from collections import Counter
    counts = Counter(chr(b).upper() for b in decoding)
    frequencies = {char: count/len(decoding) for char, count in counts.items()}
    return frequencies

def score_decoding(decoding):
    # English letter frequencies stolen from 
    # http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
    expected_frequencies = {
        "E": 12.02,
        "T": 9.10,
        "A": 8.12,
        "O": 7.68,
        "I": 7.31,
        "N": 6.95,
        "S": 6.28,
        "R": 6.02,
        "H": 5.92,
        "D": 4.32,
        "L": 3.98,
        "U": 2.88,
        "C": 2.71,
        "M": 2.61,
        "F": 2.30,
        "Y": 2.11,
        "W": 2.09,
        "G": 2.03,
        "P": 1.82,
        "B": 1.49,
        "V": 1.11,
        "K": 0.69,
        "X": 0.17,
        "Q": 0.11,
        "J": 0.10,
        "Z": 0.07
    }
    frequencies = letter_frequencies(decoding)
    sum_of_squares = 0
    for letter, actual in frequencies.items():
        expected = expected_frequencies.get(letter, 0)
        sum_of_squares += (expected - actual)**2
    return sum_of_squares

def decode_single_byte_xor(encoded_bytes):
    decodings = [bytes(b^key for b in encoded_bytes) for key in range(256)]
    return sorted(decodings, key=score_decoding, reverse=True)