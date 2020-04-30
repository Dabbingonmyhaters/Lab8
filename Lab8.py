#day 1 progres
def fibonacci_slow(n):
    if n == 1:
        return 1
    #base case for fib numbers
    elif n == 2:
        return 1 
    #second base case for fib numbers
    else:
        return fibonacci_slow(n-2) + fibonacci_slow(n-1)
    #finds the values of any fib number after the third fib number

def fib_even(x):
    fibonacci_slow(x)<400000
    #set the limit incase the function exceeds 4 million
    total_sum = 0
    #starting value to begin adding
    for i in range(1, x):
        if (i%2 == 0):
            total_sum = total_sum+i
    #essentially a for lup to continually add to get the sum of the even numbers. 
    print(total_sum)
    return total_sum


fib_even(5)



