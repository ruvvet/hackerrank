def countingValleys(steps, path):
    valley = 0
    level = 0

    for x in path:
        if x == 'D':
            level -= 1
        else:
            if level == -1:
                valley += 1
            level += 1
    return valley


countingValleys(8, ['D', 'D', 'U', 'U', 'U', 'U', 'D', 'D'])
