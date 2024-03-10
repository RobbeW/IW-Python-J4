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
cases = [(2,3,4),(5,2,3),(8,9,8),(8,8,8)]
while len(cases) < ntests:
    a = random.randint(-10,20)
    b = random.randint(-10,20)
    c = random.randint(-10,20)
    cases.append( (a,b,c))

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
    expression_name = 'midden( {}, {}, {} )'.format( test[0],test[1],test[2])
    result = module.midden( test[0],test[1],test[2] )

    # setup for return expressions
    testcase = { input: expression_name, output: result}
    yamldata[0]['testcases'].append( testcase)

write_yaml(yamldata)
