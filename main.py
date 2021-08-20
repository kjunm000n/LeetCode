import os, sys

sys.setrecursionlimit(100000)
debug_mode = os.getenv('debug_mode') in [1, True]
problem_number = os.getenv('problem_number')
skip_probs = [4, ]  # Not solved yet

from solutions.allProblems import AllProblems

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    problem_number = 7
    debug_mode = True
    ap = AllProblems()
    prob = ap.get_problem(problem_number=problem_number)
    print(f"Problem Number: {problem_number}")
    # prob.solution(51434)
    # prob.comparison_solution(33251)
    # prob.comparison_solution2(2323)
    # prob.test_one(given_input={'x':[1,2,3], 'target':3},
    #               expected_output=[0,1])
    # prob.test_one_random()
    # prob.test_runner()


def test_all(keep_going=True):
    ap = AllProblems(initialize_all=True, skip_probs=[4])
    for prob_name, prob in ap.probs.items():
        try:
            if debug_mode:
                print(f"{prob_name} is running")
            prob.test_runner()
        except:
            print(f"{prob_name} failed")
            if not keep_going:
                assert False
        else:
            if debug_mode:
                print(f"{prob_name} passed")
