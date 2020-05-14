#TODO FIB1 DONE
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

#def fib_even(x):
 #   fibonacci_slow(x)<400000
  #  total_sum = 0
   # for i in range(1, x):
    #    if (i%2 == 0):
     #       total_sum = total_sum+i
    #print(total_sum)
    #return total_sum
#the issue with the above code is that it was simply to clunky and was not adding things properly. I was not running the program in the actually function which simply created more issues 

#Discovered I was trying to solve the problem incorrectly
#def fib_even(x):
    #total_sum = 0
  #  while fib_even(x) < 4000000:
        #if(fib_even(x)%2==0):
           # totalsum+=fib_even(x)
          #  print(totalsum)

#could work but its a little to complicated as it creates a recursion error because it simply loops for to long 

#fib_even(5)


def even_fib(limit):
    a, b = 0, 1
    while a < limit:
        if not a % 2:         
            yield a
        a, b = b, a + b

print(sum(even_fib(4000000)))
