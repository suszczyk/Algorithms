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