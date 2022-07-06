import random
import time
import math


class node(object):
    def __init__(self, number=None):
        self.number = number
        self.left = None
        self.right = None
        self.parent = None


class tree(object):
    def __init__(self):
        self.dummy = node()

    def Add(self, num, nd=None):
        if(nd == None):
            nd = self.dummy.right
        if(nd == None):
            self.dummy.right = node(num)
            self.dummy.right.parent = self.dummy
            return
        if(nd.number > num):
            if(nd.left == None):
                nd.left = node(num)
                nd.left.parent = nd
                return
            else:
                self.Add(num, nd.left)
                return
        elif(nd.number < num):
            if(nd.right == None):
                nd.right = node(num)
                nd.right.parent = nd
                return
            else:
                self.Add(num, nd.right)
                return
        else:
            return

    def Find(self, num, nd="u"):

        if(nd == "u"):
            nd = self.dummy.right

        if(nd == None):

            return None
        if(nd.number == num):
            return nd
        if(nd.number > num):
            return self.Find(num, nd.left)

        else:
            return self.Find(num, nd.right)

    def Rotate(self, B):
        if (B == self.dummy or B == None or B == self.dummy.right):
            return
        A = B.parent
        P = A.parent
        if A.left == B:
            Beta = B.right
            B.parent = P
            if P.left == A:
                P.left = B
            else:
                P.right = B

            A.parent = B
            B.right = A

            A.left = Beta
            if(Beta != None):
                Beta.parent = A
        else:
            Beta = B.left
            B.parent = P
            if P.left == A:
                P.left = B
            else:
                P.right = B

            A.parent = B
            B.left = A

            A.right = Beta
            if(Beta != None):
                Beta.parent = A

    def DSW(self):
        nd = self.dummy.right
        licznik = 0
        while nd != None:
            if nd.left != None:
                self.Rotate(nd.left)
                nd = nd.parent
            else:
                nd = nd.right
                licznik += 1
        m = pow(2, int(math.log(licznik + 1, 2))) - 1
        nd = self.dummy.right
        for _ in range(licznik - m):
            self.Rotate(nd.right)
            nd = nd.parent.right

        while m > 0:
            m = m // 2
            nd = self.dummy.right
            for _ in range(m):
                self.Rotate(nd.right)
                nd = nd.parent.right


t = tree()

#ADDITION
add_start = time.time()
for _ in range(18000):
    id = random.randint(10000000000, 99999999999)
    t.Add(id)
add_stop = time.time()
print("Addition time: ", add_stop-add_start)


t.DSW()

#SEARCH
search_start = time.time()
for _ in range(2000000):
    id = random.randint(10000000000, 99999999999)
    n = t.Find(id)
    if n == None:
        continue
    else:
        print("Found ID: ", id, "in object: ", n)
search_stop = time.time()

print("Search time: ", search_stop-search_start)