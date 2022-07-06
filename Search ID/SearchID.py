import random

def MSBS(tab):
    T1 = [] #In this array, I will note the largest sum that can be obtained from the initial part of the tab array, up to and including the nth word, with the nth word going into the sum.
              
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
msbs=MSBS(t)
print('Maximum Sum Non Adjacent Elements is:',msbs, "= ", end="")
print(*(el for el in diff), sep=' + ', end='')
print("\n")