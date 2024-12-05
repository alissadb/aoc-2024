import numpy as np
from loguru import logger

from aoc.utils import read_split_data


def is_safe(report: list[int]) -> np.bool:
    diff = np.diff(np.array(report))
    return (np.all(diff > 0) or np.all(diff < 0)) and np.all(np.abs(diff) >= 1) and np.all(np.abs(diff) <= 3)


def calculate_number_of_reports(reports: list[str]) -> tuple[int, int]:
    number_of_reports = 0
    number_of_reports_single_bad_level = 0
    for index, report in enumerate(reports):
        numbers = [int(number) for number in report.split(" ")]

        if is_safe(numbers):
            number_of_reports += 1
        else:
            for index, number in enumerate(numbers):
                numbers.pop(index)
                if is_safe(numbers):
                    number_of_reports_single_bad_level += 1
                    break
                numbers.insert(index, number)
    return number_of_reports, number_of_reports_single_bad_level


def main() -> None:
    reports = read_split_data("puzzles/day2.txt")
    number_of_reports, number_of_reports_single_bad_level = calculate_number_of_reports(reports)

    logger.info(f"Part 1: {number_of_reports}")
    logger.info(f"Part 2: {number_of_reports + number_of_reports_single_bad_level}")


if __name__ == "__main__":
    main()
