#Norma Marin
#Lab Partner: Tara Pattilachan
#COP3502C - Lab 6
#10/23/2023

def encode_pass(password):
    encode_pass = ""
    for i in password:
        add3 = str((int(i)+ 3) % 10)
        encode_pass += add3
    return encode_pass

def decode_pass(encode_pass):
    decode_pass = ""
    for i in encode_pass:
        subtract3 = str((int(i) - 3) % 10)
        decode_pass += subtract3
    return decode_pass


if __name__ == '__main__':
    #Stores last encoded password
    encoded_pass = None
    while True:
        print("Menu:\n______\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("Select a Menu Option: "))

        if option == 1:
            password = str(input("Please enter your password to encode: "))
            encoded_pass = encode_pass(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            if encoded_pass:
                print(f"The encoded password is {encoded_pass}, and the original password is {decode_pass(encoded_pass)}.\n")
            else:
                print("You need to encode a password first!\n")
        elif option == 3:
            break
        else:
            print("Invalid option. Please select a valid menu option.\n")