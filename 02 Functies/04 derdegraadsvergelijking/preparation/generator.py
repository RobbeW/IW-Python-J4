import os
import sys
import importlib
import random
import ruamel.yaml
import subprocess

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

# generate test data
ntests= 20
cases = [(-3,2),(1,2),(-4,0),(-27,54),(0,0)]
while len(cases) < ntests:
    item = tuple(random.randint(-50,50) for _ in range(2))
    if item[0] != 0 and item[1] != 0:
        cases.append( item )

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
    expression_name = 'discriminant( {} , {} )'.format( test[0] , test[1] )
    result = module.discriminant( test[0], test[1] )

    print(result)
    # setup for return expressions
    testcase = { input: expression_name, output: result }
    yamldata[0]['testcases'].append( testcase)

write_yaml(yamldata)
