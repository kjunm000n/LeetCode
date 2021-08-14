import os, sys

try:
    problem_modules = [module[:-3] for module in os.listdir(os.path.dirname(__file__)) if module.startswith('problem')]
    modules_dict = {}
    for problem_module in problem_modules:
        solutions = __import__(f'solutions.{problem_module}')
        module = getattr(solutions, problem_module)
        modules_dict[problem_module] = getattr(solutions, problem_module)
except ImportError:
    raise Exception("Import Failed")
else:
    del problem_module

class AllProblems:
    def __init__(self, debug=False):
        self.module_dict = modules_dict
        self.probs = {}
        self.debug = debug

    def get_problem(self, problem_number=4):
        module_name, class_name = f'problem{problem_number}', f'Problem{problem_number}'
        if module_name in self.probs:
            return self.probs['module_name']
        if module_name not in self.module_dict:
            raise Exception(f"Problem {problem_number} doesn't exists")
        prob_class = getattr(self.module_dict[module_name], class_name)
        problem = prob_class()
        self.probs[module_name] = problem
        return problem
