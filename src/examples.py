def assert_example():
    x = "hello"
    assert x == "hello", "x не равен 'hello'"  # ничего не происходит
    assert x == "goodbye", "x не равен 'hello'"  # AssertionError с сообщением


class A:
    x = 1


class Calculator:
    def divide(self, x: int | float, y: int | float) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Arg_types must be int or float")
        if y == 0:
            raise ZeroDivisionError("Second_arg should not be zero")
        return x / y

    def add(self, x: int | float, y: int | float) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Arg_types must be int or float")
        return x + y


if __name__ == "__main__":
    calculator = Calculator()
