#def fibonacci_slow(n):
   # if n == 1:
      #  return 1
    #base case for fib numbers
   # elif n == 2:
       # return 1 
    #second base case for fib numbers
    #else:
     #   return fibonacci_slow(n-2) + fibonacci_slow(n-1)
    #finds the values of any fib number after the third fib number
    #not neccessary for current function

#def fib_even(x):
 #   fibonacci_slow(x)<400000
  #  total_sum = 0
   # for i in range(1, x):
    #    if (i%2 == 0):
     #       total_sum = total_sum+i
    #print(total_sum)
    #return total_sum
#the issue with the above code is that it was simply to clunky and was not adding things properly. I was not running the program in the actually function which simply created more issues.
#main issue is that I don't actually make use of the fibonacci function so it is kinda useless fo even inlcued and it does not know what it is idividing by 

#Discovered I was trying to solve the problem incorrectly
#def fib_even(x):
    #total_sum = 0
  #  while fib_even(x) < 4000000:
        #if(fib_even(x)%2==0):
           # totalsum+=fib_even(x)
          #  print(totalsum)
#could work but its a little to complicated as it creates a recursion error because it simply loops for to long 


def even_fib(limit):
    a, b = 0, 1
    #defining variables, works for any situation not just for the project euler question
    while a < limit:
    #a being the smallest unit to compare it to 
        if not a % 2: 
            #checking to  ensure that it is divisible by 2        
            yield a
            #a new function that I discovered that works similar to a return function but does nnot end the function when exicuted
        a, b = b, a + b
        #redefines the variables according to fibonacci sequence 

print(sum(even_fib(4000000)))
