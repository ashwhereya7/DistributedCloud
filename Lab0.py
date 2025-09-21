# /mnt/data/caesar_variation.py
# Caesar Cipher variation: byte-wise addition with repeating key, modulo 255.
MOD = 255

def _cycle_key(key: str, length: int) -> str:
    if not key:
        raise ValueError("Key must be non-empty")
    reps, rem = divmod(length, len(key))
    return key * reps + key[:rem]

def encrypt_ascii_codes(message: str, key: str):
    # return list of cipher byte values (0..254) via (m+k) % 255
    k = _cycle_key(key, len(message))
    return [(ord(m) + ord(kc)) % MOD for m, kc in zip(message, k)]

def decrypt_from_codes(codes, key: str) -> str:
    k = _cycle_key(key, len(codes))
    vals = [(c - ord(kc)) % MOD for c, kc in zip(codes, k)]
    return ''.join(chr(v) for v in vals)

def codes_to_text(codes) -> str:
    # displayable 1:1 mapping for all byte values
    return bytes(codes).decode('latin-1', errors='replace')

def run_case(message: str, key: str):
    codes = encrypt_ascii_codes(message, key)
    return codes_to_text(codes), '-'.join(map(str, codes)), decrypt_from_codes(codes, key)

def main():
    cases = [
        ("UTSA, Birds up!", "NPB"),
        ("Being a hacker is fun", "But risky"),
        ("True", "Today is a happy day"),
    ]
    for i, (msg, key) in enumerate(cases, 1):
        ct, codes, pt = run_case(msg, key)
        print(f"Case {i}\nMessage: {msg}\nKey: {key}")
        print(f"Encrypted message: {codes}")
        print(f"Encrypted string: {ct}")
        print(f"Decrypted string: {pt}")
        print("-"*60)

if __name__ == "__main__":
    main()
