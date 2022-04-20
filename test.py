import sys

def main():
    k = check(sys.argv)
    plain = input("plaintext: \n")
    print()
    print("Caesar Cipher output text: \n")

    caesar_txt = caesar(plain, k)

    for line_start in range(0, len(caesar_txt), 50):
        current_line = caesar_txt[line_start : line_start + 50]
        for block_start in range(0, len(current_line), 5):
            block = caesar_txt[line_start + block_start : line_start + block_start + 5]
            print("".join(block), end=" ")
        print()

def caesar(plain, k):
    plain = plain.upper()
    caesar_txt = []
    for letter in plain:
        if not letter.isalpha():
            continue
        offset = 65
        pi = ord(letter) - offset
        ci = (pi + k) % 26
        caesar_txt.append(chr(ci + offset))
    return caesar_txt

def check(arg):
    if len(arg) != 2 or arg[1].isalpha():
        exit("Usage is as follows ==>  python caesar.py k")
    return int(arg[1])

if __name__ == "__main__":
    main()