import string

alphabet = string.ascii_lowercase #alphabet list

def caesar(encode_decode, original_text, shift_amount):

    result = ""

    if encode_decode == "decode":
        shift_amount *= -1

    for i in original_text:
        if i in alphabet:
            num = alphabet[alphabet.index(i.lower()) + shift_amount]
            if i.isupper():
                result += num.upper()
            else:
                result += num
        else:
            result += i

    print(f"Here is the text: {result}")

end = False
while not end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in["encode", "decode"]:
        print("Invalid input! Please indicate if you want to ENCODE or DECODE.\n")
        continue

    text = input("Type your message:\n").lower()

    try:
        shift = int(input("Type the shift number:\n")) % 26
    except ValueError:
        print("Invalid input! Please enter an integer value.\n")
        continue

    caesar(encode_decode=direction, original_text=text, shift_amount=shift)

    restart = input("Type yes if you want to use the cipher again.")
    if restart.strip().lower() == "yes":
        continue
    else:
        break


