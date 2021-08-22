import os
import time
import functools

from main import debug_mode

class ProblemInterface:
    def solution(self, *args, **kwargs):
        raise Exception("solution is not implemented yet")

    def comparison_solution(self, nums1, nums2):
        raise Exception("comparison_solution is not implemented yet")

    def test_one(self, given_input, expected_output):
        my_output = self.solution(**given_input)
        print(f"output: {my_output}")
        assert my_output == expected_output

    def test_many_random(self, iteration=10):
        try:
            for _ in range(iteration):
                self.test_one_random()
        except:
            raise Exception("test failed")

    @staticmethod
    def time_check(debug_mode=True):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if os.getenv('debug_mode'):
                    func_info = f"{func.__name__} ("
                    for arg in args:
                        if type(arg).__name__.startswith('Problem'):
                            continue
                        if not getattr(arg, '__repr__', None):
                            func_info += 'non-str val, '
                        else:
                            func_info += str(arg) if len(str(arg)) <= 100 else (str(arg)[:100] + '...') + ', '
                    for kw, arg in kwargs.items():
                        func_info += kw + ': ' + arg + ', '
                    func_info += f")"
                    print(func_info, end='')
                st = time.time_ns()
                return_val = func(*args, **kwargs)
                et = time.time_ns()
                if os.getenv('debug_mode'):
                    try:
                        print(f' = {str(return_val) if len(str(return_val)) < 100 else str(return_val)[:100]}')
                    except:
                        print(' = output is not str convertable.')
                    print(f'{func.__name__} tooks {(et-st)/10**9:.6f}ms')
                return return_val
            return wrapper
        return decorator
