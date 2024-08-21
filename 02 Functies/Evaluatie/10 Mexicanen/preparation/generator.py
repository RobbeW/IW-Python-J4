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
ntests = 40
cases = [(1,2,1,3), (3,3,2,1),(6,6,2,2),(4,2,2,4),(1,2,1,2)]
while len(cases) < ntests:
    case = tuple(random.randint(1,6) for _ in range(4))
    if case not in cases:
        cases.append(case)

# generate unit tests for functions
yamldata = []

# input, expression, statement or stdin?
tabtitle = "Feedback score"

yamldata.append( {'tab': tabtitle, 'contexts': []})

for i in range(len(cases)):
    test = cases[i]
    
    yamldata[0]['contexts'].append( {'testcases' : []})  
   
    expression_name = f"score({test[0]}, {test[1]})"
    result = module.score(test[0], test[1])

    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
    
    expression_name = f"score({test[2]}, {test[3]})"
    result = module.score(test[2], test[3])

    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
    


# input, expression, statement or stdin?
tabtitle = "Feedback mexen"

yamldata.append( {'tab': tabtitle, 'contexts': []})

for i in range(len(cases)):
    test = cases[i]
    
    yamldata[1]['contexts'].append( {'testcases' : []})  
   
    expression_name = f"mexen({test[0]}, {test[1]}, {test[2]}, {test[3]})"
    result = module.mexen(test[0], test[1], test[2], test[3])

    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[1]['contexts'][i]["testcases"].append( testcase)

write_yaml(yamldata)
