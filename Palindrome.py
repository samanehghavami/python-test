def main():
    text = input("enter a string: ")

    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


if __name__ == "__main__":
    main()
