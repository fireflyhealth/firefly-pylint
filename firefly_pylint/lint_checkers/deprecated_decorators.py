from typing import Iterable

from pylint.checkers.stdlib import StdlibChecker
from pylint.lint import PyLinter


class StdlibCheckerWithAdditionalDeprecatedDecorators(StdlibChecker):
    def deprecated_decorators(self) -> Iterable:
        deprecated_decorators = set(super().deprecated_decorators())
        deprecated_decorators.add("django.db.transaction.atomic")
        return deprecated_decorators


def register(linter: PyLinter) -> None:
    """This required method auto registers the checker during initialization.
    :param linter: The linter to register the checker to.
    """
    linter.register_checker(StdlibCheckerWithAdditionalDeprecatedDecorators(linter))
