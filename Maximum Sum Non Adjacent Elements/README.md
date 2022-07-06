# Maximum Sum Non Adjacent Elements




## Code
 
```python
import random


def MSNAE(tab):
    T1 = [] 
              
    T2 = []   
              
    T1.append(tab[0])
    T2.append(0)
    for i in range(1,len(tab)):
        T1.append(T2[i-1]+tab[i])
        T2.append(max(T1[i-1],T2[i-1]))
        
    # For a better understanding, I wrote out for myself T1 i T2
    #print("T1: ",T1) 
    #print("T2: ",T2)
    #print("====")
    i=len(tab)-1
    r=0
    while i>=0:
        if T1[i]>T2[i] and T1[i-1]>T2[i-1] and i!=0:
            r=T1[i]-T2[i]+(T1[i-1]-T2[i-1])
            diff.append(r)
            i=i-2
        elif T1[i]>T2[i]:
            r=T1[i]-T2[i]
            i=i-1
            diff.append(r)
        else:
            i=i-1
    return max(T1[-1],T2[-1])
    
diff,t=[],[]
for i in range(5):
    t.append(random.randint(1,9))
    
print("Randomized array is: ",t)
msnae=msnae(t)
print('Maximum Sum Non Adjacent Elements is:',msnae, "= ", end="")
print(*(el for el in diff), sep=' + ', end='')
print("\n")
```

In array `T1` and `T2`, I will note the largest sum that can be obtained from the initial part of the tab array, up to and including the nth word, with the nth word going into the sum.


The variable `r` is calculated using data from the `T1` and `T2` arrays. It starts from the end and if `T1[i]>T2[i]` then `r` is determined by the formula `r=T1[i]-T2[i]`. In addition, if the penultimate element from the arrays also satisfies the equation that `T1[i-1]>T2[i-1]` then `r` is determined by the formula `r=(T1[i]-T2[i])+(T1[i-1]-T2[i-1])`.
Example of how the code works:

```text
The randomized array is:  [3, 7, 5, 1, 6]
T1:  [3, 7, 8, 8, 14]
T2: [0, 3, 7, 8, 8]
====
Maximum Sum Non Adjacent Elements is: 14 = 6 + 5 + 3
```




---
### Additionally

I tested the code's performance for more and larger numbers.

```python
for a in range(1000): # This loop, of course, is not necessary, but I checked more cases with it.
    diff,t=[],[]
    for i in range(20):
        t.append(random.randint(1,99))

    print("Randomized array is: ",t)

    msnae=msnae(t)

    print('msnae to:',msnae, "= ", end="")
    print(*(el for el in diff), sep=' + ', end='')
    print("\n")
    suma=sum(diff)
    if suma!=msnae:
        print("Error")
        exit()
```

If the code had been invalid, the program would have stopped because the condition that the sum of the individual elements of `MSNAE` was different from `MSNAE` itself.


Here are some function calls.

![](Screenshots/Pasted%20image%2020220427214104.png)



---

The program is working properly with large numbers.

![](Screenshots/Pasted%20image%2020220427202707.png)


I checked in Excel, after adding these example numbers the total is `301118`.

![](Screenshots/Pasted%20image%2020220427202903.png)


Mateusz Suszczyk