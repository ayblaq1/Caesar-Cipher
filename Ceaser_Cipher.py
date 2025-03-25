def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def main():
    print("Caesar Cipher Program")
    while True:
        mode = input("Choose mode (encrypt/decrypt/exit): ").strip().lower()
        if mode == 'exit':
            print("Exiting program.")
            break
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode. Please choose 'encrypt', 'decrypt', or 'exit'.")
            continue

        text = input("Enter your message: ")
        try:
            shift = int(input("Enter shift value (integer): "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue
        result = caesar_cipher(text, shift, mode)
        print(f"Result: {result}\n")

if _name_ == "_main_":
    main()