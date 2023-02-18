# print("Hello" in "Hello world")


# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list1 = list2 + list1
# print(list1)
# list1.extend(list2)
# print(list1)
# for x in list2:
#     list1.append(x)
# print(list1)

# fruits = ["apple", "banana", "cherry", "apple", "mango"]
# apples = [x for x in fruits if x != "apple"]
# print(apples)

# from collections import defaultdict  
# d = defaultdict(int) 
# L = [1, 2, 3, 4, 2, 4, 1, 2]  
# for i in L:  
#     d[i] += 1 
# print(d)


from collections import deque
de = deque([1,2,3]) 
de.append(4) 
de.popleft() 
print(de)

import math
x = math.ceil(1.4)
print(x)
import math
x = math.floor(1.4)
print(x)
