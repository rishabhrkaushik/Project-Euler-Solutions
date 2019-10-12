# Enter your code here. Read input from STDIN. Print output to STDOUT

MAXN = 5 * (10 ** 6)
numberOfElements = [1] * (MAXN + 1)
t = int(input().strip())
for a0 in range(t):
    inputN = int(input().strip())
    indices = [i for i, x in enumerate(numberOfElements[0:inputN+1]) if x == 1][2:]
    for i in indices:
        elements = [i]
        n = i
        length = 1
        while(not n == 1):
            if(n < MAXN):
                if(not numberOfElements[n] == 1):
                    length = length + numberOfElements[n] - 1
                    break
                elif(n%2 == 1):
                    n = int(3*n + 1)
                else:
                    n = int(n/2)
            else:
                if(n%2 == 1):
                    n = int(3*n + 1)
                else:
                    n = int(n/2)
            elements.append(n)
            length = length + 1
        for element in elements:
            if(element < MAXN):
                if(numberOfElements[element] == 1):
                    numberOfElements[element] = length - elements.index(element)
#         numberOfElements[i] = length
        indices = [i for i, x in enumerate(numberOfElements[0:inputN]) if x == 1][2:]
#     print(numberOfElements[0:inputN+1])
    m = max(numberOfElements[0:inputN+1])
    maxIndices = [i for i, x in enumerate(numberOfElements[0:inputN + 1]) if x == m]
    print(max(maxIndices))
