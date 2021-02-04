def jumpingOnClouds(c):
    position = 0
    end = n - 1
    jumps = 0

    while position < end:
        if ((position + 2) <= end) and (c[position + 2] == 0):
            position += 2
            jumps += 1
        elif c[position + 1] == 0:
            position += 1
            jumps += 1
    return jumps


jumpingOnClouds([0, 1, 0, 0, 0, 1, 0])
