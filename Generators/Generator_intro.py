"""
* what generators are and how to use them
* How to create generator functions and expressions
* How the python Yield statement works
* How to use multiple Yield statements in a generator function
* how to use advanced generator methods
* how to build data pipelines with multiple generators
"""

def infinite_seq():
    num = 0
    while True:
        yield num
        num += 1

# print(infinite_seq())
infinite = infinite_seq()
# print(next(infinite))
# print(next(infinite))
# print(next(infinite))
# print(next(infinite))
# print(next(infinite))
# print(next(infinite))



for i in range(1,10):
    n = next(infinite)
    print(n+n)