list1 = ['34', '89', '67' , '45', '21']


# list2 = list(map(float,list1))
# print(list2)   # [34.0, 89.0, 67.0, 45.0, 21.0]

# # Cube ----------


# list6 = list(map(lambda x : x**3,list2))
# print(list6)

# x = list(map(int,input().split()))

# print(x)


# str1 = "Hello My Name is Uja Tanna"
# print(str1.split(' '))   # ['Hello', 'My', 'Name', 'is', 'Uja', 'Tanna']


list2 = [190,90,67,56,24,12]
print(sum(list2)/len(list2))
lst6 = list(filter(lambda x : (sum(list2)/len(list2)) < x, list2 )) 
print(lst6)

import statistics
lst6 = list(filter(lambda x : statistics.mean(list2) < x, list2 )) 
lst6 = list(map(lambda x : statistics.mean(list2) < x, list2 )) 
print(lst6)   # [190, 90]


# Reduce

from functools import reduce

list2 = [190,90,67,56,24,12]
res = reduce(lambda x,y : x+y, list2)
print(res)   # 439


from itertools import accumulate

res1 = tuple(accumulate(list2, lambda x,y : x + y))
print(res1)   # (190, 280, 347, 403, 427, 439)

num = 6
print(reduce(lambda x,y : x*y, [x for x in range(1,num+1)]))


# Recursion

# when function calls itself then it is called as Recursion

def fibonnacci(num):
    n1,n2 = 0,1
    print(n1,n2,end=' ')

    for i in range(num-2):
        n3 = n1 + n2
        print(n3,end=' ')
        n1 = n2
        n2 = n3

fibonnacci(5)

# Recursion
print()
print()
from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonnacci_rec(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonnacci_rec(num-1) + fibonnacci_rec(num-2)

# print(fibonnacci_rec(5))

for i in range(50):
    print(fibonnacci_rec(i),end=' ')

# Factorial using Recursion, Map, reduce, filter ---> 5 Programs