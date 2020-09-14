#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    route = []

    for t in tickets:
        # map each ticket source to dict keys, destination to dict values
        if t.source not in d.keys():
            d[t.source] = t.destination

    # add first destination which always has source "NONE"
    route.append(d["NONE"])

    for i in range(1, length):
        # each destination has the previous destination as its source
        route.append(d[route[i-1]])

    return route
