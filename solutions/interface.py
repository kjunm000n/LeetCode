
class ProblemInterface:
    def solution(self, *args, **kwargs):
        raise Exception("solution is not implemented yet")

    def comparison_solution(self, nums1, nums2):
        raise Exception("comparison_solution is not implemented yet")

    def test_one(self, given_input, expected_output):
        my_output = self.solution(**given_input)
        print(f"output: {my_output}")
        assert my_output == expected_output

    def test_runner(self, iteration=1000):
        try:
            for _ in range(iteration):
                self.test_one_random()
        except:
            raise Exception("test_runner is not implemented yet")
