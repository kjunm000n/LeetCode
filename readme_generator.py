import main
from main import skip_probs, debug_mode
from solutions.allProblems import AllProblems
import os

if os.getenv('debug_mode'):
    print("generating readme.md...")
with open('base.md', 'r') as f_base:

    base_md = f_base.read()
    with open('readme.md', 'w') as f_readme:
        f_readme.write(base_md)

        ap = AllProblems()
        all_probs = sorted([int(module.replace('problem', '')) for module in ap.module_dict.keys()])

        # Solved
        f_readme.write('\n## Solved\n')
        for prob_num in all_probs:
            if prob_num in skip_probs:
                continue
            else:
                f_readme.write(f'[{prob_num}](solutions/problem{prob_num}.py)\n')

        # Struggled
        f_readme.write('\n## Struggled\n')
        for prob_num in skip_probs:
            f_readme.write(f'[{prob_num}](solutions/problem{prob_num}.py)\n')

if os.getenv('debug_mode'):
    print("readme.md was generated")
