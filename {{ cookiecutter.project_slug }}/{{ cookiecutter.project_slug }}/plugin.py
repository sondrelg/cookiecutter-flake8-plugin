import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ast import Module
    from typing import Generator

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    # noinspection PyUnresolvedReferences
    from importlib_metadata import version


class Plugin:
    """Flake8 plugin."""

    name = '{{ cookiecutter.project_name }}'
    version = version('{{ cookiecutter.project_name }}')

    __slots__ = ('_tree',)

    def __init__(self, tree: Module) -> None:
        self._tree = tree

    def run(self) -> Generator:
        """Run flake8 plugin and return any relevant errors."""
        line_number = 1
        column_offset = 0
        error_message = 'Something went wrong'
        yield line_number, column_offset, error_message, None
