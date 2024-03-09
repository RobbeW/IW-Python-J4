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
ntests = 20
cases = [ (100,120),(128,26)]

while len( cases ) < ntests:
    a = random.randint(1, 200)
    b = random.randint(1, 200)
    cases.append( (a, b) )
    
# generate unit tests for functions
yamldata = []

# input, expression, statement or stdin?
input = 'stdin'
# output, stdout or return?
output = 'stdout'
tabtitle = "Invoer/uitvoer feedback"

yamldata.append( {'tab': tabtitle, 'testcases': []})

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
    
    result_lines = process.stdout.split("\n")
    result_lines = [x for x in result_lines[:-1]] ## drop last element
    
    outputtxt = ""
    for line in result_lines:
        if not(line.startswith( 'Geef' )):
            print(line)
            outputtxt += line
    
    # setup for return expressions
    testcase = { input: stdin, output: outputtxt }
    yamldata[0]['testcases'].append( testcase)

# input, expression, statement or stdin?
input = 'expression'
# output, stdout or return?
output = 'return'
tabtitle = "Functie harmonisch_gemiddelde feedback"

yamldata.append( {'tab': tabtitle, 'testcases': []})

print(yamldata[1])

module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.nl.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

for test in cases:
    # generate test expression
    expression_name = 'harmonisch_gemiddelde( {} , {} )'.format( test[0] , test[1] )
    result = module.harmonisch_gemiddelde( test[0], test[1] )

    print(result)
    # setup for return expressions
    testcase = { input: expression_name, output: result }
    yamldata[1]['testcases'].append( testcase)

write_yaml(yamldata)
