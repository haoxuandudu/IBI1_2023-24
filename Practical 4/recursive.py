def a(n):
    if n == 1:
        return 4
    elif n == 2:
        return 11
    elif n == 3:
        return 25
    else:
        return 2 * a(n - 1) + 3
for i in range(1, 6):
    print(f"The {i}th value of the recursive sequence is: {a(i)}")
