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


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

# generate test data
ntests= 30
cases = [(5,),(11,),(20,),(53,)]
while len(cases) < ntests:
    test = random.randint(2,1000)
    cases.append( (test,))

# generate unit tests for functions
yamldata = []

# input, expression, statement or stdin?
input = 'expression'
# output, stdout or return?
output = 'stdout'
tabtitle = "Functie feedback"

yamldata.append( {'tab': tabtitle, 'testcases': []})

module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.nl.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

for test in cases:
    # generate test expression
    expression_name = 'priemtweeling( {} )'.format( test[0])
    
    with Capturing() as captured:
        result = module.priemtweeling( test[0] )
    
    print(captured)
    

    # setup for return expressions
    testcase = { input: expression_name, output: captured[0]}
    yamldata[0]['testcases'].append( testcase)

write_yaml(yamldata)
