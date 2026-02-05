A, B = map(int, input().split())

while 1:
    if A <= B:
        print(A, end=" ")
    else:
        break

    if A % 2 == 1:
        A *= 2
    else:
        A += 3