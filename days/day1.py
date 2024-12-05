from collections import Counter

import numpy as np
from loguru import logger

from aoc.utils import read_split_data


def parse_locations(locations: list[str]) -> tuple[list[int], list[int]]:
    locations = [location.split() for location in locations]

    location_1 = []
    location_2 = []
    for location in locations:
        location_1.append(int(location[0]))
        location_2.append(int(location[1]))
    return location_1, location_2


def calculate_distance(location_1: list[int], location_2: list[int]) -> int:
    location_1_argsort = np.argsort(location_1)
    location_2_argsort = np.argsort(location_2)

    distance = 0
    for index, locations in enumerate(zip(location_1_argsort, location_2_argsort, strict=False)):
        print(f"Index {index}, Location: {locations[0]}, Location: {locations[1]}")
        distance += abs(location_1[locations[0]] - location_2[locations[1]])

    return distance


def calculate_similarity(location_1: list[int], location_2: list[int]) -> int:
    counter_1 = Counter(location_1)
    counter_2 = Counter(location_2)

    intersection_keys = set(counter_1.keys()).intersection(set(counter_2.keys()))

    similarity = 0
    for item in counter_2.items():
        if item[0] in intersection_keys:
            similarity += item[0] * item[1]

    return similarity


def main() -> None:
    locations = read_split_data("puzzles/day1.txt")

    location_1, location_2 = parse_locations(locations)

    distance = calculate_distance(location_1, location_2)
    similarity = calculate_similarity(location_1, location_2)

    logger.info(f"Part 1: distance - {distance}")
    logger.info(f"Part 2: similarity - {similarity}")


if __name__ == "__main__":
    main()
