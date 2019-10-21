#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : October 2019
# This program tells the user can date the grandchild


def main():
    # this program tells the user if he can date the grandchild

    # input
    age = int(input("Enter your age: "))
    print("")

    # process & output
    if age > 25 and age < 40:
        print ("You are able to date the grandchild.")
    else:
        print("You are not able to date the grandchild.")


if __name__ == "__main__":
    main()
