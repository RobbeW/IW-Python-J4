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
cases = [(5,),(10,),(11,),(29,),(30,),(47,), (53,),(60,),(100,),(151,),(200,),(500,),(1000,)]


# generate unit tests for functions
yamldata = []

# input, expression, statement or stdin?
input = 'stdin'
# output, stdout or return?
output = 'stdout'

yamldata.append( {'tab': 'Feedback', 'testcases': []})

for test in cases:
    # generate test expression
    # add input to input file
    stdin = '\n'.join(f'{line}' for line in test)

    # generate output to output file
    script = os.path.join(solutiondir, 'solution.nl.py')
    process= subprocess.run(
        ['python3', script],
        input=stdin,
        encoding='utf-8',
        capture_output=True
    )
    
    outputtxt = ""
    result_lines = process.stdout.split("\n")    
    for line in result_lines:
        if not(line.startswith( 'Geef' )):
            #print()
            outputtxt += line+"\n"
            print(line)
    
    # setup for return expressions
    testcase = { input: stdin, output: outputtxt[:-2] }
    yamldata[0]['testcases'].append( testcase)

write_yaml(yamldata)