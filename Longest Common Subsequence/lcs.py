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
