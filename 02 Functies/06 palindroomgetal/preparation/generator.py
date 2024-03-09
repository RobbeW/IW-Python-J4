import os
import math
import sys
import importlib
import random
import ruamel.yaml
import subprocess
from io import StringIO 

yaml = ruamel.yaml.YAML()

# set fixed seed for generating test cases
random.seed(12345678)

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join('..', 'solution')
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

def write_yaml( data:list ):
    """ A function to write YAML file"""
    with open(os.path.join('..', 'evaluation', 'tests.yaml'), 'w', encoding='utf-8') as f:
        yaml.dump(data, f)

def construct_palindrome( a ):
    n = a // 2
    start = random.randint(10**(n-1), 10**(n)-1)
    orig = start
    nieuw = 0
    while start // 1 !=0:
        eenheid = start % 10
        nieuw = nieuw*10 + eenheid
        start //= 10

    print(a, orig, nieuw)
    return orig* (10**math.ceil(a/2)) + nieuw

# generate test data
ntests= 30
cases = [(1221,),(14541,),(13321,),(99,),(5,)]
while len(cases) < ntests:
    flag = random.randint(0,1)
    if flag == 1:
        test = construct_palindrome( random.randint(2,15) )
    else:
        test = random.randint(10,10**10)
    cases.append( (test,))

# generate unit tests for functions
yamldata = []

# input, expression, statement or stdin?
input = 'expression'
# output, stdout or return?
output = 'return'
tabtitle = "Functie feedback"

yamldata.append( {'tab': tabtitle, 'testcases': []})

module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.nl.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

for test in cases:
    # generate test expression
    expression_name = 'is_palindroom( {} )'.format( test[0])
    result = module.is_palindroom( test[0] )

    # setup for return expressions
    testcase = { input: expression_name, output: result}
    yamldata[0]['testcases'].append( testcase)

write_yaml(yamldata)
