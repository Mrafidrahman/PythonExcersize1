def number(num):
    if num%3==0 and num%5==0:
        print('FizzBuzz')
    elif num%5==0:
        print('Buzz')
    elif num%3==0:
        print('Fizz')
    else:
        print('Not a Fizz-Buzz number')
        
num = int(input('Enter a number: '))
number(num)
