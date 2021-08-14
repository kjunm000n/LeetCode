
class ProblemInterface:
    def __init__(self, number, debug=False):
        self.problem_number = number
        self.debug=debug

    def solution(self, *args, **kwargs):
        raise Exception("solution is not implemented yet")

    def comparison_solution(self, nums1, nums2):
        raise Exception("comparison_solution is not implemented yet")

    def test_one(self, input, output):
        assert self.solution(**input) == output

    def test_with_cases(self, inputs, outputs):
        for input, output in zip(inputs, outputs):
            assert self.solution(**input) == output

    def test_runner(self):
        raise Exception("test_runner is not implemented yet")
