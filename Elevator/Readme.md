# Object-Oriented Design (OOD) | Elevator System

## Overview
This document outlines the algorithm and system design for an intelligent elevator system that minimizes user wait times by efficiently managing multiple elevators.

## Algorithm for Minimizing Wait Time
### Assumptions
- **Multiple Elevators**: The building is equipped with several elevators (e.g., Elevator A, Elevator B, etc.).
- **User Requests**: Users can request elevators by pressing buttons for their desired direction (up or down) from a specific floor.

### Optimization Goals
The primary goal is to minimize wait times by intelligently assigning elevators based on:
- Proximity to the requested floor
- Current direction of travel
- Load (number of passengers)

### Elevator States
- **Idle**: The elevator is stationary and waiting for a request.
- **Moving**: The elevator is en route to a specific floor.
- **Loading/Unloading**: The elevator doors are open for passengers to enter or exit.

### Constraints
- Each elevator has a maximum capacity.
- Floors may have multiple pending requests.

## Algorithm: Intelligent Elevator Assignment
### Data Structures
- **Elevator State**: Each elevator is represented by a class with the following attributes:
  ```python
  class Elevator:
      def __init__(self, id, current_floor=0, capacity=10, min_floor=0, max_floor=10):
          self.id = id
          self.current_floor = current_floor
          self.direction = "idle"  # "up", "down", or "idle"
          self.load = 0
          self.capacity = capacity
          self.min_floor = min_floor
          self.max_floor = max_floor
          self.requests = []  # Min-heap for floors to visit
  ```

- **Global Request Queue**: A list of pending requests, where each request is represented as a dictionary:
  ```python
  {floor: int, direction: "up" | "down"}
  ```

### Initialization
- Create a list of `n` elevators, all initialized to an idle state at the ground floor.

### Request Handling
1. **Input**: When a user presses a button:
   - Add the request to the global request queue.
   - Assign the request to the most suitable elevator.

### Assignment Logic
For each new request:
1. Compute the cost for each elevator based on:
   - **Distance**: The difference between the elevator's current floor and the requested floor.
   - **Direction**: Whether the elevator is moving toward the requested floor.
   - **Load**: Preference for elevators with lower current loads.
   
2. Assign the request to the elevator with the lowest computed cost.
3. Update the elevator's requests and direction accordingly.

### Movement and Service
For each time unit:
- Move elevators toward their next target floor.
- If an elevator reaches a floor with a request:
  - Open doors to load/unload passengers.
  - Remove the fulfilled request from the queue.
  - Update the elevator's state to idle if there are no more requests.

### Dynamic Updates
Continuously monitor requests and elevator states, adjusting assignments dynamically to optimize performance.

## System Design for Multi-Elevator System
### High-Level Architecture
- **Client Layer**: 
  - Elevator buttons on each floor (for up/down requests).
  - Buttons inside each elevator to select destination floors.

- **Server Layer**: 
  - A centralized Elevator Controller System to manage requests and elevator assignments.