import os
import importlib.util
import random
import ruamel.yaml

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
cases = [([-2, 0, 1, 3, 5, 2, 4], 0, 3),
         ([-2, 0, 1, 3, 5, 2, 4], -5, -3),
         ([-2, 0, 1, 3, 5, 2, 4], 0, 0)]

while len(cases) < ntests:
    e = random.randint(0,3)
    n = random.randint(10**e,10**(e+1))
    
    lijst = [random.randint(-50, 50) for _ in range(n)]
    
    a = random.randint(-50,50)
    b = random.randint(-50,50)
    
    test = (lijst, min(a, b), max(a,b))
    
    if test not in cases:
        cases.append(test)

cases = sorted(cases, key = lambda x : len(x[0]))

# generate unit tests for functions
yamldata = []

# new tab
tabtitle = "Feedback"

yamldata.append( {'tab': tabtitle, 'contexts': []})

for i in range(len(cases)):
    test = cases[i]
    yamldata[0]['contexts'].append( {'testcases' : []})
        
    # generate test expression
    #
    expression_name = f"aantal_tussen({test[0]}, {test[1]}, {test[2]})"
    result = module.aantal_tussen(test[0], test[1], test[2])

    print(result)
    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)

write_yaml(yamldata)
