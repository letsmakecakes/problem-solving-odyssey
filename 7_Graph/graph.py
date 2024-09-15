"""
Module for creating and manipulating an undirected graph data structure.

This module defines a `Graph` class which allows users to add vertices, add edges, 
remove vertices, remove edges, and print the graph in adjacency list format. The graph 
is implemented as an adjacency list stored in a dictionary, where each key is a vertex 
and its value is a list of adjacent vertices.
"""

class Graph:
    """
    Class representing an undirected graph using an adjacency list.

    Methods:
    --------
    add_vertex(vertex):
        Adds a vertex to the graph.

    add_edge(v1, v2):
        Adds an undirected edge between two vertices.

    remove_edge(v1, v2):
        Removes an undirected edge between two vertices.

    remove_vertex(vertex):
        Removes a vertex and all its associated edges from the graph.

    print_graph():
        Prints the adjacency list representation of the graph.
    """

    def __init__(self):
        """Initializes an empty graph with no vertices or edges."""
        self.adj_list = {}

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.

        Parameters:
        -----------
        vertex : any hashable type
            The vertex to add to the graph.

        Returns:
        --------
        bool
            True if the vertex was successfully added, False if it already exists.
        """
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        """
        Adds an undirected edge between two vertices.

        Parameters:
        -----------
        v1, v2 : any hashable type
            The vertices between which the edge is to be added.

        Returns:
        --------
        bool
            True if the edge was successfully added, False if either vertex does not exist.
        """
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        """
        Removes an undirected edge between two vertices.

        Parameters:
        -----------
        v1, v2 : any hashable type
            The vertices between which the edge is to be removed.

        Returns:
        --------
        bool
            True if edge removed, False if either vertex does not exist or the edge is not present.
        """
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        """
        Removes a vertex and all associated edges from the graph.

        Parameters:
        -----------
        vertex : any hashable type
            The vertex to remove.

        Returns:
        --------
        bool
            True if the vertex was successfully removed, False if the vertex does not exist.
        """
        if vertex in self.adj_list:
            for other_vertex in self.adj_list[vertex]:
                try:
                    self.adj_list[other_vertex].remove(vertex)
                except ValueError:
                    pass

            del self.adj_list[vertex]
            return True
        return False

    def print_graph(self):
        """
        Prints the graph in an adjacency list format.

        Each vertex and its list of adjacent vertices are printed on a new line.
        """
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")


# Example usage of the Graph class
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')

print("Graph after adding vertices and edges:")
my_graph.print_graph()

my_graph.remove_vertex('D')

print("\nGraph after removing vertex 'D':")
my_graph.print_graph()
