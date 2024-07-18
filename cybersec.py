def caesar_cipher(text, shift, mode):
    encrypted_text = ""

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine the appropriate case (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Apply the shift and ensure it wraps around using modulo operation
            shifted = (ord(char) - base + shift) % 26 + base
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  # Non-alphabetical characters remain unchanged
    
    if mode == 'encrypt':
        return encrypted_text
    elif mode == 'decrypt':
        # Decryption is simply encryption with a negative shift
        decrypted_text = ""
        for char in encrypted_text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base - shift) % 26 + base
                decrypted_text += chr(shifted)
            else:
                decrypted_text += char
        return decrypted_text
    else:
        return "Invalid mode. Please use 'encrypt' or 'decrypt'."

# Example usage:
def main():
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (a positive integer): "))
    mode = input("Encrypt or Decrypt? ").lower()

    encrypted_message = caesar_cipher(message, shift, mode)

    if mode == 'encrypt':
        print(f"Encrypted message: {encrypted_message}")
    elif mode == 'decrypt':
        print(f"Decrypted message: {encrypted_message}")

if __name__ == "__main__":
    main()
