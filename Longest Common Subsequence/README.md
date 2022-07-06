# Longest Common Subsequence

## Exercise

`Write a function that takes two lists filled with integers, and returns the LENGTH of the LONGEST common subsequence.`

To solve this problem I used the `NumPy` library, which handles arrays efficiently. My implementation works for both numbers and letters.

## Code

```python
import numpy as np


def lcs_matrix(x, y):
    matrix = np.zeros((len(x)+1, len(y)+1))
    for i in range(len(x)):
        for j in range(len(y)):
            #print("Current pair: ", x[i], ",", y[j])
            #print("Indexes: ", i+1, j+1)
            if x[i] == y[j]:
                matrix[i+1, j+1] = matrix[i, j]+1
            else:
                matrix[i+1, j+1] = max(matrix[i, j+1], matrix[i+1, j])

    return matrix


####

def backtrack_matrix(x, y, matrix):
    nwp = ''
    idx = (len(x), len(y))
    #print("IDX:", idx)
    while matrix[idx[0], idx[1]] != 0:

        if matrix[idx[0]-1, idx[1]] == matrix[idx[0], idx[1]-1] != matrix[idx[0], idx[1]]:
            idx = idx[0]-1, idx[1]-1
            #print("Current index: ", idx)
            nwp = str(x[idx[0]])+nwp

        elif matrix[idx[0], idx[1]-1] <= matrix[idx[0]-1, idx[1]]:
            idx = idx[0]-1, idx[1]
            #print("Current index: ", idx)

        else:
            idx = idx[0], idx[1]-1
            #print("Current index: ", idx)
            # print(idx)
    return nwp


def main():
    # x = [1, 2, 4]
    # y = [2, 3, 4]

    # x=['a','c','b','c','f']
    # y=['a','b','c','d','a','f']

    # x=[3,1,2,5,0,7,4,3,5,7,7,2]
    # y=[2,0,5,3,1,3,5,4,1,7,2,5]

    # x=['d','y','n','a','m','i','c','p','r','o','g','r','a','m','m','i','n','g']
    # y=['c','o','m','m','o','n','s','u','b','s','e','q','u','e','n','c','e']

    # x=['a','d','e']
    # y=['q','e','a']

    x=['a','g','g','t','a','b']
    y=['g','x','t','x','a','y','b']

    # x=['s','t','o','n','e']
    # y=['l','o','n','g','e','s','t']

    # x = [6, 4, 2, 7, 3, 1, 8, 9, 2, 1, 4, 5]
    # y = [1, 2, 3, 9, 8, 7, 3, 6, 6, 2, 1, 6]
    print("First tab: ", x)
    print("Second tab: ", y)

    matrix = lcs_matrix(x, y)
    print(matrix)
    print("Length of longest common subsequence is : ",
          int(matrix[len(x), len(y)]))

    result = backtrack_matrix(x, y, matrix)
    print("Longest Common Subsequence: ")
    for el in result:
        print(el, end=" ")


if __name__ == "__main__":
    main()

```


## Explanation


### First function

Creates an array in which consecutive numbers are entered. If the consecutive elements from the arrays are equal, then it writes matrix[i+1, j+1] into the matrix[i, j] + 1 field. Otherwise, it writes the maximum from matrix[i, j+1] and matrix[i+1, j]. Returns the resulting matrix.

```python
def lcs_matrix(x, y):
    matrix = np.zeros((len(x)+1, len(y)+1))
    for i in range(len(x)):
        for j in range(len(y)):
            #print("Current pair: ", x[i], ",", y[j])
            #print("Indexes: ", i+1, j+1)
            if x[i] == y[j]:
                matrix[i+1, j+1] = matrix[i, j]+1
            else:
                matrix[i+1, j+1] = max(matrix[i, j+1], matrix[i+1, j])

    return matrix
```

### Second function

```python
def backtrack_matrix(x, y, matrix):
    nwp = ''
    idx = (len(x), len(y))
    #print("IDX:", idx)
    while matrix[idx[0], idx[1]] != 0:

        if matrix[idx[0]-1, idx[1]] == matrix[idx[0], idx[1]-1] != matrix[idx[0], idx[1]]:
            idx = idx[0]-1, idx[1]-1
            #print("Current index: ", idx)
            nwp = str(x[idx[0]])+nwp

        elif matrix[idx[0], idx[1]-1] <= matrix[idx[0]-1, idx[1]]:
            idx = idx[0]-1, idx[1]
            #print("Current index: ", idx)

        else:
            idx = idx[0], idx[1]-1
            #print("Current index: ", idx)
            # print(idx)
    return nwp
```

Processes the resulting matrix. The value in the last column and the last row is the length of the longest common subsequence. Therefore, from this point, start the return up to 0.

Below I will describe the operation of the code for different cases. But only for the first round of the loop. I have commented out the prints in the code, but while writing they helped me understand the ideas of the algorithm.

The first condition checks these three numbers. If two numbers (marked with red and blue) are equal, and the number under them (green) is different from them, it means that under these indexes for the green value is our search.

Then the changed position of the marker by one to the left and one up is saved. In this case to the cell with the color orange.

![](Screenshots/Pasted%20image%2020220521231555.png)

The second condition occurs when the number marked in red is less than or equal to the number marked in blue. Then there is a "transition" about a line higher.


In the last case, there is simply a move one column to the left.


## Testy

During my tests, I used the website https://www.mimuw.edu.pl/~erykk/algovis/lcs.html

#### 1.
```text
    x = [1, 2, 4]
    y = [2, 3, 4]
```

```python
First tab:  [1, 2, 4]
Second tab:  [2, 3, 4]
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 1. 1. 1.]
 [0. 1. 1. 2.]]
Length of longest common subsequence is:  2
Longest Common Subsequence: 
2 4
```


![](Screenshots/Pasted%20image%2020220521232129.png)

<div style="page-break-after: always;"></div>

#### 2.
```text
    x=['a','c','b','c','f']
    y=['a','b','c','d','a','f']
```


```python
First tab:  ['a', 'c', 'b', 'c', 'f']
Second tab:  ['a', 'b', 'c', 'd', 'a', 'f']
[[0. 0. 0. 0. 0. 0. 0.]
 [0. 1. 1. 1. 1. 1. 1.]
 [0. 1. 1. 2. 2. 2. 2.]
 [0. 1. 2. 2. 2. 2. 2.]
 [0. 1. 2. 3. 3. 3. 3.]
 [0. 1. 2. 3. 3. 3. 4.]]
Length of longest common subsequence is:  4
Longest Common Subsequence:
a b c f
```




![](Screenshots/Pasted%20image%2020220521232340.png)

<div style="page-break-after: always;"></div>

#### 3.

```text
    x=[3,1,2,5,0,7,4,3,5,7,7,2]
    y=[2,0,5,3,1,3,5,4,1,7,2,5]
```

```python
First tab:  [3, 1, 2, 5, 0, 7, 4, 3, 5, 7, 7, 2]
Second tab:  [2, 0, 5, 3, 1, 3, 5, 4, 1, 7, 2, 5]
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [0. 0. 0. 0. 1. 2. 2. 2. 2. 2. 2. 2. 2.]
 [0. 1. 1. 1. 1. 2. 2. 2. 2. 2. 2. 3. 3.]
 [0. 1. 1. 2. 2. 2. 2. 3. 3. 3. 3. 3. 4.]
 [0. 1. 2. 2. 2. 2. 2. 3. 3. 3. 3. 3. 4.]
 [0. 1. 2. 2. 2. 2. 2. 3. 3. 3. 4. 4. 4.]
 [0. 1. 2. 2. 2. 2. 2. 3. 4. 4. 4. 4. 4.]
 [0. 1. 2. 2. 3. 3. 3. 3. 4. 4. 4. 4. 4.]
 [0. 1. 2. 3. 3. 3. 3. 4. 4. 4. 4. 4. 5.]
 [0. 1. 2. 3. 3. 3. 3. 4. 4. 4. 5. 5. 5.]
 [0. 1. 2. 3. 3. 3. 3. 4. 4. 4. 5. 5. 5.]
 [0. 1. 2. 3. 3. 3. 3. 4. 4. 4. 5. 6. 6.]]
Length of longest common subsequence is:  6
Longest Common Subsequence:
3 1 5 4 7 2
```


![](Screenshots/Pasted%20image%2020220521232519.png)

<div style="page-break-after: always;"></div>

#### 4.

```text
    x=['d','y','n','a','m','i','c','p','r','o','g','r','a','m','m','i','n','g']
    y=['c','o','m','m','o','n','s','u','b','s','e','q','u','e','n','c','e']
```


```python
First tab:  ['d', 'y', 'n', 'a', 'm', 'i', 'c', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
Second tab:  ['c', 'o', 'm', 'm', 'o', 'n', 's', 'u', 'b', 's', 'e', 'q', 'u', 'e', 'n', 'c', 'e']
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 2. 2.]
 [0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 2. 2.]
 [0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 2. 2.]
 [0. 1. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2.]
 [0. 1. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2.]
 [0. 1. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2.]
 [0. 1. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2.]
 [0. 1. 2. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3.]
 [0. 1. 2. 3. 4. 4. 4. 4. 4. 4. 4. 4. 4. 4. 4. 4. 4. 4.]
 [0. 1. 2. 3. 4. 4. 4. 4. 4. 4. 4. 4. 4. 4. 4. 4. 4. 4.]
 [0. 1. 2. 3. 4. 4. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
 [0. 1. 2. 3. 4. 4. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]]
Length of longest common subsequence is:  5
Longest Common Subsequence:
c o m m n
```

![](Screenshots/Pasted%20image%2020220521233059.png)

<div style="page-break-after: always;"></div>

##### 5.

```text
    x=[6,4,2,7,3,1,8,9,2,1,4,5]
    y=[1,2,3,9,8,7,3,6,6,2,1,6]
```



```python
First tab:  [6, 4, 2, 7, 3, 1, 8, 9, 2, 1, 4, 5]
Second tab:  [1, 2, 3, 9, 8, 7, 3, 6, 6, 2, 1, 6]
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1.]
 [0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1.]
 [0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 2. 2. 2.]
 [0. 0. 1. 1. 1. 1. 2. 2. 2. 2. 2. 2. 2.]
 [0. 0. 1. 2. 2. 2. 2. 3. 3. 3. 3. 3. 3.]
 [0. 1. 1. 2. 2. 2. 2. 3. 3. 3. 3. 4. 4.]
 [0. 1. 1. 2. 2. 3. 3. 3. 3. 3. 3. 4. 4.]
 [0. 1. 1. 2. 3. 3. 3. 3. 3. 3. 3. 4. 4.]
 [0. 1. 2. 2. 3. 3. 3. 3. 3. 3. 4. 4. 4.]
 [0. 1. 2. 2. 3. 3. 3. 3. 3. 3. 4. 5. 5.]
 [0. 1. 2. 2. 3. 3. 3. 3. 3. 3. 4. 5. 5.]
 [0. 1. 2. 2. 3. 3. 3. 3. 3. 3. 4. 5. 5.]]
Length of longest common subsequence is:  5
Longest Common Subsequence:
2 7 3 2 1
```

![](Screenshots/Pasted%20image%2020220521233623.png)


Mateusz Suszczyk