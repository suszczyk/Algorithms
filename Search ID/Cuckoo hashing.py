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