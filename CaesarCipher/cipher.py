class Cipher:
    """This class provides methods to encrypt and decrypt messages using the Atbash cipher, which is a substitution cipher where the encrypted message is obtained by looking up each letter and finding the corresponding letter in a reversed alphabet"""

    def __init__(self):
        """Initializes the Cipher class with the alphabet."""
        self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encrypt_message(self, message):
        """Encrypts the provided message using the Atbash cipher."""
        encrypted_message = ''.join([self._encrypt_letter(letter) if letter.isalpha() else letter for letter in message.upper()])
        return encrypted_message

    def decrypt_message(self, message):
        """Decrypts the provided message using the Atbash cipher."""
        decrypted_message = ''.join([self._decrypt_letter(letter) if letter.isalpha() else letter for letter in message.upper()])
        return decrypted_message

    def _encrypt_letter(self, letter):
        """Encrypts a single letter using the Atbash cipher."""
        index = self._alphabet.index(letter)
        return self._alphabet[-(index + 1)]

    def _decrypt_letter(self, letter):
        """Decrypts a single letter using the Atbash cipher."""
        index = self._alphabet.index(letter)
        return self._alphabet[-(index + 1)]
