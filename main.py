def knapsack():
    price = [3, 8, 15]
    weight = [2, 3, 5]
    n = 3
    maxWeight = 9

    f = []
    p = []
    for i in range(n + 1):
        f.append([0] * (maxWeight + 1))
        p.append([0] * (maxWeight + 1))
    for i in range(1, n + 1):
        for w in range(1, maxWeight + 1):
            index = w + 1 - weight[i - 1]
            if index > 0:
                f[i][w] = max(list(map(lambda item: item + price[i - 1], f[i][:index])))
            else:
                f[i][w] = f[i - 1][w]
            if f[i][w] == f[i - 1][w]:
                p[i][w] = 0
            else:
                p[i][w] = 1
    print('\n')
    print("f:")
    for line in f:
        print(line)
    print('\n')
    print("p:")
    for line in p:
        print(line)
    print('\n')
    solution = max([f[i][maxWeight] for i in range(n + 1)])
    index = [element for line in f for element in line].index(solution) // (maxWeight + 1)
    x = [0] * n
    currentWeight = maxWeight
    for i in range(index, 0, -1):
        if p[i][currentWeight] == 0:
            continue
        while p[i][currentWeight] == 1 and currentWeight >= weight[i - 1]:
            x[i - 1] += 1
            currentWeight -= weight[i - 1]
        if currentWeight <= 0:
            break
    return solution, x


def main():
    option, solution = knapsack()
    print(f'Optimal solution: {option}')
    print(f'Solution is reached at values: {solution}')


main()
