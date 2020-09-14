def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    arr = []

    for w in weights:
        # assign weight value as dict keys, weight index as dict values
        if w not in d.keys():
            d[w] = weights.index(w)

    for w in weights:
        result = limit - w
        # if result exists in dict keys, current w and result is the pair we are looking for
        if result in d.keys():
            # add w's index to arr
            arr.append(d[w])

    # if length of array equals 2, there exists a pair that adds up to weight limit
    if len(arr) == 2:
        # if the pair that sums to the limit are duplicates, get the second duplicate's weight index
        if arr[0] == arr[1]:
            arr[1] = weights.index(weights[arr[1]], weights.index(weights[arr[1]])+1)
        
        # return larger index value first
        arr.sort(reverse=True)
        return tuple(arr)

    return None
