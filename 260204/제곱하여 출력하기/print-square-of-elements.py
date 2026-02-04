N = int(input())
list = list(map(int, input().split()))

new_list = [x**2 for x in list]
for i in range(N):
    print(new_list[i], end=" ")