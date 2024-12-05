import numpy as np
from loguru import logger

from aoc.utils import read_split_data

DIRECTIONS_XMAS = {
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
}
DIRECTIONS_MAS = {
    (-1, -1),  # left upper diagonal
    (0, 0),  # center
    (-1, 1),  # right upper diagonal
    (1, 1),  # right lower diagonal
    (1, -1),  # left lower diagonal
}


def part1(xmas: np.ndarray) -> int:
    rows, cols = xmas.shape
    number_of_xmas = 0
    for row in range(rows):
        for col in range(cols):
            for direction_row, direction_column in DIRECTIONS_XMAS:
                if 0 <= row + direction_row * 3 < rows and 0 <= col + direction_column * 3 < cols:
                    chars = [
                        xmas[row, col],
                        xmas[row + direction_row, col + direction_column],
                        xmas[row + direction_row * 2, col + direction_column * 2],
                        xmas[row + direction_row * 3, col + direction_column * 3],
                    ]
                    if chars == ["X", "M", "A", "S"]:
                        number_of_xmas += 1

    return number_of_xmas


def part2(xmas: np.ndarray) -> int:
    rows, cols = xmas.shape
    number_of_xmas = 0
    for row in range(rows):
        for col in range(cols):
            if 0 <= row + 1 < rows and 0 <= row - 1 < rows and 0 <= col - 1 < cols and 0 <= col + 1 < cols:
                chars = []
                for direction_row, direction_column in DIRECTIONS_MAS:
                    chars.append(xmas[row + direction_row, col + direction_column])

                if (
                    chars == ["M", "A", "S", "S", "M"]
                    or chars == ["S", "A", "S", "M", "M"]
                    or chars == ["M", "A", "M", "S", "S"]
                    or chars == ["S", "A", "M", "M", "S"]
                ):
                    number_of_xmas += 1
    return number_of_xmas


def main() -> None:
    xmas = read_split_data("puzzles/day4.txt")
    xmas = [list(x) for x in xmas]
    xmas = np.array(xmas)

    number_of_xmas_part1 = part1(xmas)
    number_of_xmas_part2 = part2(xmas)

    logger.info(f"Part 1: {number_of_xmas_part1}")
    logger.info(f"Part 2: {number_of_xmas_part2}")


if __name__ == "__main__":
    main()
