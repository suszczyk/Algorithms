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
