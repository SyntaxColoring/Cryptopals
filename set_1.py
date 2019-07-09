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
        "E": 0.120272,
        "T": 0.091044,
        "A": 0.081290,
        "O": 0.076861,
        "I": 0.073101,
        "N": 0.069522,
        "S": 0.062848,
        "R": 0.060251,
        "H": 0.059252,
        "D": 0.043219,
        "L": 0.039811,
        "U": 0.028795,
        "C": 0.027131,
        "M": 0.026132,
        "F": 0.023053,
        "Y": 0.021149,
        "W": 0.020962,
        "G": 0.020270,
        "P": 0.018201,
        "B": 0.014902,
        "V": 0.011082,
        "K": 0.006900,
        "X": 0.001729,
        "Q": 0.001125,
        "J": 0.001032,
        "Z": 0.000066,
    }
    frequencies = letter_frequencies(decoding)
    sum_of_squares = 0
    for letter, actual in frequencies.items():
        expected = expected_frequencies.get(letter, 0)
        assert 0 <= actual <= 1
        assert 0 <= expected <= 1
        sum_of_squares += (expected-actual)**2
    return sum_of_squares

def decode_single_byte_xor(encoded_bytes):
    decodings = [bytes(b^key for b in encoded_bytes) for key in range(256)]
    return sorted(decodings, key=score_decoding)
