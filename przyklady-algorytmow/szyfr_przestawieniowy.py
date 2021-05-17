# ord('a') == chr(97)
# 65-90 upper case
# 97-122 lower case

def ROT13(text, rotation = 13):
    out = ''
    for letter in text:
        encrypted = ord(letter) + rotation
        if encrypted > 122 or (ord(letter) < 91 and encrypted > 90):
            # overflow
            encrypted = encrypted - 26

        out += chr(encrypted)

    return out

print(ROT13('abccdefghijklmnopqrstuvwxyz'))
print(ROT13('ABCCDEFGHIJKLMNOPQRSTUVWXYZ'))

print(ROT13('noppqrstuvwxyzabcdefghijklm'))
print(ROT13('NOPPQRSTUVWXYZABCDEFGHIJKLM'))