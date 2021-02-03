def matchSocks(n, ar):

    # sort arr into socks by color
    socks = {n: ar.count(n) for n in ar}
    # get number of pairs for each color, sum
    return sum([s//2 for s in socks.values()])


print(matchSocks(7, [1, 2, 1, 2, 1, 3, 2]))
