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
ntests= 20
choices = ["J", "N"]
cases = [(10.5, "N"),(10.5, "J", 4)]
while len(cases) < ntests:
    s = random.randint(5,21) * 0.5
    lang = random.choice(choices)
    if lang == "J":
        A = random.randint(1,6)
        case = (s, lang, A)
    else:
        case = (s, lang)
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
        if not(line.startswith('Geef') or line.startswith("Zal")):
            print(line)
            outputtxt += line
            
    testcase = { input: stdin, output: outputtxt }            
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
    
    if len(test) == 2:
        # generate test expression
        expression_name = f"hakhoogte({test[0]})"
        result = module.hakhoogte(test[0])
        
        print(result)
        # setup for return expressions
        testcase = { "expression": expression_name, "return": result }
        yamldata[0]['contexts'][i]["testcases"].append( testcase)
    else:
        # generate test expression
        expression_name = f"wankelfactor({test[2]})"
        wankel = module.wankelfactor(test[2])
        
        print(wankel)
        # setup for return expressions
        testcase = { "expression": expression_name, "return": wankel }
        yamldata[0]['contexts'][i]["testcases"].append( testcase)
        
        # generate test expression
        expression_name = f"hakhoogte({test[0]}, {wankel})"
        result = module.hakhoogte(test[0], wankel)
        
        print(result)
        # setup for return expressions
        testcase = { "expression": expression_name, "return": result }
        yamldata[0]['contexts'][i]["testcases"].append( testcase)
        


write_yaml(yamldata)
