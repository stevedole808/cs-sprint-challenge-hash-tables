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
    cache = {}
    for i in tickets:
        cache[i.source] = i.destination
    
    route = []
    last = 'NONE'
    for i in range(0, length):
        route.append(cache[last])
        last = cache[last]
    return route
