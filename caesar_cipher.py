def encrypt(text, key):
    """Simple Caesar Cipher"""

    # TRANSFORM KEY INTO NUMBER FOR CIPHER
    key_transformation = 0
    for i in range(len(key)):
        char = key[i]
        key_transformation += ord(char)

    # ENCRYPT DATA
    result = ""
    text = text.lower()
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char) + key_transformation - 97) % 26 + 97)
    return result
