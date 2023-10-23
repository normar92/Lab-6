def encode_pass(password):
    encode_pass = ""
    for i in password:
        add3 = str((int(i)+ 3) % 10)
        encode_pass += add3
    return encode_pass




if __name__ == '__main__':
    while True:
        print("Menu:\n______\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("Select a Menu Option:"))

        if option == 1:
            password = str(input("Please enter password:"))
            print(encode_pass(password))
        else:
            break