def caesar_cipher(some_word):
    output = ""
    for c in some_word:
        print(c, end="")
        output += (shift_char(c, 1))
    print()
    print(output)

def shift_char(c, shift_config):
    if 'a' <= c <= 'z':
        base = ord('a')
        return chr((ord(c) - base + shift_config) % 26 + base)
    elif 'A' <= c <= 'Z':
        base = ord('A')
        return chr((ord(c) - base + shift_config) % 26 + base)
    else:
        return c

caesar_cipher("SNJDM CQHES QHCFD KZQFD")
