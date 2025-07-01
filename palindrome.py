def is_palindrome(num):
    original = str(num)
    reverse = original[::-1]
    if original == reverse:
        print(num, "is a palindrome")
    else:
        print(num,"is not a palindrome")
number = input("Enter a number: ")
is_palindrome(number)
