
from typing import List
import heapq


class ShortestPath:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.edges = []
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, src: int, dest: int, weight: int):
        # Directed edge
        self.edges.append((src, dest, weight))
        self.graph[src].append((dest, weight))

    # Dijkstra's Algorithm
    def dijkstra(self, src: int) -> List[int]:
        if not 0 <= src < self.vertices:
            raise ValueError("Invalid source vertex")

        if any(weight < 0 for _, _, weight in self.edges):
            raise ValueError(
                "Dijkstra's algorithm does not support negative weights"
            )

        dist = [float("inf")] * self.vertices
        dist[src] = 0

        min_heap = [(0, src)]

        while min_heap:
            current_dist, u = heapq.heappop(min_heap)

            if current_dist > dist[u]:
                continue

            for v, weight in self.graph[u]:
                new_dist = current_dist + weight

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(min_heap, (new_dist, v))

        return dist

    # Bellman-Ford Algorithm
    def bellman_ford(self, src: int) -> List[int]:
        if not 0 <= src < self.vertices:
            raise ValueError("Invalid source vertex")

        dist = [float("inf")] * self.vertices
        dist[src] = 0

        # Relax all edges V - 1 times
        for _ in range(self.vertices - 1):
            updated = False

            for u, v, weight in self.edges:
                if dist[u] != float("inf"):
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        updated = True

            if not updated:
                break

        # Detect reachable negative-weight cycles
        for u, v, weight in self.edges:
            if dist[u] != float("inf"):
                if dist[u] + weight < dist[v]:
                    raise ValueError(
                        "Graph contains a reachable negative-weight cycle"
                    )

        return dist


# Main program
if __name__ == "__main__":
    g = ShortestPath(5)

    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(2, 1, 2)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 3, 5)
    g.add_edge(3, 4, 3)

    source = 0

    print("Dijkstra's shortest distances:")
    print(g.dijkstra(source))

    print("\nBellman-Ford shortest distances:")
    try:
        print(g.bellman_ford(source))
    except ValueError as e:
        print("Error:", e)
