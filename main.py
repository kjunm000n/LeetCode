u"""
    Run Solution for LeetCode Problems
"""
import os
import sys
import argparse
from typing import Optional, Union, Any, List, Dict

sys.setrecursionlimit(100000)


# Parsing
def create_parser(initial_call=False):
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-p', '--problems', nargs='*', default=[], type=int,
                            help="This is problems to run. To run with input, only single problem should be entered."
                                 "\n If it's not set, then run random tests with all problem.")
    arg_parser.add_argument('-i', '--inputs', nargs='*', default=[], type=eval,
                            help="Each input should be form of dictionary."
                                 "If inputs are not set, random testcases will be run.\n"
                                 "ex) {'x':1234,'y':'c'} {'x':{'t':3},'y':'ac'}")
    arg_parser.add_argument('-o', '--outputs', nargs='*', default=[], type=eval,
                            help="Outputs should be matched with each inputs.\n"
                                 "ex) 1234 'xyz' {'x':31,'y':'qa'}")
    arg_parser.add_argument('-n', '--num', type=int, default=10,
                            help="The number of random test to run. Default value is 10 per each problem.")
    arg_parser.add_argument('-l', '--list', nargs='?', const=True, default=False, help="list available problems")
    if initial_call:
        arg_parser.add_argument('-d', '--debug_mode', nargs='?', const=True, help="print elapsed time and results.")
        arg_parser.add_argument('-s', '--skips', nargs='*', default=[], type=int,
                                help="Specify problems to skip, when test all.")
    arg_parser.add_argument('-e', '--exit', nargs='?', const=True, default=False, help="exit program")
    return arg_parser


parser = create_parser(initial_call=True)
args = parser.parse_args()
debug_mode = args.debug_mode is not None

# Getting Problems Info
all_probs = sorted([int(module[7:-3]) for module in os.listdir('solutions') if module.startswith('problem')])
struggled_probs = [4, 5, ]  # Not solved yet
skip_probs = args.skips
skip_probs = list(set(struggled_probs + skip_probs))

from solutions.allProblems import AllProblems


def main(parsed_args: Any):  # Namespace class
    ap = AllProblems(probs=parsed_args.problems or all_probs, skip_probs=skip_probs)
    if parsed_args.problems:
        if parsed_args.inputs:
            prob = ap.get_problem(problem_number=parsed_args.problems[0])
            for i, inp in enumerate(parsed_args.inputs):
                if parsed_args.outputs:
                    prob.test_one(given_input=get_input(inp, ap, parsed_args.problems[0]),
                                  expected_output=parsed_args.outputs[i])
                else:
                    prob.solution(**get_input(inp, ap, parsed_args.problems[0]))
        else:
            for prob_num in parsed_args.problems:
                ap.get_problem(problem_number=prob_num).test_many_random(iteration=parsed_args.num)
    else:
        ap.test_all(iteration=parsed_args.num)


def get_input(inp: Dict[str, Any], ap: AllProblems, prob_num: int) -> Dict[str, Any]:
    for k, v in inp.items():
        try:
            if type(v) == str and '(' in v and ')' in v:
                inp[k] = eval(v)
            else:
                inp[k] = v
        except (NameError, TypeError):
            try:
                cls_name, val = v.split('.')[-1].split('(')
                val = eval(val.replace(')', ''))
                inp[k] = getattr(getattr(ap.module_dict[prob_num], f'Problem{prob_num}'), cls_name)(val)
            except ImportError:
                raise ImportError
    return inp


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num_run = 0
    while True:
        if args.list:
            print(f'Available Problems: {all_probs}')
            sys.exit(0)
        if args.exit:
            sys.exit(0)
        if args.inputs and len(args.problems) >= 2:
            raise ValueError
        if args.outputs and len(args.inputs) != len(args.outputs):
            raise ValueError
        if not set(args.problems).issubset(set(all_probs)):
            raise ValueError
        main(args)
        input_str = input().split()
        args = create_parser().parse_args(args=input_str)
