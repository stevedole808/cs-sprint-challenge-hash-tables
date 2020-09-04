def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    # for loop to iterate over all values in the arrays
    for i in arrays:
    # for loop to grab all the values from the i list 
        for j in i:
            # adding all the values to the dict
            if j in cache:
                cache[j] += 1
            else:
                cache[j] = 1

    # for loop to add the same numbers in each array to the result
    for key in cache.keys():
        if cache[key] == len(arrays):
            result.append(key)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10, 20)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
