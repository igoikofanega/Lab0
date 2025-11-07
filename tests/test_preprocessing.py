import pytest
from src.preprocessing import (
    remove_missing, fill_missing, remove_duplicates, normalize,
    standardize, clip, to_integers, log_transform, tokenize,
    remove_punctuation, remove_stopwords, flatten, shuffle
)
import math

# === FIXTURE ===
@pytest.fixture
def sample_numbers():
    """Reusable list of numbers for multiple tests"""
    return [1.0, 2.0, 3.0, 4.0, 5.0]

# === PARAMETRIZE: sin opciones ===
@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 2, 3, 3, 3], [1, 2, 3]),
    (["a", "b", "a", "c"], ["a", "b", "c"]),
    ([], []),
    ([1], [1]),
])
def test_remove_duplicates(input_list, expected):
    assert remove_duplicates(input_list) == expected

# === PARAMETRIZE: con opciones ===
@pytest.mark.parametrize("values, fill_value, expected", [
    ([1, None, 3, ''], 0, [1, 0, 3, 0]),
    ([None, 'nan', 2], 999, [999, 999, 2]),
    ([], 5, []),
    (['', None], -1, [-1, -1]),
])
def test_fill_missing(values, fill_value, expected):
    assert fill_missing(values, fill_value) == expected

# === OTRAS PRUEBAS UNITARIAS ===
def test_remove_missing():
    assert remove_missing([1, None, '', 'nan', 2]) == [1, 2]

def test_normalize(sample_numbers):
    result = normalize(sample_numbers)
    assert result == [0.0, 0.25, 0.5, 0.75, 1.0]

def test_standardize(sample_numbers):
    result = standardize(sample_numbers)
    expected = [(x - 3.0) / 2.0 for x in sample_numbers]  # mean=3, std=2
    assert [round(r, 6) for r in result] == [round(e, 6) for e in expected]

def test_clip(sample_numbers):
    assert clip(sample_numbers, 2, 4) == [2, 2, 3, 4, 4]

def test_to_integers():
    assert to_integers(["1", "2.5", "abc", "3", "4.0"]) == [1, 2, 3, 4]

def test_log_transform():
    result = log_transform([1, math.e, math.e**2])
    assert [round(r, 6) for r in result] == [0.0, 1.0, 2.0]

def test_tokenize():
    text = "Hello, World! This is 2025."
    assert tokenize(text) == ["hello", "world", "this", "is", "2025"]

def test_remove_punctuation():
    text = "Hello, world! How are you???"
    assert remove_punctuation(text) == "Hello  world  How are you   "

def test_remove_stopwords():
    text = "This is a sample text"
    stopwords = ["is", "a"]
    assert remove_stopwords(text, stopwords) == "this sample text"

def test_flatten():
    assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]

def test_shuffle():
    values = [1, 2, 3, 4, 5]
    shuffled = shuffle(values, seed=42)
    assert len(shuffled) == 5
    assert set(shuffled) == {1, 2, 3, 4, 5}
    # Same seed → same result
    assert shuffle(values, seed=42) == shuffled