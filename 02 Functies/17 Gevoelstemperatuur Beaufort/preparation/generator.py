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

# generate tests
ntests= 20
cases = [(10.0,5.0, "km/u"), (3.0,5, "B")]
while len(cases) < ntests:
    T = round(random.uniform(-5,10), 1)
    if random.randint(0,1) == 0:
        W = round(random.uniform(0,45), 1)
        eenheid = "km/u"
    else:
        W = random.randint(0, 11)
        eenheid = "B"
    
    case = (T, W, eenheid)
    if case not in cases:
        cases.append( case )

   
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
    
    if test[2] == "km/u":
        # generate test expression
        expression_name = f"gevoelstemperatuur({test[0]}, {test[1]})"
        result = module.gevoelstemperatuur( test[0], test[1] )

        print(result)
        # setup for return expressions
        testcase = { "expression": expression_name, "return": result }
        yamldata[0]['contexts'][i]["testcases"].append( testcase)
    else:
        # generate test expression
        expression_name = f"gevoelstemperatuur_beaufort({test[0]}, {test[1]})"
        result = module.gevoelstemperatuur_beaufort( test[0], test[1] )

        print(result)
        # setup for return expressions
        testcase = { "expression": expression_name, "return": result }
        yamldata[0]['contexts'][i]["testcases"].append( testcase)
        
        # generate test expression
        expression_name = f"beaufort_naar_km_u({test[1]})"
        result = module.beaufort_naar_km_u( test[1] )

        print(result)
        # setup for return expressions
        testcase = { "expression": expression_name, "return": result }
        yamldata[0]['contexts'][i]["testcases"].append( testcase)
    

write_yaml(yamldata)
