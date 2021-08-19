import os, sys

try:
    problem_modules = [module[:-3] for module in os.listdir(os.path.dirname(__file__)) if module.startswith('problem')]
    module_dict = {}
    for problem_module in problem_modules:
        solutions = __import__(f'solutions.{problem_module}')
        module = getattr(solutions, problem_module)
        module_dict[problem_module] = getattr(solutions, problem_module)
except ImportError:
    raise Exception("Import Failed")
else:
    del problem_modules

class AllProblems:
    def __init__(self, initialize_all=False, skip_probs=[]):
        self.module_dict = module_dict
        self.probs = {}
        if initialize_all:
            self.get_all_problems(skip_probs=skip_probs)

    def get_problem(self, problem_number):
        module_name, class_name = f'problem{problem_number}', f'Problem{problem_number}'
        if module_name in self.probs:
            return self.probs['module_name']
        if module_name not in self.module_dict:
            raise Exception(f"Problem {problem_number} doesn't exists")
        prob_class = getattr(self.module_dict[module_name], class_name)
        prob_instance = prob_class()
        self.probs[module_name] = prob_instance
        return prob_instance

    def get_all_problems(self, skip_probs=[]):
        for module_name, module in self.module_dict.items():
            if int(module_name.replace('problem', '')) in skip_probs:
                continue
            class_name = module_name.replace('problem','Problem')
            prob_class = getattr(module, class_name)
            prob_instance = prob_class()
            self.probs[module_name] = prob_instance
        return self.probs
