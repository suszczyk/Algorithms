# Search ID


#### Exercise

```text
Create a container to store natural numbers eleven-digit ID (no more than 20000).

The container should implement two basic functionalities - adding a new number and searching for a number (with possible information that the number is not in the database).

Please perform the following operations on this container: 
Put there 18000 random numbers, and then search for 20000 random numbers.

The task is to compare the time complexity of these operations in a situation where: 
* The container is an unbalanced BST tree
* The container is an array with open addressing
* AVL trees
* An array with hashing, where collisions are resolved using lists
* An array with cuckoo hashing
```


---

I assumed the generation of IDs from `10000000000` to `9999999999999`. A total of 11 digits. For each container, I first performed an addition of `18000` IDs, then a search for `20000` IDs and additionally searching larger number to check the correctness of the search. In the examples with trees, I used the code from the class.


## Unbalanced Binary Search Tree

#### Code

```python
import random
import time


class node(object):
    def __init__(self, number=None):
        self.number = number
        self.left = None
        self.right = None
        self.parent = None


class tree(object):

    def __init__(self):
        self.dummy = node()

    def Add(self, num, nd=None):
        if(nd == None):
            nd = self.dummy.right
        if(nd == None):
            self.dummy.right = node(num)
            self.dummy.right.parent = self.dummy
            return
        if(nd.number > num):
            if(nd.left == None):
                nd.left = node(num)
                nd.left.parent = nd
                return
            else:
                self.Add(num, nd.left)
                return
        elif(nd.number < num):
            if(nd.right == None):
                nd.right = node(num)
                nd.right.parent = nd
                return
            else:
                self.Add(num, nd.right)
                return
        else:
            return

    def Find(self, num, nd="u"):

        if(nd == "u"):
            nd = self.dummy.right

        if(nd == None):

            return None
        if(nd.number == num):
            return nd
        if(nd.number > num):
            return self.Find(num, nd.left)

        else:
            return self.Find(num, nd.right)


t = tree()

# ADDITION
add_start = time.time()
for _ in range(18000):
    id = random.randint(10000000000, 99999999999)
    t.Add(id)
add_stop = time.time()
print("Addition time: ", add_stop-add_start)

# SEARCH
search_start = time.time()
for _ in range(20000):
    id = random.randint(10000000000, 99999999999)
    n = t.Find(int(id))
    if n == None:
        continue
    else:
        print("Found ID: ", id, "in object: ", n)
search_stop = time.time()

print("Search time: ", search_stop-search_start)

```

#### Times

```text
Addition time:  0.08878946304321289
Search time:  0.10722589492797852
```



#### Times (increased searched numbers)

```text
Addition time:  0.1077127456665039
Found ID:  87420962750 in object:  <__main__.node object at 0x000001EB18D48D90>
Found ID:  84041372662 in object:  <__main__.node object at 0x000001EB18D67FD0>
Search time:  110.80048274993896
```

---

## Open-addressed array

### Linear

#### Code

```python
import random
import time

tab = [None]*20000


def FindOrAdd(tab, number):
    place = number % 20000
    while True:
        if tab[place] == number:
            print("Found ID: ", tab[place], "on index: ", place)
            return place
        if tab[place] is None:
            tab[place] = number
            break
        else:
            number += 1
            place = ((number) % 20000)
            break


add_start = time.time()
for _ in range(18000):
    id = random.randint(10000000000, 99999999999)
    FindOrAdd(tab, id)
add_stop = time.time()
print("Addition time: ", add_stop-add_start)


search_start = time.time()
for _ in range(20000):
    id = random.randint(10000000000, 99999999999)
    FindOrAdd(tab, id)
search_stop = time.time()
print("Search time: ", search_stop-search_start)
```

#### Times

```text
Addition time:  0.01795220375061035
Search time:  0.02194070816040039
```

A significant increase in the number of searched IDs (from `20000` to `20000000`) already allows to find several in the database.

#### Times (increased searched numbers)

```text
Addition time:  0.01795196533203125
Found ID:  75605448672 on index:  8672
Found ID:  84737638648 on index:  18648
Found ID:  23157542335 on index:  2335
Search time:  20.145822525024414
```

---

### Quadratic

#### Code

```python
import random
import time


tab = [None]*20000


def FindOrAdd(tab, number):
    place = number % 20000
    i = 0
    while True:
        if tab[place] == number:
            print("Found ID: ", tab[place], "on index: ", place)
            return place
        if tab[place] is None:
            tab[place] = number
            break

        else:
            number = number+(i*i)
            place = number % 20000
            i += 1
            break


# ADDITION
add_start = time.time()
for _ in range(18000):
    id = random.randint(10000000000, 99999999999)
    FindOrAdd(tab, id)
add_stop = time.time()
print("Addition time: ", add_stop-add_start)

# SEARCH
search_start = time.time()
for _ in range(20000):
    id = random.randint(10000000000, 99999999999)
    FindOrAdd(tab, id)
search_stop = time.time()
print("Search time: ", search_stop-search_start)
```

#### Times 

```text
Addition time:  0.01795172691345215
Search time:  0.020945072174072266
```


#### Times (increased searched numbers)

```text
Addition time:  0.018949270248413086
Found ID:  85874626342 on index:  6342
Found ID:  37047960601 on index:  601
Found ID:  67989329080 on index:  9080
Found ID:  78865359492 on index:  19492
Found ID:  42927616178 on index:  16178
Found ID:  32476831553 on index:  11553
Search time:  22.07998538017273
```

---

### Double Hashing

#### Code

```python
import random
import time

tab = [None]*20000


def Hasz1(number):
    return number % 20000


def Hasz2(number):
    return 5-(number % 17000)


def FindOrAdd(tab, number):
    i = 0
    place = (Hasz1(number)+i) % 20000
    while True:
        if tab[place] == number:
            print("Found ID: ", tab[place], "on index: ", place)
            return place
        if tab[place] is None:
            tab[place] = number
            break

        else:
            i += 1
            number = Hasz1(number)+(Hasz2(number)//i)
            place = number % 20000
            break


# ADDITION
add_start = time.time()
for _ in range(18000):
    id = random.randint(10000000000, 99999999999)
    FindOrAdd(tab, id)
add_stop = time.time()
print("Addition time: ", add_stop-add_start)


# SEARCH
search_start = time.time()
for _ in range(20000):
    id = random.randint(10000000000, 99999999999)
    FindOrAdd(tab, id)
search_stop = time.time()
print("Search time: ", search_stop-search_start)
```

#### Times 

```text
Addition time:  0.027271032333374023
Search time:  0.03242015838623047
```


#### Times (increased searched numbers)

```text
Addition time:  0.021941423416137695
Found ID:  16033603543 on index:  3543
Found ID:  68173266078 on index:  6078
Found ID:  49259789397 on index:  9397
Search time:  28.78383779525757
```
---

## AVL Trees

#### Code

```python
import random
import time
import math


class node(object):
    def __init__(self, number=None):
        self.number = number
        self.left = None
        self.right = None
        self.parent = None


class tree(object):
    def __init__(self):
        self.dummy = node()

    def Add(self, num, nd=None):
        if(nd == None):
            nd = self.dummy.right
        if(nd == None):
            self.dummy.right = node(num)
            self.dummy.right.parent = self.dummy
            return
        if(nd.number > num):
            if(nd.left == None):
                nd.left = node(num)
                nd.left.parent = nd
                return
            else:
                self.Add(num, nd.left)
                return
        elif(nd.number < num):
            if(nd.right == None):
                nd.right = node(num)
                nd.right.parent = nd
                return
            else:
                self.Add(num, nd.right)
                return
        else:
            return

    def Find(self, num, nd="u"):

        if(nd == "u"):
            nd = self.dummy.right

        if(nd == None):

            return None
        if(nd.number == num):
            return nd
        if(nd.number > num):
            return self.Find(num, nd.left)

        else:
            return self.Find(num, nd.right)

    def Rotate(self, B):
        if (B == self.dummy or B == None or B == self.dummy.right):
            return
        A = B.parent
        P = A.parent
        if A.left == B:
            Beta = B.right
            B.parent = P
            if P.left == A:
                P.left = B
            else:
                P.right = B

            A.parent = B
            B.right = A

            A.left = Beta
            if(Beta != None):
                Beta.parent = A
        else:
            Beta = B.left
            B.parent = P
            if P.left == A:
                P.left = B
            else:
                P.right = B

            A.parent = B
            B.left = A

            A.right = Beta
            if(Beta != None):
                Beta.parent = A

    def DSW(self):
        nd = self.dummy.right
        licznik = 0
        while nd != None:
            if nd.left != None:
                self.Rotate(nd.left)
                nd = nd.parent
            else:
                nd = nd.right
                licznik += 1
        m = pow(2, int(math.log(licznik + 1, 2))) - 1
        nd = self.dummy.right
        for _ in range(licznik - m):
            self.Rotate(nd.right)
            nd = nd.parent.right

        while m > 0:
            m = m // 2
            nd = self.dummy.right
            for _ in range(m):
                self.Rotate(nd.right)
                nd = nd.parent.right


t = tree()

#ADDITION
add_start = time.time()
for _ in range(18000):
    id = random.randint(10000000000, 99999999999)
    t.Add(id)
add_stop = time.time()
print("Addition time: ", add_stop-add_start)


t.DSW()

#SEARCH
search_start = time.time()
for _ in range(20000):
    id = random.randint(10000000000, 99999999999)
    n = t.Find(id)
    if n == None:
        continue
    else:
        print("Found ID: ", id, "in object: ", n)
search_stop = time.time()

print("Search time: ", search_stop-search_start)
```

#### Times 

```text
Addition time:  0.10571670532226562
Search time:  0.08975958824157715
```


#### Times (increased searched numbers)

```text
Addition time:  0.09871149063110352
Found ID:  40014178374 in object:  <__main__.node object at 0x0000018759893130>
Found ID:  60490612671 in object:  <__main__.node object at 0x00000187597E86D0>
Found ID:  90732767575 in object:  <__main__.node object at 0x00000187599F4D00>
Found ID:  28846004319 in object:  <__main__.node object at 0x0000018759969370>
Found ID:  93314353147 in object:  <__main__.node object at 0x00000187599CD1C0>
Found ID:  97002476410 in object:  <__main__.node object at 0x0000018759A28490>
Found ID:  65115555347 in object:  <__main__.node object at 0x000001875982EE20>
Found ID:  63185013722 in object:  <__main__.node object at 0x00000187598909A0>
Found ID:  80796844251 in object:  <__main__.node object at 0x0000018759B28490>
Found ID:  53401758641 in object:  <__main__.node object at 0x0000018759986880>
Found ID:  78170420898 in object:  <__main__.node object at 0x0000018759B451C0>
Found ID:  82900730700 in object:  <__main__.node object at 0x00000187598CA370>
Search time:  86.85902404785156
```

---

## Arrays (Seperate Chaining)

#### Code

```python
import random
import time

tab = [[] for i in range(18000)]


def Add(tab, number):
    sublist_idx = number % 18000
    while True:
        if tab[sublist_idx] is None:
            tab[sublist_idx].append(number)
            break
        if tab[sublist_idx] is not None:
            tab[sublist_idx].append(number)
            break


def Search(tab, number):
    i = 0
    sublist_idx = number % 18000
    while True:
        if len(tab[sublist_idx]) == 0 or i >= len(tab[sublist_idx]):
            break
        if tab[sublist_idx][i] == number:
            print("Found ID: ", number, "on subarray nr. ",
                  sublist_idx, "and index: ", i)
            return (sublist_idx, i)
        if tab[sublist_idx][i] != number and i <= len(tab[sublist_idx]):
            i += 1
            continue


# ADDITION
add_start = time.time()
for _ in range(18000):
    id = random.randint(10000000000, 99999999999)
    Add(tab, id)
add_stop = time.time()
print("Addition time: ", add_stop-add_start)


# SEARCH
search_start = time.time()
for _ in range(20000):
    id = random.randint(10000000000, 99999999999)
    Search(tab, id)
search_stop = time.time()
print("Search time: ", search_stop-search_start)
```

#### Times

```text
Addition time:  0.018949031829833984
Search time:  0.026927709579467773
```


#### Times (increased searched numbers)

```text
Addition time:  0.017923831939697266
Found ID:  33398730536 on subarray nr.  536 and index:  0
Found ID:  37685944599 on subarray nr.  10599 and index:  0
Found ID:  14471882086 on subarray nr.  8086 and index:  0
Found ID:  98826728907 on subarray nr.  14907 and index:  1
Found ID:  14914720694 on subarray nr.  10694 and index:  1
Search time:  26.064285278320312
```

---

## Cuckoo hashing (not sure if it is working correctly)

#### Code

```python
import random
import time


tab = [None]*20000


def hash_first(x):
    global hash_function1
    hash_function1 = x % 20000
    return hash_function1


def hash_second(x):
    global hash_function2
    hash_function2 = x//20000 % 20000
    return hash_function2


def rehash():
    global hash_function1
    hash_function1 = (hash_function1+1123) % 20000
    global hash_function2
    hash_function2 = (hash_function2+143) % 20000


def Lookup(x):
    global idx
    if tab[hash_first(x)] == x:
        idx = hash_first(x)
        return x
    if tab[hash_second(x)] == x:
        idx = hash_second(x)
        return x


def Insert(x):
    if Lookup(x):
        return
    if tab[hash_second(x)] is None:
        tab[hash_second(x)] = x
        return
    hold = x
    index = hash_first(x)
    for _ in range(5):
        if tab[index] is None:
            tab[index] = hold
            return
        tab[index], hold = hold, tab[index]
        if index == hash_first(hold):
            index = hash_second(hold)
        else:
            index = hash_first(hold)


# ADDITION
add_start = time.time()
for _ in range(18000):
    id = random.randint(10000000000, 99999999999)
    Insert(id)
add_stop = time.time()
print("Addition time: ", add_stop-add_start)


# SEARCH
search_start = time.time()
for _ in range(20000):
    id = random.randint(10000000000, 99999999999)
    value = Lookup(id)
    if value == None:
        continue
    else:
        print("Found ID: ", id)
search_stop = time.time()

print("Search time: ", search_stop-search_start)
# print(tab)
```

#### Times

```text
Addition time:  0.04587697982788086
Search time:  0.027924776077270508
```


#### Times (increased searched numbers)

```text
Addition time:  0.04188704490661621
Found ID:  38856253735
Found ID:  35138903427
Found ID:  22009959735
Found ID:  65695043733
Search time:  25.780163288116455
```


### Helpful links when creating a report

[Open Addressing] - https://www.youtube.com/watch?v=Dk57JonwKNk&ab_channel=GeeksforGeeks
[Double Hash] - https://www.youtube.com/watch?v=HcWxaVl1TII&ab_channel=LalithaNatraj
[Separate Chaining] - https://www.youtube.com/watch?v=_xA8UvfOGgU
[Cuckoo Hashing] - http://people.cs.bris.ac.uk/~clifford/coms31900-2020/slides/cuckoo-hashing.pdf
[Cuckoo Hashing] - https://cs.stanford.edu/~rishig/courses/ref/l13a.pdf


Mateusz Suszczyk