def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    result = []

    # the final elements must be in ALL subarrays
    # hence we only need to assign elements in the first subarray into dict
    # whichever element in the subsequent subarrays that does not appear in dict will automatically be out of contention

    for el in arrays[0]:
        if el not in d.keys():
            d[el] = 1

    for i in range(1, len(arrays)):
        for el in arrays[i]:
            if el in d.keys():
                d[el] += 1

    for k, v in d.items():
        # if the number has appeared in ALL subararys, it's in the intersection
        if v == len(arrays):
            result.append(k)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
