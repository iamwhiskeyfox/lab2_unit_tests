def find_fibonacci(x):
        try:
            if int(x) < 0:
                return 'The entered value is out of range (n must be > 0)'
            if int(x) > 100:
                return 'The entered value is out of range (n must be < 100)'
            fib1 = fib2 = 1
            n = int(x) - 2
            while n > 0:
                fib1, fib2 = fib2, fib1 + fib2
                n -= 1
            return fib2

        except TypeError:
            return 'Type Error: Entered incorrect type of values!'
        except ValueError:
            return 'Value Error: Entered incorrect values!'

