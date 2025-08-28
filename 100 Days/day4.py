# dia 4 
def fizzbuzz(fizz_num,buzz_num, n):
    for i in range(1, n + 1):
        if i % fizz_num == 0 and i % buzz_num == 0:
            print("FizzBuzz")
        elif i % fizz_num == 0:
            print("Fizz")
        else:
            print("Buzz")
fizzbuzz(3,5, 100)
        
