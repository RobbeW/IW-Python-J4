import os
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

# generate test data
def is_priem( getal ):
    priem = True
    for i in range(2, getal):
        if getal % i == 0:
            priem = False
    
    return priem

def prev_priem(getal):
    getal -= 1
    while not is_priem(getal):
        getal -= 1
    return getal

def prev_sgpriem(getal):
    getal -= 1
    while (not is_priem(getal) or not is_priem(2* getal +1)) and getal > 2:
        getal -= 1
    return getal

ntests = 30
cases = [(7,), (4, ), (11,) ]
while len(cases) < ntests:
    e = random.randint(0,5)
    n = random.randint(10**e, 10**(e+1))
    if (temp := random.randint(0,2)) == 0:
        n = prev_sgpriem(n)
    elif temp == 1:
        n = prev_priem(n)
    
    if (n,) not in cases:
        cases.append( (n,))

cases.sort()

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
            outputtxt += f"{line}\n"
            
    testcase = { input: stdin, output: outputtxt }            
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
    
   
    expression_name = f"is_priem({test[0]})"
    result = module.is_priem(test[0])

    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
    
    expression_name = f"is_germainpriem({test[0]})"
    result = module.is_germainpriem(test[0])

    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
   
write_yaml(yamldata)
