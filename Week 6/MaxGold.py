import sys


def OptimalWeight(W, w):
    bars = [0]

    for bar in w:
        if W>=bar:
            bars.append(bar)

    noOfBars = len(bars)
    capacity = W + 1

    weights = [[0 for _ in range(noOfBars)] for _ in range(capacity)]

    for i in range(1, noOfBars):
        for j in range(1, capacity):
            prev = weights[j][i - 1]
            curr = bars[i] + weights[j - bars[i]][i - 1]
            if curr > j:
                weights[j][i] = prev
            else:
                weights[j][i] = max(prev, curr)

    return weights[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(OptimalWeight(W, w))
