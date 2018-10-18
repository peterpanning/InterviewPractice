def fizz_buzz(n):
    while n != 0:
        if n % 5 == 0:
            print "Buzz!"
        else:
            print "Fizz!"
        n = n - 1
    print "FizzBuzz!"


def fizz_buzz_rec(n):
    if n == 0:
        print "FizzBuzz!"
        return
    elif n % 5 == 0:
        print "Buzz!"
    else:
        print "Fizz!"
    return fizz_buzz_rec(n - 1)


