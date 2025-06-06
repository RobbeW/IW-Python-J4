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
cases = [
    [".", "X", ".", "X", "."],
    [".", "X", ".", ".", ".", "X", "."],
    [".", "X", ".", ".", ".", ".", "X"],
    [".", "X", ".", ".", ".", ".", ".", "X"],
    [".", "X", ".", ".", ".", "X", ".", ".", ".", "."],
    [".", ".", ".", "X"]
]

choices = [".", "X"]

while len(cases) < ntests:
    e = random.randint(0, 3)
    n = random.randint(10**e, 10**(e+1))
    
    places = random.choices(choices, k = n)
    
    if places not in cases:
        cases.append(places)
    
cases = sorted(cases, key = lambda x: len(x))

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
    print("testcase:", test)
    yamldata[0]['contexts'].append( {'testcases' : []})
        
    # generate test expression
    #
    expression_name = f"aantal_links({test})"
    result = module.aantal_links(test)
    
    print(result)
    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)


write_yaml(yamldata)
