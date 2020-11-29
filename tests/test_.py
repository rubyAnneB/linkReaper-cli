from click.testing import CliRunner
import linkReaper


def test_readwebsite():
    runner = CliRunner()
    result = runner.invoke(linkReaper.readwebsite, ["www.google.com"])
    assert result.exit_code == 0


def test_readfile():
    runner = CliRunner()
    result = runner.invoke(linkReaper.readfile, [""])
    assert result.exit_code != 0


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4
