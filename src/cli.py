"""
Command Line Interface for data preprocessing operations.
Groups: clean, numeric, text, struct.
"""

import ast
import click
from .preprocessing import (
    remove_missing,
    fill_missing,
    remove_duplicates,
    normalize,
    standardize,
    clip,
    to_integers,
    log_transform,
    tokenize,
    remove_punctuation,
    remove_stopwords,
    flatten,
    shuffle,
)


@click.group(help="Main CLI group for data preprocessing operations")
def cli() -> None:
    """Entry point for the preprocessing CLI."""


# === CLEAN GROUP ===
clean = click.Group("clean", help="Data cleaning operations")


@clean.command("remove-missing", help='Remove missing values (None, "", "nan")')
@click.argument("values", nargs=-1)
def remove_missing_cmd(values: tuple) -> None:
    """Example: cli clean remove-missing 1 None "" nan 2"""
    result = remove_missing(list(values))
    click.echo(result)


@clean.command("fill-missing", help="Fill missing values with a specified value")
@click.argument("values", nargs=-1)
@click.option(
    "--fill-value", default=0, help="Value to replace missing data", type=float
)
def fill_missing_cmd(values: tuple, fill_value: float) -> None:
    """Example: cli clean fill-missing 1 None 3 --fill-value 999"""
    result = fill_missing(list(values), fill_value)
    click.echo(result)


cli.add_command(clean)


# === NUMERIC GROUP ===
numeric = click.Group("numeric", help="Numeric data operations")


@numeric.command("normalize", help="Min-max normalization")
@click.argument("values", nargs=-1, type=float)
@click.option("--new-min", default=0.0, help="New minimum value")
@click.option("--new-max", default=1.0, help="New maximum value")
def normalize_cmd(values: tuple, new_min: float, new_max: float) -> None:
    """Example: cli numeric normalize 0 5 10 --new-min 0 --new-max 1"""
    result = normalize(list(values), new_min, new_max)
    click.echo(result)


@numeric.command("standardize", help="Z-score standardization")
@click.argument("values", nargs=-1, type=float)
def standardize_cmd(values: tuple) -> None:
    """Example: cli numeric standardize 1 2 3 4 5"""
    result = standardize(list(values))
    click.echo(result)


@numeric.command("clip", help="Clip values to a range")
@click.argument("values", nargs=-1, type=float)
@click.option("--min", "min_val", default=0.0, help="Minimum value to clip")
@click.option("--max", "max_val", default=1.0, help="Maximum value to clip")
def clip_cmd(values: tuple, min_val: float, max_val: float) -> None:
    """Example: cli numeric clip 1 2 3 4 5 --min 2 --max 4"""
    result = clip(list(values), min_val, max_val)
    click.echo(result)


@numeric.command("to-integers", help="Convert string numbers to integers")
@click.argument("values", nargs=-1)
def to_integers_cmd(values: tuple) -> None:
    """Example: cli numeric to-integers "1.5" "2" "abc" """
    result = to_integers(list(values))
    click.echo(result)


@numeric.command("log-transform", help="Apply log to positive values")
@click.argument("values", nargs=-1, type=float)
def log_transform_cmd(values: tuple) -> None:
    """Example: cli numeric log-transform 1 10 100"""
    result = log_transform(list(values))
    click.echo(result)


cli.add_command(numeric)


# === TEXT GROUP ===
text_group = click.Group(
    "text", help="Text processing operations"
)  # Renombrado para evitar conflicto


@text_group.command("tokenize", help="Tokenize text (alphanumeric, lowercase)")
@click.argument("text", type=str)
def tokenize_cmd(text: str) -> None:
    """Example: cli text tokenize "Hello, World! 123" """
    result = tokenize(text)
    click.echo(result)


@text_group.command(
    "remove-punctuation", help="Remove punctuation, keep alphanumerics and spaces"
)
@click.argument("text", type=str)
def remove_punctuation_cmd(text: str) -> None:
    """Example: cli text remove-punctuation "Hello, world!" """
    result = remove_punctuation(text)
    click.echo(result)


@text_group.command("remove-stopwords", help="Remove stopwords (case insensitive)")
@click.argument("text", type=str)
@click.option("--stopwords", multiple=True, default=[], help="Stopwords to remove")
def remove_stopwords_cmd(text: str, stopwords: tuple) -> None:
    """Example: cli text remove-stopwords "this is a test" --stopwords "is" --stopwords "a" """
    result = remove_stopwords(text, list(stopwords))
    click.echo(result)


cli.add_command(text_group)


# === STRUCT GROUP ===
struct = click.Group("struct", help="Data structure operations")


@struct.command("shuffle", help="Shuffle list with optional seed")
@click.argument("values", nargs=-1)
@click.option("--seed", type=int, default=None, help="Random seed for reproducibility")
def shuffle_cmd(values: tuple, seed: int | None) -> None:
    """Example: cli struct shuffle 1 2 3 4 5 --seed 42"""
    result = shuffle(list(values), seed)
    click.echo(result)


@struct.command("flatten", help="Flatten a list of lists")
@click.argument("values", nargs=-1)
def flatten_cmd(values: tuple) -> None:
    """Example: cli struct flatten "[1,2]" "[3,4]" """
    try:
        list_of_lists = [
            ast.literal_eval(v)
            for v in values
            if isinstance(v, str) and v.startswith("[")
        ]
        result = flatten(list_of_lists)
    except Exception:  # pylint: disable=broad-except
        result = []
    click.echo(result)


@struct.command("unique", help="Remove duplicate values (preserve order)")
@click.argument("values", nargs=-1)
def unique_cmd(values: tuple) -> None:
    """Example: cli struct unique 1 2 2 3 1"""
    result = remove_duplicates(list(values))
    click.echo(result)


cli.add_command(struct)


if __name__ == "__main__":
    cli()
