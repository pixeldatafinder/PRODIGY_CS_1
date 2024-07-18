First step toeards cyber security
caeser cipher
The Caesar Cipher algorithm is a straightforward encryption technique where each letter in the plaintext is shifted a fixed number of places down or up the alphabet.
Here’s a step-by-step explanation of the algorithm:

### Algorithm:

1. **Input Parameters:**
   - **Plaintext**: The original message that you want to encrypt.
   - **Shift (Key)**: A positive integer value indicating the number of positions each letter in the plaintext should be shifted in the alphabet.

2. **Encryption Process:**
   - Iterate through each character in the plaintext.
   - For each alphabetic character:
     - Determine if it's uppercase or lowercase.
     - Compute the new character by shifting it in the alphabet by the specified number of positions.
     - Handle wrapping around the alphabet using modulo arithmetic to ensure that shifts beyond 'Z' wrap back to 'A'.
     - Non-alphabetic characters (like spaces or punctuation) remain unchanged.
   - Construct the ciphertext by appending each transformed character.

3. **Decryption Process:**
   - To decrypt the ciphertext, apply the inverse of the encryption process:
     - Use the negative of the original shift value to shift each character backwards in the alphabet.
     - Again, handle wrapping around the alphabet using modulo arithmetic.
     - Non-alphabetic characters remain unchanged.

4. **Example:**
   - **Encryption**: Encrypt the plaintext "HELLO" with a shift of 3.
     - 'H' (shifted 3 positions forward) becomes 'K'
     - 'E' (shifted 3 positions forward) becomes 'H'
     - 'L' (shifted 3 positions forward) becomes 'O'
     - 'O' (shifted 3 positions forward) becomes 'R'
     - Therefore, "HELLO" encrypts to "KHOOR".

   - **Decryption**: Decrypt the ciphertext "KHOOR" (shifted with a key of 3).
     - 'K' (shifted 3 positions backward) becomes 'H'
     - 'H' (shifted 3 positions backward) becomes 'E'
     - 'O' (shifted 3 positions backward) becomes 'L'
     - 'O' (shifted 3 positions backward) becomes 'L'
     - 'R' (shifted 3 positions backward) becomes 'O'
     - Therefore, "KHOOR" decrypts to "HELLO".

### Implementation in Python:
Here's a basic Python implementation of the Caesar Cipher algorithm:

```python
def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine the appropriate case (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Apply the shift and ensure it wraps around using modulo operation
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char  # Non-alphabetical characters remain unchanged
    
    if mode == 'encrypt':
        return result
    elif mode == 'decrypt':
        # Decryption is simply encryption with a negative shift
        decrypted_text = ""
        for char in result:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base - shift) % 26 + base
                decrypted_text += chr(shifted)
            else:
                decrypted_text += char
        return decrypted_text
    else:
        return "Invalid mode. Please use 'encrypt' or 'decrypt'."
```

### Explanation of the Python Implementation:
- **Function `caesar_cipher(text, shift, mode)`**:
  - Takes three parameters:
    - `text`: The string to be encrypted or decrypted.
    - `shift`: An integer representing the number of positions to shift each letter.
    - `mode`: A string indicating whether to 'encrypt' or 'decrypt'.
  - Iterates through each character in `text`.
  - Checks if the character is a letter (`char.isalpha()`). If true:
    - Determines the base (ASCII value of 'A' or 'a' depending on case).
    - Computes the shifted ASCII value using modulo arithmetic to handle wrapping around the alphabet.
    - Appends the shifted character to `result`.
  - Non-alphabetic characters are appended unchanged to `result`.
  - If `mode` is 'encrypt', returns `result`. If `mode` is 'decrypt', performs decryption by reversing the shift and returns the decrypted text.

### Usage:
- You can use this function by calling it with appropriate parameters to encrypt or decrypt messages using the Caesar Cipher with a specified shift value.

This implementation demonstrates the core concepts of the Caesar Cipher algorithm in Python, allowing you to encrypt and decrypt messages using a simple shift of the alphabet.
