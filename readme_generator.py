import main
from main import all_probs, struggled_probs, debug_mode
from solutions.allProblems import AllProblems
import os

if debug_mode:
    print("generating readme.md...")
with open('base.md', 'r') as f_base:

    base_md = f_base.read()
    with open('readme.md', 'w') as f_readme:
        f_readme.write(base_md)

        ap = AllProblems()

        # Solved
        f_readme.write('\n## Solved\n')
        for prob_num in filter(lambda x: x not in struggled_probs, all_probs):
            f_readme.write(f'[{prob_num}](solutions/problem{prob_num}.py)\n')

        # Struggled
        f_readme.write('\n## Struggled\n')
        for prob_num in struggled_probs:
            f_readme.write(f'[{prob_num}](solutions/problem{prob_num}.py)\n')

if debug_mode:
    print("readme.md was generated")
