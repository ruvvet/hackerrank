def compareTriplets(a, b):

    alice = 0
    bob = 0

    for x in range(3):
        if a[x] > b[x]:
            alice += 1
        elif b[x] > a[x]:
            bob += 1

    return alice, bob


compareTriplets([5, 6, 7], [3, 6, 10])
