# mainlib.py
import sys


def Main(func):
    """
    A decorator to mark the main entry point of a script.
    Executes the decorated function only if __name__ == "__main__".
    """
    if sys.modules["__main__"].__file__ == func.__globals__["__file__"]:
        func()
    return func


def Override(func):
    def wrapped_method(*args, **kwargs):
        # Check if the method belongs to a class and overrides a parent method
        clsargs = args[0].__class__  # Access the class of the first argument (usually `self`)
        parent_methods = {attr for base in clsargs.__bases__ for attr in dir(base)}
        if func.__name__ not in parent_methods:
            raise TypeError(
                f"Method '{func.__name__}' does not override any method in the parent class."
            )
        return func(*args, **kwargs)  # Call the original method
    return wrapped_method
