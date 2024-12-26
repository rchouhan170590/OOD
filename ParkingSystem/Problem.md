Problem Statement:
Design a comprehensive parking lot management system that meets the following requirements:

Functional Requirements:
1. The parking lot consists of various types of parking spots:
   - Compact
   - Large
   - Motorcycle

2. Vehicles are categorized by size:
   - Motorcycle
   - Car
   - Bus

3. Parking rules dictate that:
   - A motorcycle can park in any available spot.
   - A car can park in either a compact or large spot.
   - A bus requires multiple large spots to accommodate its size.

4. The system must support the following operations:
   - Park a vehicle, assigning it to an available spot.
   - Remove a vehicle, thereby freeing up the occupied spot.
   - Check for available spots, filtered by type.

5. The system should effectively handle edge cases, including:
   - A full parking lot scenario.
   - Invalid parking requests (e.g., attempting to park a vehicle in an unsuitable spot).

6. Additional features to implement:
   - A fee structure to calculate parking charges.
   - A timer to accurately track the duration of vehicle parking.
   - Support for buses that require multiple parking spots for proper accommodation.
