#Norma Marin
#COP3502C - Software Engineering (Password Encoder/Decoder)
# Lab Partner Tara M. Pattilachan
#10/23/2023
#Lab 6 - Assignment

def encode_pass(password):
    encode_pass = ""
    for i in password:
        add3 = str((int(i) + 3) % 10)
        encode_pass += add3
    return encode_pass

def decoded_password(password):
    pass

def main():

    while True:
        print("\nMenu:")
        print("------------")
        print("1. Encode\n2. Decode\n3. Quit")
        option = int(input("Select a Menu Option:"))

        if option == 1:
            password = str(input("Please enter your password to encode:"))
            if len(password) == 8 and password.isdigit():
                encoded_pass = encode_pass(password)
                print("Your password has been encoded and stored!")
            else:
                print("Please enter a valid 8-digit password.\n")
        if option == 2:
            if encode_pass:
                print(f'The encoded password is {encoded_pass}, and the original password is {password}. \n')
            else:
                print("You need a password encoded first!\n")

            print(decoded_password(password))
        elif option == 3:
            break
    else:
        print("Please input a valid  menu selection.\n")

if __name__ == '__main__':
    main()