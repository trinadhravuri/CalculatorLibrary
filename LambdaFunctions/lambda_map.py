"""
map(function,iterable)
    * Return an iterator that applies function to every item of iterable, yielding the results
    * Allows quick application of a function to every element of an iterable

"""

nums = [1,2,3,4,5,6,7,8,9,10]
squared = list(map(lambda x:x**2,nums))
# print(squared)
# evens = list(map(lambda x:x%2==0,nums))
# print(evens)

wc_teams = [('Brazil',21),('Germany',19),('Italy',18),('Argentina',17),('France',15),('England',15),('India',23)]
print(wc_teams)

new_li = list(map(lambda team:(team[0],team[1]+1),wc_teams))
print(new_li)