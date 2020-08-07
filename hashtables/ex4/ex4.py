def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    pos = {}
    neg = {}
    # for loop to sort through the values in the array(a)
    for i in a:
        # adding all negative values to the neg dictionary
        if i < 0:
            # multiply the negative values by -1 in order to change it to a positive
            neg[i] = i*-1
        else:
            # all other values that aren't negative will be added to the positive dictionary
            pos[i] = i
    # another for loop to check for corresponding integers in the pos and neg dictionary
    for negatives in neg.values():
        # find corresponding values in the neg and pos dictionary
        if negatives in pos:
            # append the corresponding values to the result list
            result.append(pos[negatives])
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
