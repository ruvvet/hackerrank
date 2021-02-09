def staircase(n):

    for x in range(1, n+1):
        print(f"{(n-(x+1))*' '}{(x+1)*'#'}")


staircase(4)
