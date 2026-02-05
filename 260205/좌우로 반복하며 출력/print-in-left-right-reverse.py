N = int(input())
row = []
for i in range(1, N+1):
    row.append(i)

for i in range(N):
    for j in range(N):
        print(row[j], end="")
    row.reverse()
    print()