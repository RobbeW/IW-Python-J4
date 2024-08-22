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
ntests = 38
cases = [(9425,),(7,)]
while len(cases) < ntests:
    e = random.randint(0,5)
    n = random.randint(10*e, 10**(e+1))
    n = max(3, n)
    case = (n, )
    if case not in cases:
        cases.append(case)

cases.sort()

# generate unit tests for functions
yamldata = []

# Generate first tab
tabtitle = "Feedback volgende_priem"

yamldata.append( {'tab': tabtitle, 'contexts': []})

for i in range(len(cases)):
    test = cases[i]
    yamldata[0]['contexts'].append( {'testcases' : []})
    
    # setup for return expressions    
    expression_name = f"volgende_priem({test[0]})"
    result = module.volgende_priem(test[0])

    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
    
# Generate second tab
tabtitle = "Feedback is_priem"

yamldata.append( {'tab': tabtitle, 'contexts': []})

for i in range(len(cases)):
    test = cases[i]
    yamldata[1]['contexts'].append( {'testcases' : []})
    
    # setup for return expressions    
    expression_name = f"is_priem({test[0]})"
    result = module.is_priem(test[0])

    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[1]['contexts'][i]["testcases"].append( testcase)

write_yaml(yamldata)