import os
import importlib.util
import random
import ruamel.yaml
import subprocess
import math

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
ncases = 20
cases = [(5000, 200, 125, 50)]

while len(cases) < ncases:
    massa = random.randint(1,9) * 10**random.randint(3,4)
    aantal_nullen = math.floor(math.log10(massa))
    
    voeder = random.randint(1,9) * 10**random.randint(aantal_nullen-2, aantal_nullen - 1)
    
    oogst = random.randint(voeder//10, voeder)
    oogst = 5 * oogst // 5
    
    toename = random.randint(oogst // 10, oogst)
    toename = 5 * toename // 5
    case = (massa, voeder, oogst, toename)
    
    if case not in cases:
        cases.append(case)

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
    print(test)
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
        if not(line.startswith( 'Geef' ) or line.startswith( 'Voer' )):
            print(line)
            outputtxt += line + "\n"
            
    testcase = { input: stdin, output: outputtxt }            
    yamldata[0]['contexts'][i]["testcases"].append( testcase)

write_yaml(yamldata)