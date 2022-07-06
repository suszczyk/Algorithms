import itertools
import os
import sys
import string
import math
letters = string.ascii_lowercase+'ąćęłńóśźż'  # 35 letter + optional space


def brute(items, n):
    items = list(items)
    for k in range(n, n+1):
        for t in itertools.product(items, repeat=k):
            yield t


def generate_ngram(n):
    all_chars = dict()
    for res in brute(letters, n):
        res = "".join(res)
        all_chars[res] = 0
    return all_chars


def pull_ngrams(text, k):
    res = [text[i: j] for i in range(len(text)) for j in range(i + 1, len(text) + 1) if len(text[i:j]) == k]
    return res


def count_frequency(n):
    global total
    all_chars = generate_ngram(n)

    file = open(os.path.join(sys.path[0], "pan-tadeusz.txt"), "r", encoding="utf-8")
    for line in file:
        line = line.lower()
        strings = pull_ngrams(line, n)
        for char in strings:
            if char not in all_chars:
                char = ' '
                all_chars[char] = 1
            else:
                all_chars[char] = all_chars[char]+1
    file.close()

    all_chars.pop(" ", None)
    all_chars.pop("  ", None)
    all_chars.pop("   ", None)
    all_chars = {key: val for key, val in all_chars.items() if val != 0}

    
    total = sum(all_chars.values())

    for letter, number in all_chars.items():
        freq = number/total
        all_chars[letter] = freq
    return all_chars


def count_entropy(all_chars):
    entropy = 0
    for _, number in all_chars.items():
        entropy = entropy+number*(math.log2(float(number)))
    entropy = -entropy
    return entropy


def print_top25(all_chars):
    print("Number of elements in the dictionary: ", len(all_chars))
    print("Top 25 values")
    top_25 = sorted(all_chars.items(), key=lambda k: k[1], reverse=True)[:25]
    print("Letter   Number of occurrences     Percentage of text")
    for char, number in top_25:
        print("{}{}{}{}{}{:.4%}".format('   ', char, '\t\t', round(number*total), '\t\t', number))


def main():
    all_chars1, all_chars2, all_chars3 = [count_frequency(n) for n in range(1, 4)]
    entropy1, entropy2, entropy3 = [count_entropy(all_chars) for all_chars in (all_chars1, all_chars2, all_chars3)]
    print("Number of elements in the dictionary: ", len(all_chars1))
    print("Letter   Number of occurrences     Percentage of text")
    a1_sorted_keys = sorted(all_chars1, key=all_chars1.get, reverse=True)
    for r in a1_sorted_keys:
        print("{}{}{}{}{}{:.4%}".format('   ', r, '\t\t', round(all_chars1[r]*total), '\t\t', all_chars1[r]))

    print("\n")
    print_top25(all_chars2)
    print("\n")
    print_top25(all_chars3)
    print("\n")
    print("Comparison of individual entropies")
    print("Entropy (1-gram): ", entropy1)
    print("Entropy (2-gram): ", entropy2/2)
    print("Entropy (3-gram): ", entropy3/3)
    print("\n")
    print("H(L) is approximately: ", entropy1)
    print("1/2 * H(L^2) is approximately: ", entropy2/2,"and that equals: ", (entropy2/2)/entropy1, "* H(L)")
    print("1/3 * H(L^3) is approximately: ", entropy3/3,"and that equals: ", (entropy3/3)/entropy1, "* H(L)")


if __name__ == "__main__":
    main()