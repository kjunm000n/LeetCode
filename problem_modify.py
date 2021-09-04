from solutions.allProblems import AllProblems
from solutions.interface import ProblemInterface

ap = AllProblems()
difficulty_dict = ap.divide_by_difficulty()

for difficulty, probs in difficulty_dict.items():
    for prob_num in probs:
        with open(f'solutions/problem{prob_num}.py', 'r') as f_prob:
            code = f_prob.read()
        first_line = code.split('\n')[0]
        title = ProblemInterface.title_to_name(first_line.split('] ')[1])
        code = code.replace(f'difficulty = Difficulty.{difficulty}',
                            f"difficulty = Difficulty.{difficulty}\n    name = '{title}'")
        with open(f'solutions/problem{prob_num}.py', 'w') as f_prob:
            f_prob.write(code)
