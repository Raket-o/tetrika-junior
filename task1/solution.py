from functools import wraps
from typing import Callable, Any


def strict(func: Callable) -> Callable:
    """
    Decorator for strict type checking of arguments.
    """
    annotations = func.__annotations__

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """
        The wrapper checks the annotation of types and
        passed arguments of arguments, if there are
        discrepancies, returns raise TypeError().
        """
        for i, arg in enumerate(args):
            param_name = list(annotations.keys())[i]
            annotation_type = annotations.get(param_name)
            val_type = type(arg)
            if annotation_type != val_type:
                raise TypeError()

        for key, value in kwargs.items():
            annotation_type = annotations.get(key)
            val_type = type(value)
            if annotation_type != val_type:
                raise TypeError()

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    """
    The function of adding two numbers.
    """
    return a + b


if __name__ == "__main__":
    print(sum_two(1, 2))  # >>> 3
    print(sum_two(1, 2.4))  # >>> TypeError
