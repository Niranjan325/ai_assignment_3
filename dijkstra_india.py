import heapq

graph = {
    "Delhi": {"Jaipur": 280, "Lucknow": 555, "Chandigarh": 250},
    "Jaipur": {"Delhi": 280, "Ahmedabad": 660},
    "Lucknow": {"Delhi": 555, "Patna": 530},
    "Chandigarh": {"Delhi": 250, "Amritsar": 230},
    "Ahmedabad": {"Jaipur": 660, "Mumbai": 530},
    "Mumbai": {"Ahmedabad": 530, "Pune": 150},
    "Pune": {"Mumbai": 150, "Hyderabad": 560},
    "Hyderabad": {"Pune": 560, "Bangalore": 570},
    "Bangalore": {"Hyderabad": 570, "Chennai": 350},
    "Chennai": {"Bangalore": 350},
    "Patna": {"Lucknow": 530},
    "Amritsar": {"Chandigarh": 230}
}

def dijkstra(graph, start):
    distances = {city: float('inf') for city in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_city = heapq.heappop(pq)

        if current_distance > distances[current_city]:
            continue

        for neighbor, weight in graph[current_city].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

start_city = input("Enter source city: ")

if start_city not in graph:
    print("City not found")
else:
    result = dijkstra(graph, start_city)

    print("\nShortest Distances:")
    for city, distance in result.items():
        print(f"{start_city} -> {city} = {distance} km")
