import os

from solutions.allProblems import AllProblems

class TestProblem:
    def test_problem_n(self, iteration=10):
        n = int(os.getenv('n'))
        iteration = int(os.getenv('iteration') or iteration)
        ap = AllProblems(probs=[n])
        prob = ap.get_problem(n)
        prob.test_many_random(iteration)

    def test_all(self, iteration=10):
        ap = AllProblems()
        iteration = int(os.getenv('iteration') or iteration)
        ap.test_all(iteration=iteration, keep_going=False)
