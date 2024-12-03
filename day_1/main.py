from collections import Counter

# Part 1

list_1 = []
list_2 = []
distances = []
total_distance = 0

with open("./input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line_list = line.strip().split()
        list_1.append(int(line_list[0]))
        list_2.append(int(line_list[1]))

list_1.sort()
list_2.sort()

i = 0
while i < len(list_1):
    length = abs(list_1[i] - list_2[i])
    distances.append(length)
    i += 1

for distance in distances:
    total_distance += distance

print(total_distance)

# Part 2

similarity = 0

count = Counter(list_2)

for number in list_1:
    similarity += number * count[number]

print(similarity)
