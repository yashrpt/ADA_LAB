
from dataclasses import dataclass
from typing import List
import heapq


# Edge class
@dataclass
class Edge:
    src: int
    dest: int
    weight: int


# Graph class
class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.edges: List[Edge] = []

    def add_edge(self, src: int, dest: int, weight: int):
        self.edges.append(Edge(src, dest, weight))

    # Find operation for Disjoint Set
    def find(self, parent, vertex):
        if parent[vertex] != vertex:
            parent[vertex] = self.find(parent, parent[vertex])
        return parent[vertex]

    # Union operation for Disjoint Set
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if root_x == root_y:
            return False

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

        return True

    # Kruskal's Minimum Spanning Tree
    def kruskal_mst(self) -> List[Edge]:
        result = []
        parent = list(range(self.vertices))
        rank = [0] * self.vertices

        sorted_edges = sorted(
            self.edges, key=lambda edge: edge.weight
        )

        for edge in sorted_edges:
            if self.union(
                parent, rank, edge.src, edge.dest
            ):
                result.append(edge)

            if len(result) == self.vertices - 1:
                break

        return result

    # Prim's Minimum Spanning Tree
    def prim_mst(self) -> List[Edge]:
        if self.vertices == 0:
            return []

        adjacency = [[] for _ in range(self.vertices)]

        for edge in self.edges:
            adjacency[edge.src].append(
                (edge.weight, edge.dest)
            )
            adjacency[edge.dest].append(
                (edge.weight, edge.src)
            )

        visited = [False] * self.vertices
        result = []
        min_heap = [(0, 0, -1)]

        while min_heap and len(result) < self.vertices - 1:
            weight, vertex, parent = heapq.heappop(min_heap)

            if visited[vertex]:
                continue

            visited[vertex] = True

            if parent != -1:
                result.append(Edge(parent, vertex, weight))

            for next_weight, neighbor in adjacency[vertex]:
                if not visited[neighbor]:
                    heapq.heappush(
                        min_heap,
                        (next_weight, neighbor, vertex)
                    )

        return result


# Main program
if __name__ == "__main__":
    g = Graph(5)

    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    # Kruskal's Algorithm
    print("Kruskal's MST:")
    kruskal_edges = g.kruskal_mst()
    for edge in kruskal_edges:
        print(f"{edge.src} - {edge.dest} : {edge.weight}")

    print("Total weight:",
          sum(edge.weight for edge in kruskal_edges))

    # Prim's Algorithm
    print("\nPrim's MST:")
    prim_edges = g.prim_mst()
    for edge in prim_edges:
        print(f"{edge.src} - {edge.dest} : {edge.weight}")

    print("Total weight:",
          sum(edge.weight for edge in prim_edges))
