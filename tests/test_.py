"""This is a pytest sample that I was using for experimentation.
May move the entire project to using this"""
from click.testing import CliRunner
import linkreaper


def test_readwebsite():
    """sample test using Click's testing"""
    runner = CliRunner()
    result = runner.invoke(linkreaper.readwebsite, ["www.google.com"])
    assert result.exit_code == 0


def test_readfile():
    """sample test using Click's testing"""
    runner = CliRunner()
    result = runner.invoke(linkreaper.readfile, [""])
    assert result.exit_code != 0
