# Author: Aishwarya Patel (gfu786)
# Date: September 21, 2025
# Course: CS 4663-901 Distributed and Cloud Systems Security
# Project: Lab 0 - Simple Interactive Caesar Cipher Variant
# Description: Simple interactive Caesar cipher variant
# to add plaintext byte to key byte (repeating key) mod 255.

# Work in a single byte by adding ASCII values and wrap around using mod 255
MOD = 255

# Repeat (pad) the key so it matches the message length.
# - Empty keys are not allowed.
# - divmod tells us how many full repeats we need (reps) and how many extra chars (rem).
# - Return the repeated key plus the first 'rem' chars.
def _cycle_key(key: str, length: int) -> str:
    if not key:
        raise ValueError("Key must be non-empty")
    reps, rem = divmod(length, len(key))
    return key * reps + key[:rem]

# Pad/repeat the key to the message length, as required
# Encrypt to add each message char to its key char and wrap in one byte (mod 255)
def encrypt_ascii_codes(message: str, key: str):
    k = _cycle_key(key, len(message))
    return [(ord(m) + ord(kc)) % MOD for m, kc in zip(message, k)]

# Optional display helper to show a byte as signed 8-bit
def to_signed8(v: int) -> int:
    return v if v < 128 else v - 256

# Use the same padded key length as the cipher length
# Decrypt to reverse the addition → subtract key and wrap with mod 255
# Turn numeric codes back into characters
def decrypt_from_codes(codes, key: str) -> str:
    k = _cycle_key(key, len(codes))
    vals = [(c - ord(kc)) % MOD for c, kc in zip(codes, k)]
    return ''.join(chr(v) for v in vals)

# Show cipher bytes as characters using a 1:1 mapping (Latin-1 keeps 0–255 unchanged)
def codes_to_text(codes) -> str:
    return bytes(codes).decode('latin-1', errors='replace')


# Prompt the user for message and key, then show encrypted and decrypted results
# Encrypt the message using the repeated key (sum ASCII, wrap mod 255)
# Print the cipher as hyphen-separated numbers.
# Show the cipher as characters (Latin-1 keeps 0–255 one-to-one)
# Decrypt to confirm we recover the original plaintext
# Include a simple error message for instance like an empty key
def main():
    try:
        message = input("Enter your message: ")
        key = input("Enter your key: ")
        codes = encrypt_ascii_codes(message, key)
        #signed = [to_signed8(v) for v in codes]
        #print("\nEncrypted message:" + "-".join(str(x) for x in signed))
        print("\nEncrypted message:" + "-" + "-".join(str(x) for x in codes))
        print("\nEncrypted string: " + codes_to_text(codes))
        print("\nDecrypted string: " + decrypt_from_codes(codes, key))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
