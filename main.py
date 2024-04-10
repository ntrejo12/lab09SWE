from encoder import *

if __name__ == '__main__':
    check = True
    while check is True:
        print("Menu")
        print("-------------")
        print("1. Encode\n2. Decode\n3. Quit\n")

        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            new_password = encoder(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            new_password = encoder(password)
            print(f"The encoded password is {new_password}, and the original password is {password}\n")
        elif option == 3:
            check = False