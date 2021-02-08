def plusMinus(arr):

    pos = len([x for x in arr if x > 0])/len(arr)
    neg = len([x for x in arr if x < 0])/len(arr)
    zero = 1 - (pos+neg)

    print(f"{pos:.5f} \n {neg:.5f} \n {zero:.5f}")


plusMinus([1, 2, 3, 4, -1, -3, 0, 0, 0, 0])
