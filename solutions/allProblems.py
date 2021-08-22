import os

from solutions.interface import TestFailedException

def import_problems(probs, skip_probs):
    try:
        module_dict = {}
        for prob_num in [prob_num for prob_num in probs if prob_num not in skip_probs]:
            solutions = __import__(f'solutions.problem{prob_num}')
            module_dict[prob_num] = getattr(solutions, f'problem{prob_num}')
    except ImportError:
        raise ImportError
    return module_dict


class AllProblems:
    def __init__(self, probs=[], skip_probs=[]):
        self.module_dict = import_problems(probs=probs, skip_probs=skip_probs)
        self.probs = {}
        self.get_all_problems(all_probs=probs, skip_probs=skip_probs)

    def get_problem(self, problem_number):
        class_name = f'Problem{problem_number}'
        if problem_number in self.probs:
            return self.probs[problem_number]
        if problem_number not in self.module_dict:
            raise ModuleNotFoundError
        prob_class = getattr(self.module_dict[problem_number], class_name)
        prob_instance = prob_class()
        self.probs[problem_number] = prob_instance
        return prob_instance

    def get_all_problems(self):
        for proble_number, module in self.module_dict.items():
            class_name = f'Problem{proble_number}'
            prob_class = getattr(module, class_name)
            prob_instance = prob_class()
            self.probs[proble_number] = prob_instance
        return self.probs

    def test_all(self, iteration=10, keep_going=True):
        passed, failed = [], []
        for prob_num, prob in self.probs.items():
            try:
                print(f"Problem {prob_num} is running")
                prob.test_many_random(iteration=iteration)
            except TestFailedException:
                failed.append(prob_num)
                print(f"Problem {prob_num} failed")
                if not keep_going:
                    assert False
            else:
                passed.append(prob_num)
                print(f"Problem {prob_num} passed")
        print(f"Pass: {passed} / Fail: {failed}")
        return passed, failed
