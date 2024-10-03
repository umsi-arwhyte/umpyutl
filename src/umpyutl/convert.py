from typing import Any, Optional


def to_float(value: str) -> float | Any:
    """Attempts to convert a < value > to a float including numeric strings that include one or
    more thousand separator commas (e.g., "1,000,000.9999"). If a runtime exception is encountered the
    < value > is returned to the caller unchanged.

    Parameters:
        value (bool|float|int|str): string or number to be converted

    Returns:
        float|any: float if value converted; otherwise returns value unchanged
    """

    try:
        return float(value.replace(",", ""))
    except (AttributeError, TypeError, ValueError):
        return value


def to_int(value: str) -> int | Any:
    """Attempts to convert a < value > to an integer including numeric strings that include one or
    more thousand separator commas (e.g., "1,000,000") or a period designating a fractional
    component (e.g., "1,000,000.9999"). If a runtime exception is encountered the < value > is
    returned to the caller unchanged.

    Parameters:
        value (bool|float|int|str): value to be converted

    Returns:
        int|any: integer if value converted else returns value unchanged
    """

    try:
        return int(float(value.replace(",", "")))
    except (AttributeError, TypeError, ValueError):
        return value


def to_list(value: str, delimiter: Optional[str] = None) -> list | Any:
    """Attempts to convert a string < value > to a list in the < try > block using the provided
    < delimiter >. Removes leading/trailing spaces before converting < value > to a list.

    If a runtime exception is encountered the < value > is returned unchanged in the except block.

    Parameters:
        value (str): string to be split.
        delimiter (str): optional delimiter provided for splitting the string

    Returns:
         list|any: list if value successfully converted else returns value unchanged
    """

    try:
        if delimiter:
            return value.strip().split(delimiter)
        else:
            return value.strip().split()
    except (AttributeError, TypeError, ValueError):
        return value
