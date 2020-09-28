from fibo import find_fibonacci
import os
print('\n')
os.system('cls')
print('<<< Find Fibonacci program started successfully.\n')
print('\n')
while True:
    n = input('Enter the serial number\n >>>> ')
    result = find_fibonacci(n)
    print('Result: ', result)
    sys = input('Enter " + " for continue or " - " for exit\n >>>> ')
    if sys == '+':
        os.system('cls')
        pass
    if sys == '-':
        break
