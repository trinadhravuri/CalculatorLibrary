"""
filter(function,iterable)
    * Construct an iteraor from those elements of iterable for which function returns true.
    * allows quick creation of iterables of items in another iterable that have passed a test.
"""




li = list(range(1,100))
print(li)

primes = list(filter(lambda x: not list(filter(lambda y:x%y == 0,range(2,x))),range(2,100)))
print(primes)
#print(list(filter(lambda y:x%y == 0,range(2,x))))
print(list(filter(lambda x:x%2==0,range(2,50))))
print(list(filter(lambda x:x%2!=0,range(2,50))))
print(list(filter(lambda x: not list(filter(lambda y:x%y==0,range(2,x))),range(2,100))))
print(list(filter(lambda x: list(filter(lambda y:x%y==0,range(2,x))),range(2,100))))





def primes_nums(num,d):
    if num//2 <d:
        return True
    if num%d == 0:
        return False
    return primes_nums(num,d+1)

def find_primes(num,i,result):
    if i == num + 1:
        return result
    if primes_nums(i,2):
        result.append(i)
    return find_primes(num,i+1,result)

print(find_primes(100,2,[]))
print(list(n for n in range(2,100)))
#print(list(all(n%d for d in range(2,50))))
print(list(n for n in range(2,100) if all(n%d for d in range(2,n))))


print(list(filter(lambda x:x%2 == 0,list(range(20)))))


for num in range(2,50):
    prime = True
    for i in range(2,num):
        if num%i == 0:
            prime = False

    if prime:
        print(num)
def prime_nums(li):
    primes_li = []
    for num in li:
        prime = True
        if num == 0 or num == 1:
            continue
        for i in range(2,num):
            if num%i == 0:
                prime = False
        if prime:
            primes_li.append(num)
    print(primes_li)


lis = list(range(1,51))
new_lis = [1,0,58,69,54,2,58,98,7,75,89,63,21,25,]
prime_nums(lis)

from statistics import mean
data = list(range(1,21))
avg = mean(data)
above_avg = list(filter(lambda x:x>avg,data))
print(data)
print(avg)
print(above_avg)
