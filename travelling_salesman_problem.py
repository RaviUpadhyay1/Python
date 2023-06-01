# import itertools

# def tsp_brute_force(graph, start):
#     # Generate all possible permutations of cities
#     cities = list(graph.keys())
#     permutations = itertools.permutations(cities)

#     # Initialize variables to store the best route and its length
#     best_route = None
#     best_length = float('inf')

#     for permutation in permutations:
#         # Check if the current permutation starts with the given starting city
#         if permutation[0] == start:
#             route_length = 0
#             current_city = start

#             # Calculate the length of the current permutation (route)
#             for next_city in permutation:
#                 route_length += graph[current_city][next_city]
#                 current_city = next_city

#             # Update the best route and its length if the current route is shorter
#             if route_length < best_length:
#                 best_route = permutation
#                 best_length = route_length

#     return best_route, best_length

# def main():
#     # Example graph representing distances between cities
#     graph = {
#         'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
#         'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
#         'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
#         'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
#     }

#     start_city = 'A'

#     best_route, best_length = tsp_brute_force(graph, start_city)

#     print("Best route:", ' -> '.join(best_route))
#     print("Length:", best_length)

# if __name__ == '__main__':
#     main()
import itertools

def tsp(cities):
    # Generate all possible tours
    tours = list(itertools.permutations(cities))

    # Compute the length of each tour
    tour_lengths = [tour_length(tour) for tour in tours]

    # Find the shortest tour
    shortest_tour = tours[tour_lengths.index(min(tour_lengths))]

    return shortest_tour

def tour_length(tour):
    # Compute the total length of a tour
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1)) + distance(tour[-1], tour[0])

def distance(city1, city2):
    # Compute the Euclidean distance between two cities
    return ((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2)**0.5

# Example usage
cities = [(0,0), (1,0), (1,1), (0,1)]
shortest_tour = tsp(cities)
print(shortest_tour)