N, M = map(int, input().split())
list1 = [list(map(int, input().split())) for i in range(N)]
list2 = [list(map(int, input().split())) for i in range(N)]

for i in range(N):
    row = []
    for j in range(M):
        if list1[i][j] == list2[i][j]:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()
   