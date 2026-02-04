cnt_3 = 0
cnt_5 = 0
for i in range(10):
    N = int(input())
    if N % 3 == 0:
        cnt_3 += 1
    if N % 5 == 0:
        cnt_5 += 1

print(cnt_3, cnt_5)

