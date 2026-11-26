# PROJECT 10 – BUS PASSENGER OCCUPANCY SIMULATION

## About the Project
The Bus Passenger Occupancy Simulation project is designed to simulate passenger movement across multiple bus stops by tracking boarding and alighting counts from stop to stop. It validates passenger counts, flags stops that exceed bus capacity, and reports peak occupancy and total violations.

## Technologies Used
- **Python** – Used to develop the bus occupancy simulation program.
- **Lists & Tuples** – Used to store stop-by-stop occupancy logs for final reporting.
- **Loops** – Used to simulate passenger changes across each stop and print the report.
- **Conditional Statements** – Used to validate counts, update peak occupancy, and flag capacity violations.
- **Arithmetic Operators** – Used to update live onboard passengers (`current - alight + board`).

## Main Features
- Accepts maximum bus capacity and total number of stops.
- Validates that alighting and boarding counts are non-negative and alighting does not exceed current onboard passengers.
- Updates live passenger count at each stop and marks `OVER CAPACITY!` when `current > capacity`.
- Reports stop-wise activity along with bus capacity, peak occupancy, and violation count.

## Algorithm
1. Start the program.
2. Read maximum bus capacity and number of stops.
3. Initialize `current = 0`, `peak = 0`, `violations = 0`, and an empty `log` list.
4. Loop through each stop to read stop name, passengers alighting, and passengers boarding.
5. Skip invalid counts where `alight < 0`, `board < 0`, or `alight > current`.
6. Update `current = current - alight + board` and update `peak` if `current > peak`.
7. Mark status as `OVER CAPACITY!` and increment `violations` if `current > capacity`, then append to `log`.
8. Display the stop-wise report, bus capacity, peak occupancy, and total violations.
9. Stop the program.

## Sample Output
Enter maximum bus capacity: 40
Enter number of stops: 4

Stop 1:
  Stop Name: Gannavaram
  Passengers Alighting: 0
  Passengers Boarding: 25

Stop 2:
  Stop Name: Benz Circle
  Passengers Alighting: 5
  Passengers Boarding: 24

Stop 3:
  Stop Name: Bus Stand
  Passengers Alighting: 18
  Passengers Boarding: 10

Stop 4:
  Stop Name: Railway Station
  Passengers Alighting: 20
  Passengers Boarding: 4

----- BUS OCCUPANCY SIMULATION REPORT -----
Stop: Gannavaram   | Off: 0  | On: 25 | Total: 25 | OK
Stop: Benz Circle  | Off: 5  | On: 24 | Total: 44 | OVER CAPACITY!
Stop: Bus Stand    | Off: 18 | On: 10 | Total: 36 | OK
Stop: Railway Station | Off: 20 | On: 4  | Total: 20 | OK
-------------------------------------------
Bus Max Capacity    : 40
Peak Occupancy      : 44
Capacity Violations : 1

## Conclusion
This project models stop-by-stop bus occupancy and overcrowding detection in a clear report. It demonstrates Python concepts such as lists, tuples, loops, conditional statements, and arithmetic tracking.
