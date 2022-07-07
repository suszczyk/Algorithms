import random
import time
tab=[]

for n in range (4096):
    tab.append(random.randrange(1,4096))


start=time.time()
def InsertSortStep(tab,step):
    for i in range(1, len(tab)):
        a=tab[i]
        k=i-step
        while(a<tab[k] and k>=0):
            tab[k+step]=tab[k]
            k=k-step
        tab[k+step]=a
    return tab

InsertSortStep(tab,1)
stop=time.time()
print('Sorting time: ', stop-start)
#print(tab)