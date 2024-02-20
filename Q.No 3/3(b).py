# Class to represent a graph edge
class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    # Compare two edges based on their weight
    def __lt__(self, other):
        return self.weight < other.weight


# Class to represent a subset for union-find
class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


class KruskalAlgorithm:
    def __init__(self, v, e):
        self.V = v  # Number of vertices
        self.E = e  # Number of edges
        self.edges = []

    # Function to find the set of an element 'i'
    def find(self, subsets, i):
        if subsets[i].parent != i:
            subsets[i].parent = self.find(subsets, subsets[i].parent)
        return subsets[i].parent

    # Function that does union of two sets of x and y
    def union(self, subsets, x, y):
        xroot = self.find(subsets, x)
        yroot = self.find(subsets, y)

        # Attach smaller rank tree under root of high rank tree
        if subsets[xroot].rank < subsets[yroot].rank:
            subsets[xroot].parent = yroot
        elif subsets[xroot].rank > subsets[yroot].rank:
            subsets[yroot].parent = xroot
        else:
            # If ranks are the same, then make one as root and increment its rank by one
            subsets[yroot].parent = xroot
            subsets[xroot].rank += 1

    # Function to construct MST using Kruskal's algorithm
    def kruskal_mst(self):
        result = []  # This will store the resultant MST
        e = 0  # An index variable, used for result[]
        i = 0  # An index variable, used for sorted edges

        # Step 1: Sort all the edges in non-decreasing order of their weight
        self.edges.sort()

        subsets = [Subset(i, 0) for i in range(self.V)]

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
            # Step 2: Pick the smallest edge. Increment the index for the next iteration
            next_edge = self.edges[i]
            i += 1

            x = self.find(subsets, next_edge.src)
            y = self.find(subsets, next_edge.dest)

            # If including this edge doesn't cause a cycle, include it in the result and increment the index
            # of result for the next edge
            if x != y:
                result.append(next_edge)
                e += 1
                self.union(subsets, x, y)

        # Print the edges of MST
        print("Following are the edges in the constructed MST:")
        minimum_cost = 0
        for edge in result:
            print(f"{edge.src} -- {edge.dest} == {edge.weight}")
            minimum_cost += edge.weight
        print(f"Minimum Cost Spanning Tree: {minimum_cost}")


# Main function
if __name__ == "__main__":
    V = 4  # Number of vertices in graph
    E = 5  # Number of edges in graph
    graph = KruskalAlgorithm(V, E)

    # Add edges
    graph.edges.append(Edge(0, 1, 10))
    graph.edges.append(Edge(0, 2, 6))
    graph.edges.append(Edge(0, 3, 5))
    graph.edges.append(Edge(1, 3, 15))
    graph.edges.append(Edge(2, 3, 4))

    # Function call to find the minimum spanning tree
    graph.kruskal_mst()