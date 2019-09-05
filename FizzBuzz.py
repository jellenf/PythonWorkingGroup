###For every number from 1 to 100, output Fizz if the number is divisible by 3, output Buzz if the number is divisible by 5, and output FizzBuzz if the number is divisible by both 3 and 5. If none of these conditions match, then just output the number.

for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
