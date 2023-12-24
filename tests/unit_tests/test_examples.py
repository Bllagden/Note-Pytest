from contextlib import nullcontext as does_not_raise

import pytest

from examples import A, Calculator


def test_a():
    assert A.x == 1


class TestCalculator:
    """Способы запуска:
    pytest tests/unit_tests/test_examples.py -v
    pytest tests/unit_tests/test_examples.py::TestCalculator -v
    pytest tests/unit_tests/test_examples.py::TestCalculator::test_calculator_divide -v
    pytest tests/unit_tests/test_examples.py::TestCalculator::test_calculator_add -v

    флаг -v (для вывода подробностей)

    pytest.raises - контекстный менеджер для проверки, поднимается ли определенное исключение.
    does_not_raise (nullcontext) - контекстный менеджер, который ничего не делает.
    Таким образом достигается корректное исполнение тестов с правильными и неправильными
    входными данными.
    """

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, 0.5, does_not_raise()),
            (5, -1, -5, does_not_raise()),
            (5, "-1", -5, pytest.raises(TypeError)),
            (5, 0, 5, pytest.raises(ZeroDivisionError)),
        ],
    )
    def test_calculator_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, 3, does_not_raise()),
            (5, -1, 4, does_not_raise()),
            ("5", -1, 4, pytest.raises(TypeError)),
            (5, "-1", 4, pytest.raises(TypeError)),
        ],
    )
    def test_calculator_add(self, x, y, res, expectation):
        with expectation:
            assert Calculator().add(x, y) == res
