

def optimal_points(data):
    data.sort(key = lambda i: i[1])
    n = len(data)
    i = 0
    d = list()
    while i < n:
        l,r = data[i][0], data[i][1]
        x = r
        i += 1
        while i < n and data[i][0] <= r:
            if data[i][1] < x:
                x = data[i][1]
            i += 1
        d.append(x)
    return [len(d),d]
    

if __name__ == '__main__':
    data = list()
    for i in range(int(input())):
        data.append(list(map(int,input().split())))
    result = optimal_points(data)
    print(result[0])
    print(" ".join(list(str(i) for i in result[1])))
