from definitions import all_probs, struggled_probs
from solutions.allProblems import AllProblems


print("...generating readme.md...")

with open('base.md', 'r') as f_base:
    base_md = f_base.read()
    with open('readme.md', 'w') as f_readme:
        f_readme.write(base_md)

        ap = AllProblems()
        difficulty_dict = ap.divide_by_difficulty()

        # Solved
        f_readme.write(f'\n## Solved ({len(all_probs) - len(struggled_probs)} problems)\n')
        for difficulty, probs in difficulty_dict.items():
            f_readme.write(f'\n### {difficulty} ({len(probs)} problems)\n')
            for prob_num in probs:
                f_readme.write(f'[{prob_num}](solutions/problem{prob_num}.py)\n')

        # Struggled
        f_readme.write('\n## Struggled\n')
        for prob_num in struggled_probs:
            f_readme.write(f'[{prob_num}](solutions/problem{prob_num}.py)\n')

print("...readme.md was generated...")
