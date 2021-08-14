import os

from solutions.allProblems import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    problem_number = os.getenv('problem_number')
    print(problem_number)
    ap = AllProblems()
    prob = ap.get_problem(problem_number=problem_number)
    prob.test_runner()

