"""
1. What is Lambda Function?
    A lambda function is a simple throw away function which is designed to
    write in inline code.
    These are also known as :
        Lambda Expressions
        Anonymous functions
        lambda abstractions
        lambda form
        functions Literals

    standard functions          Lambda Functions
    * Used many times           * intended for single use
    * Multiple lines of code    * Defined in a single line
    * Named only                * Named and anonymous
    * None or more inputs       * None or more inputs
    * None or more returns      * one or more returns

2. Where are Lambda Functions Useful?
    * Lambda functions are useful as small, "throwaway" single line functions.
    * They are often useful to allow quick calculations or processing as the
        input to other functions.
    * They can make code easier to read if they are used appropriately.
3. Lambda Functions With Sort, Filter,Map and reduce
4. Testing Lambda Functions

"""

def myfunc(x,y,z):
    result = x + y + z
    return result

print(myfunc(10,20,30))

#lambda 10,20,30:10+20+30
#
def second(x):
    return x[1]
a = [(1,2),(2,5),(3,1),(4,15)]
b = [(3,2,5),(2,5,6),(0,1,8),(2,15,2)]
l = [2,5,6,7,1,9,3,4,8,11]
l.sort()
print(l)

a.sort()
print(a)
print(a[1])
print(second(a))
a.sort(key=second)
print(a)
print(b)
print(second(b))
b.sort(key=second)
print(b)

