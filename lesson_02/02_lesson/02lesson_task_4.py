def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0 or i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)
