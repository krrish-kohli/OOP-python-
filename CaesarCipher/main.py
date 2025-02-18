# Names: Kareem Fardoun, Krrish Kohli
# Date: 10/08/2024
# Description:
# This program allows the user to encrypt or decrypt messages using two types of cipher methods:
# Atbash cipher (a simple substitution cipher where the alphabet is reversed) and
# Caesar cipher (a substitution cipher where each letter in the plaintext is shifted by a certain number of positions).
# The user can choose to either encrypt or decrypt a message and save or read the result from a file.

# Required imports:
import check_input  # Module to handle input validation (assumed to have a function get_int_range)
from caesar import Caesar  # Caesar cipher class implementation (inherits from Cipher)
from cipher import Cipher  # Atbash cipher class for Atbash cipher implementation (Base class for inheritance)


def main():
    # Main function to drive the encryption/decryption process
    print("Secret Decoder Ring:")

    # Ask the user whether they want to encrypt or decrypt a message
    action = check_input.get_int_range("1. Encrypt\n2. Decrypt\n ", 1, 2)

    if action == 1:
        # Encryption process
        print("\nEnter encryption type:")
        print("1. Atbash")
        print("2. Caesar")

        # Get the user's choice of encryption type
        cipher_type = check_input.get_int_range("", 1, 2)

        # Input the message to be encrypted
        message = input("Enter message: ")

        if cipher_type == 2:
            # For Caesar cipher, we need the shift value to determine how much to shift each letter
            shift = check_input.get_int_range("Enter shift value (0-25): ", 0, 25)
            # create cipher using the chosen class which is caesar in this case
            cipher = Caesar(shift)  # Initialize Caesar cipher with the given shift value
        else:
            # Atbash cipher uses the Cipher class, which represents a simple substitution cipher.
            # Since Atbash uses a reversed alphabet, no shift value is needed.
            # Cipher here acts as the base class that provides the `encrypt_message` and `decrypt_message` methods.
            cipher = Cipher()  # This class acts as the base cipher

        # Encrypt the message using the chosen cipher (either Atbash or Caesar)
        encrypted_message = cipher.encrypt_message(message)

        # Save the encrypted message to a file
        with open("message.txt", "w") as file:
            file.write(encrypted_message)
        print(f"Encrypted message saved to 'message.txt'.")

    else:
        # Decryption process
        print("\nEnter decryption type:")
        print("1. Atbash")
        print("2. Caesar")

        # Get the user's choice of decryption type
        cipher_type = check_input.get_int_range("Choose decryption type: ", 1, 2)

        if cipher_type == 2:
            # For Caesar cipher, get the shift value used during encryption to correctly decrypt the message
            shift = check_input.get_int_range("Enter shift value: ", 0, 25)
            # Caesar inherits from Cipher and adds additional behavior for shifting.
            # It uses the same shift value for both encryption and decryption, so we need to ask the user for it.
            cipher = Caesar(shift)
        else:
            # Atbash cipher uses the Cipher class for decryption, and no shift value is needed.
            # This is because Cipher provides the necessary methods for both encryption and decryption of a simple substitution cipher like Atbash.
            cipher = Cipher()

        # Read the encrypted message from the file
        with open("message.txt", "r") as file:
            encrypted_message = file.read()
        print(f"Reading encrypted message from 'message.txt'.")

        # Decrypt the message using the chosen cipher (either Atbash or Caesar)
        decrypted_message = cipher.decrypt_message(encrypted_message)
        print(f"Decrypted message: {decrypted_message}\n")


# Start of the program
if __name__ == "__main__":
    main()