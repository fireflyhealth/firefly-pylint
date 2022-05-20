from firefly_pylint.lint_checkers.deprecated_decorators import (  # noqa
    StdlibCheckerWithAdditionalDeprecatedDecorators,
)


def register(linter):
    linter.register_checker(StdlibCheckerWithAdditionalDeprecatedDecorators(linter))
