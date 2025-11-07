import click
from preprocessing import remove_missing, fill_missing, remove_duplicates, normalize, standardize, clip, to_integers, log_transform, tokenize, remove_punctuation, remove_stopwords, flatten, shuffle


@click.group(help="Main CLI group for data preprocessing")
def cli():
    pass

# === CLEAN GROUP ===
clean = click.Group('clean', help='Data cleaning operations')

@clean.command('remove-missing', help='Remove missing values')
@click.argument('values', nargs=-1)
def remove_missing_cmd(values):
    """Example: cli clean remove-missing 1 2 None '' nan 3"""
    result = remove_missing(list(values))
    click.echo(result)

@clean.command('fill-missing', help='Fill missing values')
@click.argument('values', nargs=-1)
@click.option('--fill-value', default=0, help='Value to fill missing data')
def fill_missing_cmd(values, fill_value):
    result = fill_missing(list(values), fill_value)
    click.echo(result)

cli.add_command(clean)

# === NUMERIC GROUP ===
numeric = click.Group('numeric', help='Numeric data operations')

@numeric.command('normalize')
@click.argument('values', nargs=-1, type=float)
@click.option('--new-min', default=0.0)
@click.option('--new-max', default=1.0)
def normalize_cmd(values, new_min, new_max):
    result = normalize(values, new_min, new_max)
    click.echo(result)

@numeric.command('standardize')
@click.argument('values', nargs=-1, type=float)
def standardize_cmd(values):
    result = standardize(values)
    click.echo(result)

@numeric.command('clip')
@click.argument('values', nargs=-1, type=float)
@click.option('--min', 'min_val', default=0.0)
@click.option('--max', 'max_val', default=1.0)
def clip_cmd(values, min_val, max_val):
    result = clip(values, min_val, max_val)
    click.echo(result)

@numeric.command('to-integers')
@click.argument('values', nargs=-1)
def to_integers_cmd(values):
    result = to_integers(values)
    click.echo(result)

@numeric.command('log-transform')
@click.argument('values', nargs=-1, type=float)
def log_transform_cmd(values):
    result = log_transform(values)
    click.echo(result)

cli.add_command(numeric)

# === TEXT GROUP ===
text = click.Group('text', help='Text processing')

@text.command('tokenize')
@click.argument('text')
def tokenize_cmd(text):
    result = tokenize(text)
    click.echo(result)

@text.command('remove-punctuation')
@click.argument('text')
def remove_punctuation_cmd(text):
    result = remove_punctuation(text)
    click.echo(result)

@text.command('remove-stopwords')
@click.argument('text')
@click.option('--stopwords', multiple=True, default=[])
def remove_stopwords_cmd(text, stopwords):
    result = remove_stopwords(text, list(stopwords))
    click.echo(result)

cli.add_command(text)

# === STRUCT GROUP ===
struct = click.Group('struct', help='Data structure operations')

@struct.command('shuffle')
@click.argument('values', nargs=-1)
@click.option('--seed', type=int, default=None)
def shuffle_cmd(values, seed):
    result = shuffle(list(values), seed)
    click.echo(result)

@struct.command('flatten')
@click.argument('values', nargs=-1)
def flatten_cmd(values):
    # Convert string like "[1,2],[3,4]" → [[1,2],[3,4]]
    import ast
    try:
        list_of_lists = [ast.literal_eval(v) for v in values if v.startswith('[')]
        result = flatten(list_of_lists)
    except:
        result = []
    click.echo(result)

@struct.command('unique')
@click.argument('values', nargs=-1)
def unique_cmd(values):
    result = remove_duplicates(list(values))
    click.echo(result)

cli.add_command(struct)

if __name__ == '__main__':
    cli()