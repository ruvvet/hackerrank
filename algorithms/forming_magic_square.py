def formingMagicSquare(s):
    magic_constant = int((3*((3**2)+1))/2)

    cost = 0

    for x in s:
        if sum(x) != magic_constant:
            cost += abs(sum(x)-magic_constant)

    print(cost)


formingMagicSquare([[5, 3, 4], [1, 5, 8], [6, 4, 2]])
