N = int(input())
arr = [[0 for i in range(N)] for i in range(N)]

for i in range(N):
    if i % 2 == 0:
        cnt = 1
        for j in range(N):
            arr[j][i] = cnt
            cnt += 1
    else:
        cnt = N
        for j in range(N):
            arr[j][i] = cnt
            cnt -= 1

for i in range(N):
    for j in range(N):
        print(arr[i][j], end="")
    print()