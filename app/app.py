from flask import Flask, render_template, make_response
from flask_restful import Resource, Api
from flask_restful import reqparse
from markupsafe import escape

from definitions import ROOT_DIR
from solutions.allProblems import AllProblems

app = Flask(__name__, instance_path=f"/{ROOT_DIR}/app")
api = Api(app)


class CreateMain(Resource):
    def get(self):
        ap = AllProblems()
        template_problems = ap.divide_by_difficulty()
        return make_response(render_template("index.html", template_title='Home', template_problems=template_problems))

class CreateSolution(Resource):
    def get(self, num):
        try:
            # parser = reqparse.RequestParser()
            # parser.add_argument('problem_number', type=int)
            # args = parser.parse_args()
            # _problem_number = args['problem_number']

            with open(f'../solutions/problem{num}.py', 'r') as problem:
                problem_code = problem.read()
                return problem_code
        except IOError:
            return {'error': f'problem{num} was not loaded properly.'}


api.add_resource(CreateMain, '/')
api.add_resource(CreateSolution, '/solutions/<num>')

if __name__ == '__main__':
    app.run(debug=True)
