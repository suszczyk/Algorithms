# Entropy of polish language


## Exercise

![](Screenshots/Pasted%20image%2020220525191817.png)


## Code

```python
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
```



## Description of functions

I will briefly describe the operation of each function below.


### brute i generate_ngram

The given functions work together. The function `generate_ngram` takes an argument `n` and returns a dictionary filled in the keys with letters of length `n`. Each key is assigned a value of `0`. Depending on the number given, you will get all possible combinations of letters.

For `n=1`:

```text
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, 'ą': 0, 'ć': 0, 'ę': 0, 'ł': 0, 'ń': 0, 'ó': 0, 'ś': 0, 'ź': 0, 'ż': 0, ' ': 0}
```

For `n=2`:

```text
{'aa': 0, 'ab': 0, 'ac': 0, 'ad': 0, 'ae': 0, 'af': 0, 'ag': 0, 'ah': 0, 'ai': 0, 'aj': 0, 'ak': 0, 'al': 0, 'am': 0, 'an': 0, 'ao': 0, 'ap': 0, 'aq': 0, 'ar': 0, 'as': 0, 'at': 0, 'au': 0, 'av': 0, 'aw': 0, 'ax': 0, 'ay': 0, 'az': 0, 'aą': 0, 'ać': 0, 'aę': 0, 'ał': 0, 'ań': 0, 'aó': 0, 'aś': 0, 'aź': 0, 'aż': 0, 'a ': 0, 'ba': 0, 'bb': 0, 'bc': 0, 'bd': 0,  ... ... ...
```

```python
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
```


### pull_ngrams

The function `pull_ngrams` takes arguments in text and a number, and returns a list filled with letters of length `k`. An example of how the function works.

For `k=1`:

```python
text="Ala ma kota"
x=pull_ngrams(text,1)
print(x)

['A', 'l', 'a', ' ', 'm', 'a', ' ', 'k', 'o', 't', 'a']
```

For `k=2`:

```python
text="Ala ma kota"
x=pull_ngrams(text,2)
print(x)

['Al', 'la', 'a ', ' m', 'ma', 'a ', ' k', 'ko', 'ot', 'ta']
```


```python
def pull_ngrams(text, k):
    res = [text[i: j] for i in range(len(text)) for j in range(i + 1, len(text) + 1) if len(text[i:j]) == k]
    return res
```



### count_frequency

The function takes a numeric argument `n` used to call the above functions. Then a text file is loaded. In this case, the book `Adam Mickiewicz - "Pan Tadeusz"`. Then, in a loop, each line is reduced to lowercase. Using the `pull_ngrams` function, ngrams are extracted. Function `if` checks if a character exists in the `all_chars` dictionary. In this case, the condition checks whether `char` has letters or other characters. If it has other characters, the `char` is converted to a space character. Otherwise, a certain key is incremented by `1`. According to the command, space characters are removed and keys with possible values equal to `0` are removed. The function then sums all the remaining values from the `total` variable. Immediately after that, it counts the frequency of occurrence of the specified character/s and overwrites under the specified keys. It returns this dictionary.

```python
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
```



### count_entropy

The function takes a dictionary from the function above and the entropy is calculated according to the formula. The calculated value of `entropy` is returned.

![](Screenshots/Pasted%20image%2020220526013229.png)


```python
def count_entropy(all_chars):
    entropy = 0
    for _, number in all_chars.items():
        entropy = entropy+number*(math.log2(float(number)))
    entropy = -entropy
    return entropy
```



### print_top25

Here is the first graphical representation of the calculated values. The function successively gives the number of elements from the dictionary and the 25 largest values from the dictionary. Then the letter, the number of occurrences and the percentage of text that the character(s) occupies.

```python
def print_top25(all_chars):
    print("Number of elements in the dictionary:", len(all_chars))
    print("Top 25 values")
    top_25 = sorted(all_chars.items(), key=lambda k: k[1], reverse=True)[:25]
    print("Letter   Number of occurrences     Percentage of text")
    for char, number in top_25:
        print("{}{}{}{}{}{:.4%}".format('   ', char, '\t\t', round(number*total), '\t\t', number))
```


### main

The most important function. For the following variables, three dictionaries are calculated for unigram, bigram and trigram. Then the entropy of `H(L)`, `H(L^2)` and `H(^3)` is calculated. This is followed by the presentation of the calculated data.


```python
def main():
    all_chars1, all_chars2, all_chars3 = [count_frequency(n) for n in range(1, 4)]
    entropy1, entropy2, entropy3 = [count_entropy(all_chars) for all_chars in (all_chars1, all_chars2, all_chars3)]
    print("Number of elements in the dictionary:", len(all_chars1))
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
```


### _name__== "__main__"

Initiating function.

```python
if __name__ == "__main__":
    main()
```



### `Not including spaces`

## The result of the program for n=1

```text
Number of elements in the dictionary: 35
Letter   Number of occurrences     Percentage of text
   a            19923           8.9145%    
   i            18997           8.5003%
   e            15969           7.1452%
   o            14865           6.6516%
   z            14825           6.6335%
   s            10259           4.5903%
   n            10245           4.5840%
   w            9996            4.4726%
   r            9948            4.4514%
   c            9260            4.1436%
   y            8637            3.8645%
   k            8208            3.6725%
   d            7570            3.3873%
   t            7365            3.2957%
   m            6842            3.0613%
   ł            6368            2.8493%
   p            5840            2.6129%
   u            4957            2.2179%
   j            4608            2.0619%
   l            4384            1.9615%
   b            3983            1.7823%
   ę            3492            1.5623%
   g            3237            1.4484%
   ą            3025            1.3537%
   h            2656            1.1883%
   ż            2242            1.0034%
   ó            1962            0.8778%
   ś            1639            0.7334%
   ć            1234            0.5522%
   ń            411             0.1841%
   f            270             0.1210%
   ź            264             0.1182%
   v            4               0.0020%
   x            2               0.0008%
   q            1               0.0006%
```

## The result of the program for n=2

```text
Number of elements in the dictionary: 692
Top 25 values
Letter   Number of occurrences     Percentage of text
   ie           7993            3.5763%
   ni           4619            2.0668%
   rz           3489            1.5613%
   sz           3277            1.4664%
   cz           3107            1.3904%
   zy           2937            1.3144%
   wi           2913            1.3035%
   ch           2893            1.2944%
   na           2864            1.2814%
   ze           2667            1.1935%
   za           2624            1.1742%
   st           2384            1.0667%
   po           2361            1.0565%
   dz           2331            1.0429%
   ał           2269            1.0152%
   ci           2133            0.9542%
   ta           2127            0.9518%
   si           2090            0.9350%
   ra           2057            0.9206%
   zi           2013            0.9006%
   ro           1931            0.8639%
   ię           1913            0.8558%
   em           1910            0.8548%
   ki           1887            0.8442%
   ia           1819            0.8141%
```


## The result of the program for n=3

```text
Number of elements in the dictionary: 5584
Top 25 values
Letter   Number of occurrences     Percentage of text
   nie          3478            1.5562%
   dzi          2220            0.9933%
   rze          1848            0.8269%
   się          1652            0.7392%
   wie          1585            0.7092%
   rzy          1439            0.6439%
   prz          1324            0.5924%
   zie          1130            0.5056%
   czy          1034            0.4627%
   cie          959             0.4291%
   kie          917             0.4103%
   jak          910             0.4072%
   sta          899             0.4023%
   szy          899             0.4023%
   ach          755             0.3378%
   iem          737             0.3298%
   ier          718             0.3213%
   wsz          712             0.3186%
   trz          686             0.3070%
   iał          676             0.3025%
   str          667             0.2985%
   ego          648             0.2899%
   ani          644             0.2882%
   owi          630             0.2819%
   ści          630             0.2819%
```


## Entropy

```text
Entropy comparison
Entropy (1-gram):  4.580162255425056
Entropy (2-gram):  3.978190770295998
Entropy (3-gram):  3.5749975914662238


H(L) is approximately:  4.580162255425056
1/2 * H(L^2) is approximately:  3.978190770295998 and that equals:  0.8685698340891653 * H(L)
1/3 * H(L^3) is approximately:  3.5749975914662238 and that equals:  0.7805395075756876 * H(L)
```



### `Including spaces`

## The result of the program for n=1

```text
Number of elements in the dictionary: 35
Letter   Number of occurrences     Percentage of text
   a            33611           8.9145%
   i            32049           8.5003%
   e            26940           7.1452%
   o            25079           6.6516%
   z            25011           6.6335%
   s            17307           4.5903%
   n            17284           4.5840%
   w            16864           4.4726%
   r            16784           4.4514%
   c            15623           4.1436%
   y            14571           3.8645%
   k            13847           3.6725%
   d            12771           3.3873%
   t            12426           3.2957%
   m            11542           3.0613%
   ł            10743           2.8493%
   p            9852            2.6129%
   u            8363            2.2179%
   j            7774            2.0619%
   l            7396            1.9615%
   b            6720            1.7823%
   ę            5891            1.5623%
   g            5461            1.4484%
   ą            5104            1.3537%
   h            4480            1.1883%
   ż            3783            1.0034%
   ó            3310            0.8778%
   ś            2765            0.7334%
   ć            2082            0.5522%
   ń            694             0.1841%
   f            456             0.1210%
   ź            446             0.1182%
   v            7               0.0020%
   x            3               0.0008%
   q            2               0.0006%
```

## The result of the program for n=2

```text
Number of elements in the dictionary: 754
Top 25 values
Letter   Number of occurrences     Percentage of text
   ie           9753            2.5868%
    s           5919            1.5700%
   a            5646            1.4975%
   ni           5637            1.4950%
    p           5452            1.4461%
    w           5443            1.4435%
   e            5420            1.4375%
    z           4438            1.1770%
   i            4401            1.1673%
   o            4353            1.1544%
   rz           4258            1.1293%
    n           4026            1.0678%
   sz           3999            1.0607%
   cz           3792            1.0057%
   zy           3585            0.9507%
   wi           3555            0.9428%
   y            3536            0.9378%
   ch           3530            0.9363%
   na           3495            0.9269%
   ze           3255            0.8633%
   za           3202            0.8493%
    d           2977            0.7896%
    t           2966            0.7868%
   st           2909            0.7716%
   po           2881            0.7642%
```


## The result of the program for n=3

```text
Number of elements in the dictionary: 7084
Top 25 values
Letter   Number of occurrences     Percentage of text
   nie          3478            0.9225%
   ie           2738            0.7262%
   dzi          2220            0.5888%
    po          2218            0.5883%
    na          2065            0.5477%
    ni          1892            0.5018%
   rze          1848            0.4901%
    si          1756            0.4657%
   na           1724            0.4572%
   się          1652            0.4382%
   wie          1585            0.4204%
    w           1521            0.4034%
    pr          1496            0.3968%
    za          1446            0.3835%
   rzy          1439            0.3817%
    i           1421            0.3769%
   ię           1386            0.3676%
   prz          1324            0.3512%
    z           1246            0.3305%
   ch           1163            0.3085%
   em           1160            0.3077%
    do          1157            0.3069%
   zie          1130            0.2997%
    wi          1099            0.2915%
   ał           1042            0.2764%
```



## Entropy

```text
Entropy comparison
Entropy (1-gram):  4.580162255425056
Entropy (2-gram):  4.026684464929646
Entropy (3-gram):  3.6701855710453373


H(L) is approximately:  4.580162255425056
1/2 * H(L^2) is approximately:  4.026684464929646 and that equals:  0.8791576019299682 * H(L)
1/3 * H(L^3) is approximately:  3.6701855710453373 and that equals:  0.8013221729640952 * H(L)
```


## `Mateusz Suszczyk`