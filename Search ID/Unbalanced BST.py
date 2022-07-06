import random
import time


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


t = tree()

# ADDITION
add_start = time.time()
for _ in range(18000):
    id = random.randint(10000000000, 99999999999)
    t.Add(id)
add_stop = time.time()
print("Addition time: ", add_stop-add_start)

# SEARCH
search_start = time.time()
for _ in range(20000):
    id = random.randint(10000000000, 99999999999)
    n = t.Find(int(id))
    if n == None:
        continue
    else:
        print("Found ID: ", id, "in object: ", n)
search_stop = time.time()

print("Search time: ", search_stop-search_start)