# LeetCode
Personal solutions of LeetCode for algorithm study

All codes are based on Python 3.9.6

## Structure
|code|description|
|---|---|
|[definitions.py](definitions.py) | define global variables like root directory and list of solved problems |
|[allProblems.py](solutions/allProblems.py) |class for loading problem classes |
|[interface.py](solutions/interface.py) | parent class for problem each class |
|[sample.py](solutions/sample.py) | sample template of problem class |
|[test.py](solutions/test.py) | run solution code with pytest |

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

## Solved (26 problems)

### Easy (7 problems)
[1](solutions/problem1.py)
[7](solutions/problem7.py)
[9](solutions/problem9.py)
[13](solutions/problem13.py)
[14](solutions/problem14.py)
[69](solutions/problem69.py)
[367](solutions/problem367.py)

### Medium (18 problems)
[2](solutions/problem2.py)
[3](solutions/problem3.py)
[6](solutions/problem6.py)
[11](solutions/problem11.py)
[12](solutions/problem12.py)
[15](solutions/problem15.py)
[16](solutions/problem16.py)
[17](solutions/problem17.py)
[18](solutions/problem18.py)
[19](solutions/problem19.py)
[22](solutions/problem22.py)
[33](solutions/problem33.py)
[36](solutions/problem36.py)
[45](solutions/problem45.py)
[48](solutions/problem48.py)
[49](solutions/problem49.py)
[55](solutions/problem55.py)
[445](solutions/problem445.py)

### Hard (1 problems)
[214](solutions/problem214.py)

## Struggled
[4](solutions/problem4.py)
[5](solutions/problem5.py)
