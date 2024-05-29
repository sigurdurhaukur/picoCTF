
def encrypt(flag):
    return ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])



def decrypt(encoded):
    decrypted = []
    for char in encoded:
        code_point = ord(char)
        high = code_point >> 8  # Shift right by 8 bits to get the original high byte
        low = code_point & 0xFF  # AND with 0xFF to mask out the low byte
        decrypted.append(chr(high))
        decrypted.append(chr(low))
    return ''.join(decrypted)


with open('enc', 'r') as f:
    enc = f.read().strip()


dec = decrypt(enc)

with open('flag.txt', 'w') as f:
    f.write(dec)
