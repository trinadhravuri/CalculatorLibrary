cmp = ['Michael Collins',
       'Richard Gordan',
       'Jack Swigert',
       'Stuart Roosa',
       'Alfred Worden',
       'Ken Mattingly',
       'Ron Evans']
cmp_li = [[1,2],[2,3],[5,2],[4,8],[3,1]]
cmp_tu = [(1,2),(2,3),(5,2),(4,8),(3,1)]
people = [('trinadh',29),('tarun',30),('sree',26),('ramya',25)]
def sorting_fun(a):
    return a[1]
def sir_name_sort(a):
    return a.split()[1]
print(cmp)
cmp.sort(key = lambda x:x.split()[1])
print(cmp)
print(cmp_li)
cmp_li.sort(key=sorting_fun)
print(cmp_li)
print(cmp_tu)
cmp_tu.sort()
print(cmp_tu)
print(people)
people.sort(key = lambda x:x[1])
print(people)



class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def __repr__(self):
        return f"{self.name} : {self.age}"


alex = Person('Alex',37)
trinadh = Person('Trinadh',36)
tarun = Person('Tarun',30)
p = [alex,trinadh,tarun]
print(p)
p.sort(key = lambda x:x.age)
print(p)


nicknames = ['Diamondbacks','Braves','Orioles','Red Sox','Cubs','White Sox','Reds','Indians','Rockies']

print(nicknames)
short_names = list(filter(lambda x:len(x)<6,nicknames))
print(short_names)