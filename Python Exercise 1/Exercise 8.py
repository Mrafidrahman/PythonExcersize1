def number(num):
    stored_number = 6
    if num > stored_number:
        print('Your guess is higher')
    elif num < stored_number:
        print('Your guess is almost there')
    elif num == stored_number:
        print('Your guess is Correct')
        
num = int(input("Enter a number between 1 and 9: "))
number(num)
