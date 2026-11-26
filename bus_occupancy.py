capacity = int(input("Enter maximum bus capacity: "))
stops = int(input("Enter number of stops: "))

current = 0
peak = 0
violations = 0
log = []

for i in range(stops):
    print(f"\nStop {i + 1}:")
    stop_name = input("  Stop Name: ")
    alight = int(input("  Passengers Alighting: "))
    board = int(input("  Passengers Boarding: "))

    if alight < 0 or board < 0 or alight > current:
        print("  -> Invalid count! Alighting cannot exceed onboard passengers.")
        continue

    current = current - alight + board
    if current > peak:
        peak = current

    status = "OK"
    if current > capacity:
        violations += 1
        status = "OVER CAPACITY!"

    log.append((stop_name, alight, board, current, status))

print("\n----- BUS OCCUPANCY SIMULATION REPORT -----")
for entry in log:
    print(f"Stop: {entry[0]:<12} | Off: {entry[1]:<2} | On: {entry[2]:<2} | Total: {entry[3]:<2} | {entry[4]}")
print("-------------------------------------------")
print(f"Bus Max Capacity    : {capacity}")
print(f"Peak Occupancy      : {peak}")
print(f"Capacity Violations : {violations}")
