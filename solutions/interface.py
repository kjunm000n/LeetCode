import time
import functools
from typing import Optional, Union, Any, List, Tuple, Set, Dict
from enum import Enum


class ProblemInterface:
    def solution(self, *args, **kwargs):
        raise NotImplementedError

    def comparison_solution(self, *args, **kwargs):
        raise NotImplementedError

    def test_one(self, given_input: Dict[str, Any], expected_output: Any):
        my_output = self.solution(**given_input)
        print(f"output: {my_output}")
        assert my_output == expected_output

    def test_many_random(self, iteration=10):
        try:
            for _ in range(iteration):
                self.test_one_random()
        except TestFailedException:
            raise TestFailedException

    @staticmethod
    def print_func_input(func, args, kwargs):
        func_info = f"{func.__name__} ("
        for arg in args:
            if type(arg).__name__.startswith('Problem'):
                continue
            if not getattr(arg, '__repr__', None):
                func_info += 'non-str val, '
            else:
                func_info += str(arg) + ', ' if len(str(arg)) <= 100 else (str(arg)[:100] + '...') + ', '
        for kw, arg in kwargs.items():
            try:
                func_info += kw + ': ' + str(arg) + ', '
            except NameError:
                func_info += kw + ': non_str val, '
        func_info += f")"
        print(func_info, end='')

    @staticmethod
    def print_func_output(output):
        try:
            print(f' = {str(output) if len(str(output)) < 100 else str(output)[:100]}')
        except TypeError:
            print(' = output is not str convertable.')

    @staticmethod
    def print_func_runtime(func_name, st, et):
        print(f'{func_name} took {(et - st) / 10 ** 9:.6f}ms')

    @staticmethod
    def time_check(debug_mode=True):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if debug_mode:
                    ProblemInterface.print_func_input(func, args, kwargs)
                st = time.time_ns()
                return_val = func(*args, **kwargs)
                et = time.time_ns()
                if debug_mode:
                    ProblemInterface.print_func_output(return_val)
                    ProblemInterface.print_func_runtime(func.__name__, st, et)
                return return_val

            return wrapper

        return decorator


class TestFailedException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Difficulty(Enum):
    Easy = 0
    Medium = 1
    Hard = 2
