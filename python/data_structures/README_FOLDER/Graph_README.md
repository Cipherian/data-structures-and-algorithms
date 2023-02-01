# Graph data structure implementation

- Author: Daniel Brott

## Approach

- Node/Vertex based implementation

## Functionality

### Classes

- Graph: initalized with adjacency list and five methods(see methods)

  - A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

- Vertex: Initialized with value and neighbors, which is defaulted to None.

  - vertex, also called a “node”, is a data object that can have zero or more adjacent vertices.

- Edge: Initialized with vertex and weight paramters.

  - An edge is a connection between two nodes.

### Methods

- add_node: Instantiates a new Vertex/Node value and appends it to the Graph's adjacency list

- size: returns the length of the adjacency list

- add_edge: Takes in 2 node parameters to be connected by the edge and weight which is optional

- get_nodes: Returns the adjacency list

- get_neighbors: Takes in a parameter and iterates through the adjacency list, then check if the node/vertex matches the given parameter then returns it's neighbors

- add_edge: First checks if the start or vertex are not in the adjacency list, if either are not true it raises a key error. Otherwise, it adds a new edge with vertex and weight paramters, it then iterates throug the adjacency list and checks if node/vertex are equal to the start paramter, if it is it then appends the new edge to the neighbors property in the Edge class.
