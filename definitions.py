import os
import argparse

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--debug_mode', nargs='?', const=True, help="print elapsed time and results.")
args, unknown = parser.parse_known_args()
debug_mode = os.getenv('debug_mode') or args.debug_mode or False

all_probs = sorted([int(module[7:-3]) for module in os.listdir(f'{ROOT_DIR}/solutions') if module.startswith('problem')])
struggled_probs = [4, 5, ]  # Not solved yet
