def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    result = []

    for el in a:
        # assign all positive integers into dict keys
        if el > 0 and el not in d.keys():
            d[el] = None
    
    for el in a:
        if el < 0:
            # check if the absolute value of the negative integers exists in dict keys
            check = el * -1
            # if exists, the positive integer has a corresponding negative integer, hence is added to result
            if check in d.keys():
                result.append(check)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
