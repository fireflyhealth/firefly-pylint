import astroid
from pylint.testutils import CheckerTestCase, MessageTest

from firefly_pylint.lint_checkers.deprecated_decorators import (
    StdlibCheckerWithAdditionalDeprecatedDecorators,
)


class TestDeprecatedDecoratorChecker(CheckerTestCase):
    CHECKER_CLASS = StdlibCheckerWithAdditionalDeprecatedDecorators

    def test_unrelated_decorators_do_not_trigger_linter(self):
        node = astroid.extract_node(
            """
                call_something()
            """
        )

        with self.assertNoMessages():
            self.checker.visit_call(node)

    def test_atomic_decorators_trigger_linter(self):
        node = astroid.extract_node(
            """
        from django.db import transaction

        @transaction.atomic #@
        def function():
            pass
        """
        )

        with self.assertAddsMessages(
            MessageTest(
                msg_id="deprecated-decorator",
                node=node,
                args="django.db.transaction.atomic",
                line=4,
                col_offset=0,
                end_line=None,
                end_col_offset=None,
            ),
        ):
            self.checker.visit_decorators(node)
