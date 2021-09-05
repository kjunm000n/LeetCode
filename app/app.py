import sys
import re

from flask import Flask, render_template, make_response
from flask_restful import Resource, Api
from flask_restful import reqparse
from markupsafe import escape
from bs4 import BeautifulSoup

try:
    from definitions import ROOT_DIR
    from solutions.allProblems import AllProblems
except ImportError:
    sys.path.append('.')
    from definitions import ROOT_DIR
    from solutions.allProblems import AllProblems

app = Flask(__name__, instance_path=f"/{ROOT_DIR}/app")
api = Api(app)


class CreateMain(Resource):
    def get(self):
        ap = AllProblems()
        problems = ap.divide_by_difficulty()
        return make_response(
            render_template("index.html", easy=problems['Easy'], medium=problems['Medium'], hard=problems['Hard']))


class CreateSolution(Resource):
    def get(self, num):
        try:
            # parser = reqparse.RequestParser()
            # parser.add_argument('problem_number', type=int)
            # args = parser.parse_args()
            # _problem_number = args['problem_number']

            with open(f'../solutions/problem{num}.py', 'r') as problem:
                code = problem.read()
                name = re.findall("    name = '([0-9a-z\-]+)'", code)[0]
                return make_response(render_template("problem.html", num=num, name=name, code=code))
        except IOError:
            return {'error': f'problem{num} was not loaded properly.'}


api.add_resource(CreateMain, '/')
api.add_resource(CreateSolution, '/solutions/<num>.html')

if __name__ == '__main__':
    app.run(debug=True)
