from cipher import Cipher


class Caesar(Cipher):
    """This class extends the Cipher class to provide methods for encrypting and decrypting messages using the Caesar cipher, where the encrypted message is found by looking up each letter and finding the corresponding letter in a shifted alphabet"""

    def __init__(self, shift):
        """Initializes the Caesar class with the shift value."""
        super().__init__()
        self._shift = shift

    def _encrypt_letter(self, letter):
        """Encrypts a single letter using the Caesar cipher."""
        index = (self._alphabet.index(letter) + self._shift) % len(self._alphabet)
        return self._alphabet[index]

    def _decrypt_letter(self, letter):
        """Decrypts a single letter using the Caesar cipher."""
        index = (self._alphabet.index(letter) - self._shift) % len(self._alphabet)
        return self._alphabet[index]
