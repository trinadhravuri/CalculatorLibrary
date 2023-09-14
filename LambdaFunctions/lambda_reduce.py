"""
reduce(function,iterable)
 * Apply function of two arguments cumulatively to the items of sequence
    from left to right, so as to reduce the sequence to a single value.
 * Allows cumulative application of a function to every element of an iterable.
"""

from functools import reduce

nums = [1,2,3,4,5,6,7,8,9,10]
total = reduce(lambda x,y:x + y, nums)
print(total)

nums_1 = list(range(1,11))[::-1]
print(nums_1)
minus = reduce(lambda x,y:x-y,nums_1)
print(minus)
names = ['dan','darran','jonna','jackie','chris']
cons = reduce(lambda x,y:x + y[:2],names,'')
print(cons)