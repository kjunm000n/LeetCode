import os

from solutions.allProblems import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    problem_number = os.getenv('problem_number')
    print(problem_number)
    ap = AllProblems(debug=True)
    prob = ap.get_problem(problem_number=problem_number)
    prob.test_one(input={'nums1':[6, 16, 26, 26, 27, 51, 58, 78], 'nums2':[10, 22, 49, 54, 63, 77]}, output=38)
    # prob.test_runner()

