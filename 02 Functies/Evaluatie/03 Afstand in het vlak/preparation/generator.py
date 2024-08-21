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

def transform( x1, y1, x2, y2, x3, y3 ):
    a = random.uniform(0, 2*math.pi)
    x_t = random.randint(-10,10)
    y_t = random.randint(-10,10)
    
    xa = round(x1 * math.cos(a) + y1*math.sin(a) + x_t, 2)
    ya = round(-x1 * math.sin(a) + y1*math.cos(a) + y_t, 2)
    xb = round(x2 * math.cos(a) + y2*math.sin(a) + x_t, 2)
    yb = round(-x2 * math.sin(a) + y2*math.cos(a) + y_t, 2)
    xc = round(x3 * math.cos(a) + y3*math.sin(a) + x_t, 2)
    yc = round(-x3 * math.sin(a) + y3*math.cos(a) + y_t, 2)
    
    return (xa, ya, xb, yb, xc, yc)

# generate test data
ntests = 20
cases = [(0.0,0.0,4.0,0.0,2.0,5.0), (0.0,0.0,4.0,0.0,2.0,3.46)]
while len(cases) < ntests:
    soort = random.randint(1,4)
    z = round(random.uniform(1,20), 1)
    if soort == 3: # gelijkzijdig
        xA = 0
        yA = 0
        xB = z
        yB = 0
        xC = z/2
        yC = z/2*math.sqrt(3)
    elif soort == 2: # gelijkbenig
        xA = 0
        yA = 0
        xB = z
        yB = 0
        xC = z/2
        yC = random.randint(1,10)
    else: # ongelijkbenig
        xA = 0
        yA = 0
        xB = z
        yB = 0
        xC = random.randint(1,10)
        yC = random.randint(1,10)
    
    cases.append( transform( xA, yA, xB, yB, xC, yC ) )

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
    x1 = test[0]
    y1 = test[1] 
    x2 = test[2]
    y2 = test[3]
    x3 = test[4]
    y3 = test[5]
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
    
    # generate test expression
    expression_name = f"afstand({x1}, {y1}, {x2}, {y2})"
    result = module.afstand(x1 , y1, x2, y2)

    print(result)
    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
    
    # generate test expression
    expression_name = f"afstand({x1}, {y1}, {x3}, {y3})"
    result = module.afstand( x1 , y1, x3, y3 )

    print(result)
    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
    
    # generate test expression
    expression_name = f"afstand({x2}, {y2}, {x3}, {y3})"
    result = module.afstand( x2 , y2, x3, y3 )

    print(result)
    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)

write_yaml(yamldata)
