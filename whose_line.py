from typing import List


def avg_diff(a: List[int], b: List[int]) -> float:
    """
    Calculate the average of the absolute differences between corresponding elements of two lists.
    :param a: First list of integers.
    param b: Second list of integers.
    :return float: The average of the absolute differences.
    """

    return sum(abs(x - y) for x, y in zip(a, b)) / len(a)


def remove_leading_whitespaces(s: List[str]) -> List[str]:
    """
    Remove leading whitespaces from each string in the list.
    :param s: List of strings.
    :return List[str]: List of strings with leading whitespaces removed.
    """
    return [line.lstrip() for line in s]


def strip_lines(s: str) -> str:
    """
    Strip leading and trailing whitespaces for each line of the string.
    :param s: Input string.
    :return str: Stripped string.
    """
    return "\n".join(line.strip() for line in s.splitlines())


def main() -> None:
    a: List[int] = [1, 2, 3]
    b: List[int] = [4, 5, 6]
    result = avg_diff(a, b)
    assert result == 3.0
    b = [1, 2, 3]
    result = avg_diff(a, b)
    assert result == 0.0


if __name__ == "__main__":
    main()
