import sys

from flask_frozen import Freezer

from app import app
try:
    from definitions import all_probs, struggled_probs
except ImportError:
    sys.path.append('.')
    from definitions import all_probs, struggled_probs


freezer = Freezer(app)
freezer.app.config['FREEZER_REMOVE_EXTRA_FILES'] = False


@freezer.register_generator
def createsolution():
    for num in [problem for problem in all_probs if problem not in struggled_probs]:
        yield {'num': num}


if __name__ == '__main__':
    freezer.freeze()
