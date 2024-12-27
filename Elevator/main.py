import heapq

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

    def __str__(self):
        return f"Elevator {self.id}: Floor {self.current_floor}, Direction {self.direction}, Load {self.load}/{self.capacity}, Range [{self.min_floor}-{self.max_floor}]"

    def add_request(self, floor):
        if self.min_floor <= floor <= self.max_floor and floor not in self.requests:
            heapq.heappush(self.requests, floor)

    def move(self):
        if self.requests:
            next_floor = heapq.heappop(self.requests)
            self.direction = "up" if next_floor > self.current_floor else "down"
            self.current_floor = next_floor
            if not self.requests:
                self.direction = "idle"

class ElevatorSystem:
    def __init__(self, num_elevators):
        self.elevators = [Elevator(id=i) for i in range(num_elevators)]
        self.request_queue = []

    def add_elevator(self, min_floor, max_floor, max_capacity, current_floor=None):
        """Add a new elevator to the system."""
        id = len(self.elevators)
        current_floor = current_floor if current_floor is not None else min_floor
        elevator = Elevator(id, current_floor, max_capacity, min_floor, max_floor)
        self.elevators.append(elevator)

    def add_request(self, floor, direction):
        """Add a new request to the system."""
        self.request_queue.append((floor, direction))
        self.assign_request()

    def assign_request(self):
        """Assign requests from the queue to the most suitable elevators."""
        unassigned_requests = []

        for floor, direction in self.request_queue:
            best_elevator = None
            best_score = float('inf')

            for elevator in self.elevators:
                if (elevator.direction == direction or elevator.direction == "idle") and elevator.load < elevator.capacity:
                    if not (elevator.min_floor <= floor <= elevator.max_floor):
                        continue
                    distance = abs(elevator.current_floor - floor)
                    if direction == "up" and elevator.current_floor > floor:
                        continue
                    if direction == "down" and elevator.current_floor < floor:
                        continue
                    if distance < best_score:
                        best_elevator = elevator
                        best_score = distance

            if best_elevator:
                best_elevator.add_request(floor)
            else:
                unassigned_requests.append((floor, direction))

        self.request_queue = unassigned_requests

    def step(self):
        """Simulate one step of the system."""
        for elevator in self.elevators:
            elevator.move()

    def status(self):
        """Print the status of all elevators."""
        for elevator in self.elevators:
            print(elevator)

# Example Usage
if __name__ == "__main__":
    system = ElevatorSystem(num_elevators=3)

    # Add a new elevator to the system
    system.add_elevator(min_floor=0, max_floor=20, max_capacity=15, current_floor=5)

    # Simulate requests
    system.add_request(3, "up")
    system.add_request(5, "down")
    system.add_request(1, "up")

    # Simulate steps
    for _ in range(5):
        system.step()
        system.status()
        print("-")
