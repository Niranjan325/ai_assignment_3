# ai_assignment_3

# AI Search Algorithms and UGV Navigation

## Overview

This project implements three Artificial Intelligence search and path-planning problems:

1. Dijkstra's Algorithm for finding shortest paths between Indian cities.
2. UGV Navigation in a static obstacle environment using A* Search.
3. UGV Navigation in a dynamic obstacle environment using replanning A* Search.

---

## Problem 1: Dijkstra's Algorithm for Indian Cities

### Objective

Implement Dijkstra's Algorithm (Uniform Cost Search) to find the shortest road distances from a selected source city to all other connected cities in India.

### Algorithm Used

* Dijkstra's Algorithm
* Priority Queue (Min Heap)

### Features

* Uses a graph representation of cities and road distances.
* Accepts a source city from the user.
* Computes shortest distances to all reachable cities.
* Displays the minimum travel distance from the source city.

### Output

The program displays the shortest path cost from the selected city to all other cities in the graph.

---

## Problem 2: UGV Navigation with Static Obstacles

### Objective

Design a path-planning algorithm for an Unmanned Ground Vehicle (UGV) operating in a battlefield environment containing known static obstacles.

### Algorithm Used

* A* Search Algorithm

### Features

* Generates a grid environment.
* Randomly places obstacles.
* Finds the shortest collision-free path.
* Avoids all known obstacles.
* Calculates path length.

### Measures of Effectiveness

* Path Length
* Number of Nodes Explored
* Path Availability
* Computational Efficiency

### Output

The program displays the shortest path from the start position to the goal position while avoiding obstacles.

---

## Problem 3: UGV Navigation with Dynamic Obstacles

### Objective

Enable a UGV to navigate in an environment where obstacles may appear or move during execution and are not known beforehand.

### Algorithm Used

* Dynamic Replanning using A* Search

### Features

* Detects newly appearing obstacles.
* Recalculates the optimal path whenever the current path becomes blocked.
* Continues navigation until the goal is reached.

### Measures of Effectiveness

* Replanning Time
* Success Rate
* Path Optimality
* Adaptability to Dynamic Changes

### Output

The program demonstrates dynamic obstacle handling by introducing new obstacles and recalculating a valid path.

---

## Technologies Used

* Python 3
* Heapq Library
* Graph Search Algorithms
* A* Path Planning
* Uniform Cost Search

---

## Project Structure

AI_Assignment/

├── dijkstra_india.py

├── ugv_static_obstacles.py

├── ugv_dynamic_obstacles.py

├── README.md

└── screenshots/

---

## Conclusion

This project demonstrates the application of Artificial Intelligence search algorithms for shortest path computation and autonomous navigation. Dijkstra's Algorithm is used for shortest path discovery in weighted graphs, while A* Search is used for efficient path planning in both static and dynamic obstacle environments. The results show the effectiveness of informed search techniques in solving real-world navigation problems.
