class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0

        stop_to_route=defaultdict(list)
        for index,route in enumerate(routes):
            for stop in route:
                stop_to_route[stop].append(index)
        
        queue=deque()
        visited_routes=set()
        visited_stops=set([source])

        for route_index in stop_to_route[source]:
            queue.append([route_index,1])
            visited_routes.add(route_index)
        
        while queue:
            route_index,buses_taken=queue.popleft()
            for stop in routes[route_index]:
                if stop==target:
                    return buses_taken
                if stop not in visited_stops:
                    visited_stops.add(stop)

                    for next_route_index in stop_to_route[stop]:
                        if next_route_index not in visited_routes:
                            visited_routes.add(next_route_index)
                            queue.append((next_route_index,buses_taken+1))
        
        return -1


        