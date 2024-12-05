import re

from loguru import logger

from aoc.utils import read_data

MUL_PATTERN = r"mul\((\d+),(\d+)\)"
DO_DONT_MUL_PATTERN = r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))"


def part1(mul_instructions: str) -> int:
    instructions = re.findall(MUL_PATTERN, mul_instructions)

    number = 0
    for instruction in instructions:
        number += int(instruction[0]) * int(instruction[1])

    return number


def part2(mul_instructions: str) -> int:
    instructions = re.findall(DO_DONT_MUL_PATTERN, mul_instructions)

    number = 0
    enabled = True
    for instruction in instructions:
        instruction_str = instruction[0]

        if instruction_str == "do()":
            enabled = True
        elif instruction_str == "don't()":
            enabled = False
        elif enabled:
            number += int(instruction[1]) * int(instruction[2])

    return number


def main() -> None:
    mul_instructions = read_data("puzzles/day3.txt")

    part1(mul_instructions)
    part2(mul_instructions)

    logger.info(f"Part 1: {part1(mul_instructions)}")
    logger.info(f"Part 2: {part2(mul_instructions)}")


if __name__ == "__main__":
    main()
