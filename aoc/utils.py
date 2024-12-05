"""Helpers for AOC."""


def read_data(file_name: str) -> list[list]:
    """Read the data from a given file name.

    Args:
        file_name (str): File name of the file to read

    Returns:
        list[list]: List of lists with the data
    """
    with open(file_name, encoding="utf-8") as file_obj:
        puzzle_input = file_obj.read()

    return puzzle_input


def read_split_data(file_name: str) -> list[list]:
    """Read the data from a given file name.

    Args:
        file_name (str): File name of the file to read

    Returns:
        list[list]: List of lists with the data
    """
    with open(file_name, encoding="utf-8") as file_obj:
        puzzle_input = file_obj.read().split("\n")

    return puzzle_input
