
def encrypt(text, key):
    encrypted = ""
    # loop through the message char by char

    for char in text:
        # check if lower case
        if char.isupper():
            char_index = ord(char) - ord("A")

            # shift current characters by key positions

            char_shifted = (char_index+key) % 26 + ord("A")
            char_new = chr(char_shifted)
            encrypted += char_new
        elif char.islower():
            char_index = ord(char) - ord("a")

            # shift current characters by key positions

            char_shifted = (char_index+key) % 26 + ord("a")
            char_new = chr(char_shifted)
            encrypted += char_new
        elif char.isdecimal():

            # shift current characters by key positions

            char_new = (int(char)+key) % 10
            encrypted += str(char_new)
        else:
            encrypted += char
    return encrypted


def decrypt(text, key):
    encrypted = ""
    # loop through the message char by char

    for char in text:
        # check if lower case
        if char.isupper():
            char_index = ord(char) - ord("A")

            # shift current characters by key positions

            char_shifted = (char_index-key) % 26 + ord("A")
            char_new = chr(char_shifted)
            encrypted += char_new
        elif char.islower():
            char_index = ord(char) - ord("a")

            # shift current characters by key positions

            char_shifted = (char_index-key) % 26 + ord("a")
            char_new = chr(char_shifted)
            encrypted += char_new
        elif char.isdecimal():

            # shift current characters by key positions

            char_new = (int(char)-key) % 10
            encrypted += str(char_new)
        else:
            encrypted += char
    return encrypted


def brute_force(text):
    i = 0
    while True:
        decrypted = decrypt(text, i)
        print()
        print(decrypted)
        print()
        ans = input("Is this correct? y/n\n").lower()
        if ans == "y":
            return(decrypted)
            break
        i += 1


def main():
    message = "kbhfmtlbsepolfo"
    encrypted_message = encrypt(message, 40)
    print(f"Message: {message}")
    print(f"One shifted message: {encrypted_message}")
    print(f"Decrypted message: {brute_force(encrypted_message)}")


if __name__ == "__main__":
    main()
