import string

alphabet = list(string.ascii_lowercase)

# Implementing the Strategy Pattern


def transform_text(text, shift_amount):
    transformed_text = ""
    limit = len(alphabet)

    for letter in text:

        if letter not in alphabet:
            # If we are in decode mode and the letter is not in the alphabet
            transformed_text += " " if shift_amount < 0 else letter
            continue

        position = alphabet.index(letter)
        new_position = (position + shift_amount) % limit

        new_letter = alphabet[new_position]
        transformed_text += new_letter

    return transformed_text


def encrypt(plain_text, shift_amount):
    cipher_text = transform_text(plain_text, shift_amount)
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = transform_text(cipher_text, -shift_amount)
    print(f"The decoded text is {plain_text}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(message, shift)
elif direction == "decode":
    decrypt(message, shift)
