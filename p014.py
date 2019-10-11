# Enter your code here. Read input from STDIN. Print output to STDOUT

MAXN = 15 * (10 ** 6)
numberOfElements = [1] * (MAXN + 1)
# allElements = [[1]] * (MAXN + 1)
t = int(input().strip())
for a0 in range(t):
    inputN = int(input().strip())
    indices = [i for i, x in enumerate(numberOfElements) if x == 1][2:inputN]
    for i in indices:
    #     print("i: ", i)
        elements = [i]
        n = i
        length = 1
        while(not n == 1):
            if(not numberOfElements[n] == 1):
#                 print("found: ")
                length = length + numberOfElements[n] - 1
#                 elements = elements + allElements[n][1:]
#                 print("N: ", n)
                break
            elif(n%2 == 1):
                n = int(3*n + 1)
            else:
                n = int(n/2)
#             print("n: ", n)
            elements.append(n)
            length = length + 1
        for element in elements:
            if(numberOfElements[element] == 1):
                numberOfElements[element] = length - elements.index(element)
#         print(elements)
#         print("length: ", length)
#         allElements[i] = elements
        numberOfElements[i] = length
        indices = [i for i, x in enumerate(numberOfElements) if x == 1][2:n]
    # print(allElements)
    # print(numberOfElements)
    print(numberOfElements.index(max(numberOfElements[0:inputN])))
