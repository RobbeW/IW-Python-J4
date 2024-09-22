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
ntests= 24
cases = [([1, 2, 3, 4, 5, 6, 7, 8, 9], 4), ([9, 8, 7, 6, 5, 4, 3, 2, 1], 3), ([1, 2, 3, 4, 5], 1) ]
while len(cases) < ntests:
    e = random.randint(1,4)
    n = random.randint(10**e, 10**(e + 1))
    n = min(n, 10000)
    lijst = list( random.randint(10,100) for _ in range(n) )
    a = random.randint(1,n // 2)
    if (lijst, a) not in cases:
        cases.append( (lijst, a) )

lijst = list( random.randint(10,100) for _ in range(80000) )
a = 6000
cases.append( (lijst, a) )

cases = sorted(cases, key = lambda x: len(x[0]))


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
    #
    expression_name = f"opbrengst({test[0]}, {test[1]})"
    result = module.opbrengst(test[0], test[1])

    print(result)
    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)

write_yaml(yamldata)
