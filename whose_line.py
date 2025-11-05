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


def has_dup(li: List[int]) -> bool:
    """
    Check if the list has duplicate elements.
    :param li: List of integers.
    :return bool: True if duplicates exist, False otherwise.
    """
    return len(li) != len(set(li))


def flatten(nested_list: List[List[int]]) -> List[int]:
    """
    Flatten a nested list of integers into a single list.
    :param nested_list: List of lists of integers.
    :return List[int]: Flattened list of integers.
    """
    return [item for sublist in nested_list for item in sublist]


def main() -> None:
    # Test cases to validate avg_diff
    a: List[int] = [1, 2, 3]
    b: List[int] = [4, 5, 6]
    result = avg_diff(a, b)
    assert result == 3.0
    b = [1, 2, 3]
    result = avg_diff(a, b)
    assert result == 0.0

    # Test cases to validate remove_leading_whitespaces and strip_lines
    string2: List[str] = [
        "    line one",
        "  line two",
        "\tline three",
    ]
    stripped_lines = remove_leading_whitespaces(string2)
    assert stripped_lines == ["line one", "line two", "line three"]

    string3: str = "   line one   \n  line two  \n\tline three\t"
    stripped_string = strip_lines(string3)
    assert stripped_string == "line one\nline two\nline three"

    # Test cases to validate has_dup
    list_with_dups: List[int] = [1, 2, 3, 2]
    assert has_dup(list_with_dups) is True
    list_without_dups: List[int] = [1, 2, 3]
    assert has_dup(list_without_dups) is False

    # Test cases to validate flatten
    nested_list: List[List[int]] = [[1, 2], [3, 4], [5]]
    flattened = flatten(nested_list)
    assert flattened == [1, 2, 3, 4, 5]
    nested_list_empty: List[List[int]] = []
    flattened_empty = flatten(nested_list_empty)
    assert flattened_empty == []
    nested_list_single: List[List[int]] = [[1, 2, 3], []]
    flattened_single = flatten(nested_list_single)
    assert flattened_single == [1, 2, 3]



if __name__ == "__main__":
    main()
