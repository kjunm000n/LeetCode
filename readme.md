# LeetCode
Personal solutions of LeetCode for algorithm study

## Structure
[allProblems.py](solutions/allProblems.py) : class for loading problem classes <br>
[interface.py](solutions/interface.py) : parent class for problem each class <br>
[sample.py](solutions/sample.py) : sample template of problem class

### common methods
|name|location|Nullable|description|
|---|---|---|---|
|solution|problemN.py|X|My personal solution and it could be wrong.|
|comparison_solution|problemN.py|O|It's for comparison accuracy and efficiency. Sometimes, it ignores constraints of problems.|
|time_check|interface.py|X|It's used as decorator for checking elapsed time.|
|test_one|interface.py|X|This function compares the output from given input and the expected output.|
|test_one_random|problemN.py|X|From random input, compare the results of solution and comparison solution.|
|test_many_random|interface.py|X|It iterates test_one_random several times.|
|test_all|allProblem.py|X|Run test_runner for each problem except problems in skip.|

## Usage
```shell
usage: main.py [-h] [-p [PROBLEMS [PROBLEMS ...]]] [-i [INPUTS [INPUTS ...]]] [-o [OUTPUTS [OUTPUTS ...]]] [-n NUM] [-l [LIST]] [-d [DEBUG_MODE]] [-s [SKIPS [SKIPS ...]]] [-e [EXIT]]

optional arguments:
  -h, --help            show this help message and exit
  -p [PROBLEMS [PROBLEMS ...]], --problems [PROBLEMS [PROBLEMS ...]]
                        This is problems to run. To run with input, only single problem should be entered. If it's not set, then run random tests with all problem.
  -i [INPUTS [INPUTS ...]], --inputs [INPUTS [INPUTS ...]]
                        Each input should be form of dictionary. If inputs are not set, random testcases will be runned. ex) "{'x':1234,'y':'c'} {'x':{'t':3},'y':'ac'}"
  -o [OUTPUTS [OUTPUTS ...]], --outputs [OUTPUTS [OUTPUTS ...]]
                        Outputs should be matched with each inputs. ex) "1234 'xyz' {'x':31,'y':'qa'}"
  -n NUM, --num NUM     The number of random test to run. Default value is 10 per each problem.
  -l [LIST], --list [LIST]
                        list available problems
  -d [DEBUG_MODE], --debug_mode [DEBUG_MODE]
                        print elapsed time and results.
  -s [SKIPS [SKIPS ...]], --skips [SKIPS [SKIPS ...]]
                        Specify problems to skip, when test all.
  -e [EXIT], --exit [EXIT]
                        exit program
```

## Solved
[1](solutions/problem1.py)
[2](solutions/problem2.py)
[3](solutions/problem3.py)
[6](solutions/problem6.py)
[7](solutions/problem7.py)
[69](solutions/problem69.py)
[214](solutions/problem214.py)
[367](solutions/problem367.py)
[445](solutions/problem445.py)

## Struggled
[4](solutions/problem4.py)
[5](solutions/problem5.py)
