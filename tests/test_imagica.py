"""Test for the imagica package."""
import toml

from imagica import __version__


def test_version() -> None:
    """Check the version."""
    config = toml.load("pyproject.toml")
    version = config["tool"]["poetry"]["version"]
    assert __version__ == version
