import os
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
def is_priem(getal):
    i = 2
    while i < getal and getal % i != 0:
        i = i + 1
    # Indien geen delers werden gevonden is i == getal
    return i == getal

def prev_priem(getal):
    getal -= 1
    if not is_priem(getal):
        getal -= 1
    return getal

ntests = 30
cases = [ (5,) ,(11,),(20,),(53,), (599,),(521,), (523,), (605,),(827,), (881,),(883,), (823,), (281,), (1873,)]

while len( cases ) < ntests:
    a = random.randint(2, 2000)
    if random.randint(0,3) != 0:
        if is_priem(a) and (a,) not in cases:
            cases.append( (a, ) )
        else:
            a = prev_priem(a)
            if (a,) not in cases:
                cases.append( (a,))
    else:
        if (a,) not in cases:
            cases.append( (a, ) )

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
            outputtxt += line
            
    testcase = { input: stdin, output: outputtxt }            
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
    
    # generate test expression
    
    expression_name = f"is_priem({test[0]})"
    result = module.is_priem(test[0])

    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
    
    expression_name = f"priemtweeling({test[0]})"
    result = module.priemtweeling(test[0])

    # setup for return expressions
    testcase = { "expression": expression_name, "stdout": outputtxt }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)

write_yaml(yamldata)
