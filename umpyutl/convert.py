def convert_to_float(value):
    """Attempts to convert a string, number, or boolean < value > to a float. Can also convert
    numbers masquerading as strings that include one or more thousand separator commas
    (e.g., "5,000,000"). If a runtime AttributeError, TypeError (usually triggered by NoneType),
    or a ValueError exception is encountered, the function returns the value unchanged.

    Parameters:
        value (obj): string or number to be converted

    Returns:
        float|any: float if value successfully converted; otherwise returns value unchanged
    """

    try:
        return float(value.replace(',', ''))
    except (AttributeError, TypeError, ValueError):
        return value


def convert_to_int(value):
    """Attempts to convert a string, number boolean < value > to an int. Can also convert
    numbers masquerading as strings that include one or more thousand separator commas
    (e.g., "5,000,000"). If a runtime AttributeError, TypeError (usually triggered by NoneType),
    or a ValueError exception is encountered, the function returns the value unchanged.

    Parameters:
        value (str|int): string or number to be converted

    Returns:
        int|any: integer if value successfully converted else returns value unchanged
    """

    try:
        return int(value.replace(',', ''))
    except (AttributeError, TypeError, ValueError):
        return value


def convert_to_list(value, delimiter=None):
    """Attempts to convert a string < value > to a list using the provided < delimiter >. Removes
    leading/trailing spaces before converting < value > to a list. If a runtime AttributeError,
    TypeError (usually triggered by NoneType), or a ValueError exception is encountered, the
    function returns the value unchanged.

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