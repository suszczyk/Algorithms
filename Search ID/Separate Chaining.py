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