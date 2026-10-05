# AI Assignment 1 – Dijkstra's Algorithm

# Project Description

This project implements **Dijkstra's Shortest Path Algorithm** to find the shortest route between two Indian cities.

The program uses an **Indian cities dataset** containing:

- Origin city
- Destination city
- Distance between the cities

The dataset is converted into a weighted graph, and Dijkstra's algorithm is used to calculate the shortest path and total distance.

# Objective

The main objectives of this assignment are:

- To understand graph representation.
- To implement Dijkstra's algorithm.
- To find the shortest path between two cities.
- To calculate the minimum travel distance.
- To work with a real-world city-distance dataset.

# Technologies Used

- **Python**
- **Google Colab**
- **Pandas**
- **Heap / Priority Queue**
- **Dijkstra's Algorithm**

## 📂 Files

text
AI_Assignment_1/
│
├── ai_assignment_1_dijsktras_algorithm_.py
├── indian-cities-dataset.csv
└── README.md


## 🔄 Working Procedure

### 1. Load the Dataset

The program uploads and reads the CSV dataset using Pandas.

python
df = pd.read_csv("indian-cities-dataset.csv")


It also displays the number of rows, columns, and unique cities.

### 2. Create the Graph

A `Graph` class is used to represent the Indian cities as a weighted graph.

Each city is treated as a **node**, and the distance between two cities is treated as an **edge weight**.

text
City A ---- distance ---- City B


The graph is undirected, meaning the connection works in both directions.

### 3. Build the Graph from Dataset

Every row of the dataset is processed and added to the graph.

python
graph.add_edge(origin, destination, distance)


The distance is stored as the weight of the edge.

### 4. Apply Dijkstra's Algorithm

Dijkstra's algorithm starts from the source city and repeatedly selects the unvisited city having the smallest known distance.

A **priority queue (min-heap)** is used to efficiently select the next city.

python
heap = [(0, source)]


The algorithm updates the distance whenever a shorter route is found.

### 5. Reconstruct the Shortest Path

The `parent` dictionary stores the previous city for every city.

The `build_path()` function uses this information to reconstruct the final shortest route.

### 6. User Input

The user enters:

Enter source city:
Enter destination city:

The program then finds and displays the shortest path between them.

 How to Run

# Google Colab

1. Open the Python file in Google Colab.
2. Upload the program.
3. Upload `indian-cities-dataset.csv` when prompted.
4. Run all cells.
5. Enter the source city.
6. Enter the destination city.

## Example
Enter source city: Hyderabad
Enter destination city: Delhi


# Output
Shortest Path:
Hyderabad -> ... -> Delhi

Total Distance:
XXXX km
```

The actual path and distance depend on the dataset.

 Algorithm

# Dijkstra's Algorithm

**Input:**
- Weighted graph
- Source city
- Destination city

**Output:**
- Shortest path
- Minimum total distance

### Basic Steps


1. Set source distance = 0.
2. Set all other distances = infinity.
3. Insert source into priority queue.
4. Select the city with minimum distance.
5. Check all its neighboring cities.
6. Update their distances if a shorter path is found.
7. Repeat until the destination is reached.
8. Reconstruct the shortest path.
9. Display the path and total distance.

 Complexity

Using a priority queue (min-heap), Dijkstra's algorithm has approximately:

Time Complexity:
O((V + E) log V)


where:

- `V` = number of cities (vertices)
- `E` = number of connections (edges)

Space Complexity:
O(V + E)




Dijkstra's algorithm works correctly when **edge weights are non-negative**.

In this project, the edge weights represent road distances, which are positive.


Assignment: **Artificial Intelligence – Assignment 1**

Algorithm: **Dijkstra's Shortest Path Algorithm**