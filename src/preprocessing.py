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
    """Remove missing values: None, '', float('nan'), 'none'"""
    return [v for v in values if v is not None and v != '' and str(v).lower() != 'nan' and str(v).lower() != 'none']


def fill_missing(values: List[Any], fill_value: Any = 0) -> List[Any]:
    """Replace missing values with fill_value"""
    return [fill_value if v is None or v == '' or str(v).lower() == 'nan' or str(v).lower() == 'none' else v for v in values]


def remove_duplicates(values: List[Any]) -> List[Any]:
    """Return unique values preserving order"""
    seen = set()
    return [x for x in values if not (x in seen or seen.add(x))]


def normalize(
    values: List[float], new_min: float = 0.0, new_max: float = 1.0
) -> List[float]:
    """Min-max normalization"""
    if not values:
        return []
    v_min, v_max = min(values), max(values)
    if v_min == v_max:
        return [new_min] * len(values)
    return [
        new_min + (v - v_min) * (new_max - new_min) / (v_max - v_min) for v in values
    ]


def standardize(values: List[float]) -> List[float]:
    """Z-score standardization"""
    if not values:
        return []
    mean = sum(values) / len(values)
    std = (sum((v - mean) ** 2 for v in values) / len(values)) ** 0.5
    if std == 0:
        return [0.0] * len(values)
    return [(v - mean) / std for v in values]


def clip(values: List[float], min_val: float, max_val: float) -> List[float]:
    """Clip values to [min_val, max_val]"""
    return [max(min_val, min(v, max_val)) for v in values]


def to_integers(str_list: List[str]) -> List[int]:
    """Convert string numbers to int, skip non-numeric"""
    result = []
    for s in str_list:
        try:
            result.append(int(float(s)))
        except (ValueError, TypeError):
            continue
    return result


def log_transform(values: List[float]) -> List[float]:
    """Apply log to positive values only"""
    return [math.log(v) for v in values if v > 0]


def tokenize(text: str) -> List[str]:
    """Tokenize, keep alphanumeric, lowercase"""
    return [word.lower() for word in re.findall(r"\w+", text)]


def remove_punctuation(text: str) -> str:
    """Keep only alphanumerics and spaces"""
    return re.sub(r"[^a-zA-Z0-9\s]", " ", text)


def remove_stopwords(text: str, stopwords: List[str]) -> str:
    """Remove stopwords (case insensitive)"""
    words = text.lower().split()
    return " ".join([w for w in words if w not in stopwords])


def flatten(list_of_lists: List[List[Any]]) -> List[Any]:
    """Flatten one level"""
    return [item for sublist in list_of_lists for item in sublist]


def shuffle(values: List[Any], seed: int = None) -> List[Any]:
    """Shuffle list with optional seed"""
    result = values[:]
    if seed is not None:
        random.seed(seed)
    random.shuffle(result)
    return result
