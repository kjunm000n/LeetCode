import os

from solutions.allProblems import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    problem_number = os.getenv('problem_number')
    problem_number = 367
    print(f"Problem Number: {problem_number}")
    ap = AllProblems(debug=False)
    prob = ap.get_problem(problem_number=problem_number)
    # prob.test_one(given_input={'nums':[1,2,3], 'target':3},
    #               expected_output=[0,1])
    # prob.test_one_random()
    prob.test_runner()
    #
