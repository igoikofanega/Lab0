import pytest
from click.testing import CliRunner
from src.cli import cli

@pytest.fixture
def runner():
    """Shared CliRunner for all CLI tests"""
    return CliRunner()

def test_cli_clean_remove_missing(runner):
    result = runner.invoke(cli, ['clean', 'remove-missing', '1', 'None', '', 'nan', '2'])
    assert result.exit_code == 0
    assert "['1', '2']" in result.output or "[1, 2]" in result.output

def test_cli_clean_fill_missing(runner):
    result = runner.invoke(cli, ['clean', 'fill-missing', '1', 'None', '3', '--fill-value', '999'])
    assert result.exit_code == 0
    # Comprobamos que la salida contenga el float 999.0
    assert "['1', 999.0, '3']" in result.output

def test_cli_numeric_normalize(runner):
    result = runner.invoke(cli, ['numeric', 'normalize', '0', '5', '10', '--new-min', '0', '--new-max', '1'])
    assert result.exit_code == 0
    assert all(str(round(i*0.5, 6)) in result.output for i in range(3))

def test_cli_numeric_standardize(runner):
    result = runner.invoke(cli, ['numeric', 'standardize', '1', '2', '3', '4', '5'])
    assert result.exit_code == 0
    # Just check it's a list of 5 floats
    output = result.output.strip("[]\n").split(", ")
    assert len(output) == 5

def test_cli_text_tokenize(runner):
    result = runner.invoke(cli, ['text', 'tokenize', 'Hello, World! 2025'])
    assert result.exit_code == 0
    assert "['hello', 'world', '2025']" in result.output

def test_cli_text_remove_stopwords(runner):
    result = runner.invoke(cli, [
        'text', 'remove-stopwords', 'This is a test',
        '--stopwords', 'is', '--stopwords', 'a'
    ])
    assert result.exit_code == 0
    assert "this test" in result.output

def test_cli_struct_shuffle(runner):
    result = runner.invoke(cli, ['struct', 'shuffle', '1', '2', '3', '--seed', '42'])
    assert result.exit_code == 0
    assert len(result.output.strip("[]\n").split(", ")) == 3

def test_cli_struct_flatten(runner):
    result = runner.invoke(cli, ['struct', 'flatten', '[1,2]', '[3,4]'])
    assert result.exit_code == 0
    assert "[1, 2, 3, 4]" in result.output

def test_cli_struct_unique(runner):
    result = runner.invoke(cli, ['struct', 'unique', '1', '2', '2', '3', '1'])
    assert result.exit_code == 0
    assert "['1', '2', '3']" in result.output or "[1, 2, 3]" in result.output