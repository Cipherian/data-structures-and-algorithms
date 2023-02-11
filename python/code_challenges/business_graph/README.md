# Business Graph Trip

- Author: Daniel brott

- Code: [Business_Graph_Trip](../graph_business_trip.py)
- 
- Whiteboard: [Business_Graph_Whiteboard](./images/business_graph.jpg)

## Feature Tasks

- Write a function claled business trip

- Takes in a graph and a list of city names

- Returns the cost of the trip if it's possible or null if it is not

## Functionality

- First declare a function which takes in two parameters, graph and a cities list

- Then initialize a variable to 0 to hold cost

- then iterate through the length of the cities - 1

- declare two variables two hold the start city and the end city

- Initialize the start vertex and the end vertex

- Then traverse through the graph nodes, if the vertex value is equal to the start of the citie then we set it to the vertex7

- if the vertex value is equal to the end city then we set the end of the vertex to the vertex

- if nothing has been assigned to the start vertex or the end vertex return None

- Then iterate through the neighbors if the neighers vertex is the end vertex increment the cost with the neighbors weight

- if no edge exists, return None
