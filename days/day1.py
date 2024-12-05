from collections import Counter

import numpy as np

from aoc import read_split_data

locations = read_split_data("puzzles/input1.txt")

locations = [location.split() for location in locations]

location_1 = []
location_2 = []
for location in locations:
    print(location)
    location_1.append(int(location[0]))
    location_2.append(int(location[1]))

location_1_argsort = np.argsort(location_1)
location_2_argsort = np.argsort(location_2)

distance = 0
for index, locations in enumerate(zip(location_1_argsort, location_2_argsort, strict=False)):
    print(f"Index {index}, Location: {locations[0]}, Location: {locations[1]}")

    a = location_1[locations[0]]
    b = location_2[locations[1]]

    distance += abs(a - b)

counter_1 = Counter(location_1)
counter_2 = Counter(location_2)

intersection_keys = set(counter_1.keys()).intersection(set(counter_2.keys()))

similarity = 0
for item in counter_2.items():
    if item[0] in intersection_keys:
        similarity += item[0] * item[1]

print(f"Part 1: distance - {distance}")
print(f"Part 2: similarity - {similarity}")
