#FIZZ-BUZZ GAME

#DIVISIBLE BY 3 FIZZ (Multiple of 3)
#DIVISIBLE BY 5 BUZZ (Multiple of 5)
#DIVISIBLE BY 5 AND 3 FIZZBUZZ (multiple of both 3 and 5)


#Printing numbers from 1 to 50
"""
for i in range(1,51):
    if(i%3==0):
        print(str(i) + " = Fizz")
    else:
        if(i%5==0):
            print(str(i) + " = Buzz")
        else:
            if(i%3==0 and i%5==0):
                print(str(i) + " = FizzBuzz")
            else:
                print(str(i))

# We are facing a problem where FizzBuzz is not printing because
the program exits on checking if it is divisible by 3
So the FizzBuzz won't prints
"""
def FizzBuzz(r):
    for i in range(1,r):
        if(i%3 == 0 and i%5 == 0):
            print(str(i) + " = FizzBuzz")
        else:
            if(i%3 == 0):
                print(str(i) + " = Fizz")
            else:
                if(i%5 == 0):
                    print(str(i) + " = Buzz")
                else:
                    print(str(i))
                    
FizzBuzz(51)




