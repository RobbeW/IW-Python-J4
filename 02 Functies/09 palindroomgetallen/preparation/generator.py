import os
import math
import importlib.util
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


module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.nl.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# generate test data
def is_palindroom(getal):
    oorspronkelijke = getal
    nieuw = getal % 10
    getal //= 10
    
    while getal != 0:
        eenheden = getal % 10
        getal //= 10
        nieuw = nieuw * 10 + eenheden
    
    return nieuw == oorspronkelijke

def prev_palindroom(getal):
    getal -= 1
    while not is_palindroom(getal):
        getal -= 1
    return getal

ntests = 20
cases = [(50,120), (14541, 17511), (0,10), (120,122), (88,99)]
while len(cases) < ntests:
    n = random.randint(0,6)
    getal = random.randint(10**n, 10**(n+1)-1)
    n = random.randint(1,4)
    toename = random.randint(10**n,(10**(n+1))-1)
    cases.append( (getal, getal+toename))

cases = sorted(cases, key = lambda x: x[1] - x[0])

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
    
    # generate test expression
    a = prev_palindroom(test[1])
    
    expression_name = f"is_palindroom({a})"
    result = module.is_palindroom(a)

    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
    
    if a != test[1]:
        expression_name = f"is_palindroom({test[1]})"
        result = module.is_palindroom(test[1])

        # setup for return expressions
        testcase = { "expression": expression_name, "return": result }
        yamldata[0]['contexts'][i]["testcases"].append( testcase)

write_yaml(yamldata)
