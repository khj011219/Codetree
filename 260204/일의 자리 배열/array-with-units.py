list = list(map(int, input().split()))
while len(list) < 10:
    a = len(list)
    b = list[a-1] + list[a-2]
    list.append(b%10)

for i in list:
    print(i, end=" ")