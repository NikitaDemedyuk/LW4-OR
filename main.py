price = [1, 3, 4]
weight = [2, 2, 3]
n = 3
maxWeight = 6


def solveTask():
    f = []
    p = []
    for i in range(n + 1):
        f.append([0] * (n + 1))
        p.append([0] * (n + 1))
    for i in range(1, n + 1):
        for w in range(1, n + 1):
            index = w + 1 - weight[i]
            if index > 0:
                f[i][w] = max(list(map(lambda item: item + price[i - 1], f[i][:ind])))
            else:
                f[i][w] = f[i - 1][w]
            if f[i][w] == f[i - 1][w]:
                p[i][w] = 0
            else:
                p[i][w] = 1
    print("f:")
    for line in f:
        print(line)
    print("p:")
    for line in p:
        print(line)
    solution = max([f[i][maxWeight] for i in range(n + 1)])
    index = [element for line in f for element in line].index(solution) // (maxWeight + 1)
    x = [0] * n
    currentIndex = maxWeight
    #for i in range(index, 0, -1):

def main():
    return 0


main()
