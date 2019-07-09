import set_1

def test_hex_to_base64():
    hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    base64_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert set_1.hex_to_base64(hex_string) == base64_string

def test_fixed_xor():
    a = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    b = bytes.fromhex("686974207468652062756c6c277320657965")
    result = bytes.fromhex("746865206b696420646f6e277420706c6179")
    assert set_1.fixed_xor(a, b) == result

def test_decode_single_byte_xor():
    ciphertext = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    plaintext = b"Cooking MC's like a pound of bacon"
    decodings = set_1.decode_single_byte_xor(ciphertext)
    assert plaintext in decodings[:5]
