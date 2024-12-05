from functools import cmp_to_key

import numpy as np
from loguru import logger


def read_input() -> tuple[set[tuple[int, int]], list[list[int]]]:
    with open("puzzles/day5.txt") as file:
        rules_info, updates_info = file.read().strip().split("\n\n")

    rules = {(int(rule.split("|")[0]), int(rule.split("|")[1])) for rule in rules_info.split("\n")}
    updates = [list(map(int, update.split(","))) for update in updates_info.split("\n")]

    return rules, updates

def is_valid_rule(update: list[int], rules: set[tuple[int, int]]) -> bool:
  valid_indices = []
  for left_value, right_value in rules:
    if left_value in update and right_value in update:
       valid_indices.append(update.index(left_value) < update.index(right_value))

  return all(valid_indices)


def sort_update(update: list[int], rules: set[tuple[int, int]]) -> list[int]:
    return sorted(update, key=cmp_to_key(lambda left_value, right_value: -1 if (left_value, right_value) in rules else 0))

def calculate_median(updates: list[list[int]], rules: set[tuple[int, int]]) -> tuple[int, int]:
    median_updates = 0
    median_updates_invalid = 0

    for update in updates:
        if is_valid_rule(update, rules):
            print(f"Valid update: {update}")
            median_updates += np.take(update, len(update) // 2)
        else:
            print(f"Invalid update: {update}")
            sorted_update = sort_update(update, rules)
            median_updates_invalid += np.take(sorted_update, len(sorted_update) // 2)

    return median_updates, median_updates_invalid

def main() -> None:
    rules, updates = read_input()
    median_updates, median_updates_invalid = calculate_median(updates, rules)

    logger.info(f"Part 1: {median_updates}")
    logger.info(f"Part 2: {median_updates_invalid}")

if __name__ == "__main__":
    main()


