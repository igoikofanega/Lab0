"""
Data preprocessing utilities:
- Cleaning: missing, duplicates
- Numeric: normalize, standardize, clip
- Text: tokenize, clean, stopwords
- Structure: flatten, shuffle
"""

import math
import random
from typing import List, Any
import re


def remove_missing(values: List[Any]) -> List[Any]:
    """
    Removes missing values (None, '', 'nan or 'none') from a list of values.

    Args:
        data: List of values, potentially including missing ones.

    Returns:
        List of values without missing ones.
    """
    result = []
    for v in values:
        if (
            v is not None
            and v != ""
            and str(v).lower() != "nan"
            and str(v).lower() != "none"
        ):
            result.append(v)
    return result


def fill_missing(values: List[Any], fill_value: Any = 0) -> List[Any]:
    """
    Replaces missing values (None, '', 'nan or 'none') with a specified fill value.

    Args:
        data: List of values, potentially including missing ones.
        fill_value: The value to use for replacement (default is 0).

    Returns:
        List of values with missing ones replaced.
    """
    result = []
    for v in values:
        if (
            v is None
            or v == ""
            or str(v).lower() == "nan"
            or str(v).lower() == "none"
        ):
            result.append(fill_value)
        else:
            result.append(v)
    return result


def remove_duplicates(values: List[Any]) -> List[Any]:
    """
    Removes duplicated values from a list, preserving order of first appearance.

    Args:
        data: List of values.

    Returns:
        List of unique values.
    """
    seen = set()
    return [x for x in values if not (x in seen or seen.add(x))]


def normalize(
    values: List[float], new_min: float = 0.0, new_max: float = 1.0
) -> List[float]:
    """
    Normalizes numerical values using the Min-Max method.

    Args:
        data: List of numerical values.
        new_min: The minimum value of the new range (by default is 0.0).
        new_max: The maximum value of the new range (by default is 1.0).

    Returns:
        List of normalized values (float).
    """
    if not values:
        return []
    v_min, v_max = min(values), max(values)
    if v_min == v_max:
        return [new_min] * len(values)
    return [
        new_min + (v - v_min) * (new_max - new_min) / (v_max - v_min) for v in values
    ]


def standardize(values: List[float]) -> List[float]:
    """
    Standardizes numerical values using the Z-score method.

    Args:
        data: List of numerical values.

    Returns:
        List of standardized values (float).
    """
    if not values:
        return []
    mean = sum(values) / len(values)
    std = (sum((v - mean) ** 2 for v in values) / len(values)) ** 0.5
    if std == 0:
        return [0.0] * len(values)
    return [(v - mean) / std for v in values]


def clip(values: List[float], min_val: float, max_val: float) -> List[float]:
    """
    Clips numerical values to a specified minimum and maximum range.

    Args:
        data: List of numerical values.
        min_clip: Minimum value to clip to.
        max_clip: Maximum value to clip to.

    Returns:
        List of clipped values.
    """
    return [max(min_val, min(v, max_val)) for v in values]


def to_integers(str_list: List[str]) -> List[int]:
    """
    Converts elements in a list of strings to integers, excluding non-numerical
    and incomplete numerical strings.

    Args:
        data: List of strings (can include numerical and non-numerical values).

    Returns:
        List of values converted to integers (non-numerical values are excluded).
    """
    result = []
    for s in str_list:
        try:
            result.append(int(float(s)))
        except (ValueError, TypeError):
            continue
    return result


def log_transform(values: List[float]) -> List[float]:
    """
    Applies a logarithmic scale transformation (natural log, ln) to a list of values.
    Only positive numbers are transformed (log(x) for x > 0).

    Args:
        data: List of numerical values.

    Returns:
        List of values converted to logarithmic scale.
    """
    return [math.log(v) for v in values if v > 0]


def tokenize(text: str) -> List[str]:
    """
    Tokenizes text into words, keeping only alphanumeric characters and lower-casing words.

    Args:
        text: Text.

    Returns:
        Processed text (string).
    """
    return [word.lower() for word in re.findall(r"\w+", text)]


def remove_punctuation(text: str) -> str:
    """
    Processes text by selecting only alphanumeric characters and spaces (removes punctuation).

    Args:
        text: Text to be processed.

    Returns:
        Processed text (string).
    """
    return re.sub(r"[^a-zA-Z0-9\s]", " ", text)


def remove_stopwords(text: str, stopwords: List[str]) -> str:
    """
    Remove stopwords from the input text in a case-insensitive manner.
    
    Args:
        text (str): The input text to process.
        stopwords (List[str]): List of stopwords to remove.
    
    Returns:
        str: Text with stopwords removed, preserving original word order.
    """
    words = text.lower().split()
    return " ".join([w for w in words if w not in stopwords])


def flatten(list_of_lists: List[List[Any]]) -> List[Any]:
    """
    Flatten a list of lists by one level.
    
    Args:
        list_of_lists (List[List[Any]]): A list containing sublists to flatten.
    
    Returns:
        List[Any]: A single list containing all elements from the sublists.
    """
    return [item for sublist in list_of_lists for item in sublist]


def shuffle(values: List[Any], seed: int = None) -> List[Any]:
    """
    Shuffle a list in-place and return the shuffled copy. Optionally use a seed for reproducibility.
    
    Args:
        values (List[Any]): The list to shuffle.
        seed (int, optional): Random seed for reproducible shuffling. Defaults to None.
    
    Returns:
        List[Any]: A new shuffled list (original list remains unchanged).
    """
    result = values[:]
    if seed is not None:
        random.seed(seed)
    random.shuffle(result)
    return result
