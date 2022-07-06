# Longest Common Subsequence

## Exercise

`Find some book in English in a text file on the Internet. Extract individual words from it into a list, peel off the punctuation marks
punctuation marks, flip to lower case. Sort with RadixSort - produce next text files from next sorting steps. Dump the list into a text file after each Countingsort function. Please note that sorting should be lexicographic.`



## Basic Raddix Sort

Initial Raddix Sort code from classes working on numbers.

```python
import random
import math


def CountingSort(tab, poz):
    counters = [0]*10
    for i in range(len(tab)):
        counters[GetDigit(tab[i], poz)] += 1
    for i in range(1, len(counters)):
        counters[i] += counters[i-1]
    posort = [0]*len(tab)
    for j in range(len(tab)-1, -1, -1):
        counters[GetDigit(tab[j], poz)] -= 1
        posort[counters[GetDigit(tab[j], poz)]] = tab[j]
    for i in range(len(tab)):
        tab[i] = posort[i]


def GetDigit(number, digit):
    return int((number/(10**digit)) % 10)


"""def GetDigit2(number,digit):
        number=str(number)
        if digit<len(number):
                return int(number[-1-digit])
        else:
                return 0"""


def RadixSort(tab):
    m = tab[0]
    for i in range(1, len(tab)):
        if tab[i] > m:
            m = tab[i]
    c = int(math.log(m, 10))+1
    for dig in range(c):
        CountingSort(tab, dig)


tab = []
for i in range(100):
    tab.append(random.randrange(0, 1000))
RadixSort(tab)
print(tab)

```

Example result of an running code:

```text
[3, 31, 43, 51, 64, 70, 72, 81, 81, 86, 88, 88, 104, 115, 118, 131, 147, 156, 164, 166, 170, 201, 203, 213, 238, 245, 257, 307, 312, 322, 338, 344, 350, 362, 367, 376, 386, 397, 400, 437, 442, 448, 493, 495, 506, 519, 528, 539, 540, 540, 568, 578, 590, 603, 607, 608, 608, 613, 628, 629, 651, 653, 654, 655, 680, 682, 684, 686, 698, 698, 703, 712, 722, 745, 750, 765, 787, 816, 835, 838, 872, 875, 877, 877, 885, 896, 904, 918, 922, 929, 934, 944, 949, 949, 956, 958, 960, 961, 973, 985]
```

## My code modification

```python
import os
import sys
import re

#The first function takes a file and rearranges it to get a convenient list containing all the words in the file.

def open_file(name):
    list = []
    with open(os.path.join(sys.path[0], str(name)), "r+", encoding="utf-8") as f:
        the_list = (word.strip(",") for line in f for word in line.split())
        for word in the_list:
            newstring = re.sub(r"[^A-Za-z]+", "", word)
            newstring = newstring.lower()
            list.append(newstring)

    return list

#The second function saves files. I created it in such a way that it creates names along with a specific counter.

def save_to_file(tab, name, i=None):
    with open(os.path.join(sys.path[0], "{}{}.txt".format(name, "" if i is None else i)), 'w') as f:
        for item in tab:
            f.write("%s\n" % item)

#Below is a modified CoutingSort function.
def CountingSort(tab, poz):
    counters = [0] * (26+1)  # Whole alphabet + spot for spaces
    alpha_start = ord('a') - 1  # Subtract one too allow for dummy character

    for i in range(len(tab)): 
        if poz < len(tab[i]):
            letter = ord(tab[i][poz]) - alpha_start
        else:
            letter = 0
        counters[letter] += 1

    for i in range(1, len(counters)):
        counters[i] += counters[i-1]

    posort = [0] * len(tab)

    for j in range(len(tab)-1, -1, -1):
        if poz < len(tab[j]):
            letter = ord(tab[j][poz]) - alpha_start
        else:
            letter = 0
        counters[letter] -= 1
        posort[counters[letter]] = tab[j]
    return posort

#Function that searches for the longest word in an array

def max_length(tab):
    length = 0
    global longest_word
    for el in tab:
        if len(el) > length:
            length = len(el)
            longest_word = el
    return length



def RadixSort(tab):
    """ Main sorting routine """
    global max_l
    max_l = max_length(tab)
    print("The longest word in the text has:", max_l,"letters.")
    for poz in range(max_l - 1, -1, -1):  # max_len-1, max_len-2, ...0
        tab = CountingSort(tab, poz)
        #print("Tab: ", tab, " position: ", poz)
        save_to_file(tab, "CountingSort", poz)
    return tab

#Main function

def main():
    prepare_list = open_file("test.txt")
    save_to_file(prepare_list, "test-cleared")

    list = open_file("test-cleared.txt")
    #save_to_file(list, "test-cleared")

    #print("Original tab :", list)
    list = RadixSort(list)
    #print(RadixSort(list) == sorted(list))
    save_to_file(list, "final_sorted")

    #Check if my implementation works properly.
    final_sorted = open_file("final_sorted.txt")
    print(final_sorted == sorted(list))


if __name__ == "__main__":
    main()
```


## Tests

For the example text `Lorem Ipsum is simply dummy text of the printing and typesetting industry.` I got the following result:

![](Screenshots/Pasted%20image%2020220517223150.png)

The program also created files of each stage.

![](Screenshots/Pasted%20image%2020220517222058.png)

Now I will proceed to check the whole book. I chosed `Crime and Punishment` by `Rodion Raskolnikov` as the book which is free from `Gutenberg Project`. 
Source: `https://www.gutenberg.org/ebooks/2554`

![](Screenshots/Pasted%20image%2020220517235515.png)

![](Screenshots/Pasted%20image%2020220517235525.png)


The file `final_sorted.txt` contains a list of sorted words.

In addition, I checked that my algorithm actually sorts by `print(final_sorted == sorted(list))`.

![](Screenshots/Pasted%20image%2020220517235808.png)

Random place in `final_sorted.txt` file.

Mateusz Suszczyk