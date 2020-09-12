#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

# Create a cache
cache = {}

def reconstruct_trip(tickets, length):
    """
    Reconstructs trips from tickets
    """
    # Your code here
    # Create an empty list for saving airports
    route = []

   # Hash each ticket so the source are keys and the destination are values
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    # The first flight is the one where source=None
    route.append(cache['NONE'])

    # Add in routes for each flight
    for idx in range(length):
        # Take the flight from the cache
        if route[idx] in cache:
            # If statement to check if it is the first flight. If yes, move on
            if cache[route[idx]] == route[0]:
                continue
            # Add the next destination
            route.append(cache[route[idx]])

    return route

    # Tickets
    tickets = [
        Ticket("PIT", "ORD" ),
        Ticket("XNA", "CID" ),
        Ticket("SFO", "BHM" ),
        Ticket("FLG", "XNA" ),
        Ticket("NONE", "LAX"),
        Ticket("LAX", "SFO" ),
        Ticket("CID", "SLC" ),
        Ticket("ORD", "NONE"),
        Ticket("SLC", "PIT" ),
        Ticket("BHM", "FLG" )
    ]

    reconstruct_trip(tickets, 10)