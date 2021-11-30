"""
Write a function that can encrypt and decrypt a text.
You should use the “Caesar Cipher” method to encrypt and decrypt your text.
The Caesar Cipher is an encryption algorithm that takes in a key (integer) and text (string).
It encrypts the text by moving every letter of the text “forward” in the alphabet a 
total of key places. This key acts as the password that will be required to decrypt 
the encrypted text"""

def encrypt_ceaser(text, key):
    encrypted_text = ""
    # in ASCII, A = 65, Z = 90, a = 97, z = 122
    for letter in text:
        if letter.isalpha():
            letter_num = ord(letter)
            if letter.isupper():
                letter_num = letter_num + key
                if letter_num > 90:
                    letter_num = letter_num - 26
            elif letter.islower():
                letter_num = letter_num + key
                if letter_num > 122:
                    letter_num = letter_num - 26
            encrypted_text += chr(letter_num)
        else:
            encrypted_text += letter
    return encrypted_text
def decrypt_ceaser(text, key):
    decrypted_text = ""
    # in ASCII, A = 65, Z = 90, a = 97, z = 122
    for letter in text:
        if letter.isalpha():
            letter_num = ord(letter)
            if letter.isupper():
                letter_num = letter_num - key
                if letter_num < 65:
                    letter_num = letter_num + 26
            elif letter.islower():
                letter_num = letter_num - key
                if letter_num < 97:
                    letter_num = letter_num + 26
            decrypted_text += chr(letter_num)
        else:
            decrypted_text += letter
    return decrypted_text


def main():
    text = input("Enter text to decrypt: ")
    key = int(input("Enter key: "))
    decrypted_text = decrypt_ceaser(text, key)
    print(decrypted_text)

main()



"""The secret word is: hungry"""
