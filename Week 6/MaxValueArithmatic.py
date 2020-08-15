import math

def Evalt(a, b, sym):
    if sym == '+':
        return a + b
    elif sym == '-':
        return a - b
    else:
        return a * b


def MaxVal(M, m, x, y, sym):
    minValue = math.inf
    maxValue = -math.inf

    for i in range(x, y):
        a = Evalt(M[x][i], M[i+1][y], sym[i])
        b = Evalt(M[x][i], m[i+1][y], sym[i])
        c = Evalt(m[x][i], M[i+1][y], sym[i])
        d = Evalt(m[x][i], m[i+1][y], sym[i])
        minValue = min(minValue, a, b, c, d)
        maxValue = max(maxValue, a, b, c, d)

    return minValue, maxValue


def MaxValue(numbers, symbols):

    n = len(numbers)

    min = [[None for x in range(n)] for x in range(n)]
    max = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        min[i][i] = numbers[i]
        max[i][i] = numbers[i]

    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            min[i][j], max[i][j] = MaxVal(max, min, i, j, symbols)

    return max[0][n-1]


if __name__ == "__main__":
    expression = input()
    symbols, numbers = [], []

    for i in expression:
        if i in ['+', '-', '*']:
            symbols.append(i)
        else:
            numbers.append(int(i))

    print(MaxValue(numbers, symbols))