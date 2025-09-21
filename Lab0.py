# Author: Aishwarya Patel
# Date: September 21, 2025
# Course: CS 4663-901 Distributed and Cloud Systems Security
# Project: Lab 0 - Simple Interactive Caesar Cipher Variant
# Description: Simple interactive Caesar cipher variant
# to add plaintext byte to key byte (repeating key) mod 255.

MOD = 255

def _cycle_key(key: str, length: int) -> str:
    if not key:
        raise ValueError("Key must be non-empty")
    reps, rem = divmod(length, len(key))
    return key * reps + key[:rem]

def encrypt_ascii_codes(message: str, key: str):
    k = _cycle_key(key, len(message))
    return [(ord(m) + ord(kc)) % MOD for m, kc in zip(message, k)]

def to_signed8(v: int) -> int:
    return v if v < 128 else v - 256

def decrypt_from_codes(codes, key: str) -> str:
    k = _cycle_key(key, len(codes))
    vals = [(c - ord(kc)) % MOD for c, kc in zip(codes, k)]
    return ''.join(chr(v) for v in vals)

def codes_to_text(codes) -> str:
    return bytes(codes).decode('latin-1', errors='replace')

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