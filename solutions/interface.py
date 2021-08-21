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
                st = time.time_ns()
                return_val = func(*args, **kwargs)
                et = time.time_ns()
                if os.getenv('debug_mode'):
                    print(f"{func.__name__} tooks {(et-st)/10**9:.6f}ms")
                return return_val
            return wrapper
        return decorator
