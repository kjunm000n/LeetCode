import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--num', default=0, type=int, help="problem number to generate sample.py")
args = parser.parse_args()
num = args.num
while not num:
    print('please enter the problem number to generate skeleton: ', end='')
    num = input()
    if num.isdigit():
        num = int(num)
    else:
        print("problem number isn't number")

print(f"...generating solutions/problem{num}.py...")
sample_path = 'solutions/sample.py'
problem_path = f'solutions/problem{num}.py'

if not os.path.exists(sample_path):
    print("sample.py doesn't exist")
    exit(-1)
if os.path.exists(problem_path):
    print("problem.py already exists")
    exit(-1)

with open(sample_path, 'r') as f_sample:
    sample = f_sample.read()
    sample = sample.replace('[N]', f'[{num}]')
    sample = sample.replace('ProblemN(ProblemInterface)', f'Problem{num}(ProblemInterface)')
    title = None
    while not title:
        print('please enter the title of the problem.')
        title = input()
    difficulty = None
    while not difficulty:
        print('please enter the difficulty of problem (Easy, Medium, Hard or 1,2,3)')
        difficulty = input()
        if difficulty.isalpha():
            if difficulty.lower() == 'easy':
                break
            elif difficulty.lower() == 'medium':
                sample = sample.replace('Difficulty.Easy', 'Difficulty.Medium')
                break
            elif difficulty.lower() == 'hard':
                sample = sample.replace('Difficulty.Easy', 'Difficulty.Hard')
                break
            else:
                difficulty = None
        if difficulty.isdigit():
            difficulty = int(difficulty)
            if difficulty == 1:
                break
            elif difficulty == 2:
                sample = sample.replace('Difficulty.Easy', 'Difficulty.Medium')
                break
            elif difficulty == 3:
                sample = sample.replace('Difficulty.Easy', 'Difficulty.Hard')
                break
            else:
                difficulty = None
    sample = sample.replace('**Sample Text**', title)

    with open(problem_path, 'w') as f_problem:
        f_problem.write(sample)

print("...readme.md was generated...")
