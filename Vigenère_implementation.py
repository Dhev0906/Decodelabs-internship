def generate_key(text, key):
    key = key.upper()
    key_extended = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            key_extended += key[key_index % len(key)]
            key_index += 1
        else:
            key_extended += char  # keep spaces/punctuation aligned

    return key_extended


def encrypt_vigenere(text, key):
    text = text.upper()
    key_extended = generate_key(text, key)
    result = ""

    for t, k in zip(text, key_extended):
        if t.isalpha():
            encrypted_char = chr((ord(t) - 65 + (ord(k) - 65)) % 26 + 65)
            result += encrypted_char
        else:
            result += t

    return result


def decrypt_vigenere(text, key):
    text = text.upper()
    key_extended = generate_key(text, key)
    result = ""

    for t, k in zip(text, key_extended):
        if t.isalpha():
            decrypted_char = chr((ord(t) - 65 - (ord(k) - 65)) % 26 + 65)
            result += decrypted_char
        else:
            result += t

    return result


# ---- MAIN PROGRAM ----
text = input("Enter text: ")
key = input("Enter key (word): ")

encrypted = encrypt_vigenere(text, key)
decrypted = decrypt_vigenere(encrypted, key)

print("\nEncrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
