coordinates = []

with open("./input.txt", "r") as file:
    report = file.readlines()
    for levels in report:
        coordinate = levels.strip().split()
        coordinate = list(map(int, coordinate))
        coordinates.append(coordinate)

safe_count = 0
for coordinate in coordinates:
    is_safe = True
    previous_difference = None
    i = 0
    while i < len(coordinate) - 1:
        j = i + 1
        difference = coordinate[j] - coordinate[i]
        if not (1 <= abs(difference) <= 3) or (difference == 0):
            is_safe = False
            break
        if not (previous_difference == None):
            if (previous_difference < 0 and difference > 0) or (
                previous_difference > 0 and difference < 0
            ):
                is_safe = False
                break
        previous_difference = difference
        i += 1

    if is_safe:
        safe_count += 1

print(safe_count)
