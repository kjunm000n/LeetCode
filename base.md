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
|comparison_solution|problemN.py|X|It's for comparison accuracy and efficiency. Sometimes, it ignores constraints of problems.|
|time_check|interface.py|X|It's used as decorator for checking elapsed time.|
|test_one|interface.py|X|This function compares the output from given input and the expected output.|
|test_one_random|problemN.py|X|From random input, compare the results of solution and comparison solution.|
|test_many|interface.py|X|It's similar as running test_one multiple times.|
|test_many_random|interface.py|X|It iterates test_one_random several times.|
|test_all|main.py|X|Run test_runner for each problem except problems in skip.|

## Environment Variable
- debug_mode: if it's True or 1, print time elapsed and results.
- problem_number: if it doesn't exist, then run all tests.
- ~~skip: specify number of problems to skip.~~
