import os
import math
import sys
import importlib.util
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


module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.nl.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

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
ntests = 20
cases = [(10.0,),(100.5,),(2,),(11,),(23.8,),(22.9,)]
while len(cases) < ntests:
    exp = random.randint(1,4)
    if exp == 1:
        getal = round(random.uniform(2,10), 1)
    else:
        getal = round(random.uniform(10**(exp-1),10**exp), 1)
    if (getal,) not in cases:
        cases.append((getal,))

cases.sort()

def is_priem( getal ):
    priem = True
    for i in range(2, getal):
        if getal % i == 0:
            priem = False
    
    return priem

def find_prev_prime( getal ):
    getal_n = math.floor(getal)
    if isinstance(getal, float) and is_priem(getal_n):
        getal = getal_n+1
    else:
        getal = getal_n
        flag = True
        while not is_priem(getal - 1):
            getal -= 1
    return getal -1

# generate unit tests for functions
yamldata = []

# input, expression, statement or stdin?
input = 'stdin'
# output, stdout or return?
output = 'stdout'
tabtitle = "Feedback"

yamldata.append( {'tab': tabtitle, 'contexts': []})

for i in range(len(cases)):
    test = cases[i]
    yamldata[0]['contexts'].append( {'testcases' : []})
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
    
    result_lines = process.stdout.split("\n")
    result_lines = [x for x in result_lines[:-1]] ## drop last element
    
    outputtxt = ""
    for line in result_lines:
        if not(line.startswith( 'Geef' )):
            print(line)
            outputtxt += line
            
    testcase = { input: stdin, output: outputtxt }            
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
    
    expression_name = f"telpriem({test[0]})"
    result = module.telpriem(test[0])

    print(result)
    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
    
    #check primes
    getal = test[0]
    count = min(result, 4)
    for j in range(count):
        getal = find_prev_prime(getal)
        
        expression_name = f"is_priem({getal})"
        result = module.is_priem( getal )

        print(result)
        # setup for return expressions
        testcase = { "expression": expression_name, "return": result }
        yamldata[0]['contexts'][i]["testcases"].append( testcase)
    
write_yaml(yamldata)
