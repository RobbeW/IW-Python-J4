import os
import sys
import importlib
import random
import ruamel.yaml
import subprocess
from io import StringIO 


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

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


# generate test data
ntests= 20
cases = [([1, 2, 3, 4, 1, 6], 3), ([1, 2, 3, 4, 1, 6], 6)]
while len(cases) < ntests:
    n = random.randint(3,50)
    lijst = list( random.randint(0,150) for _ in range(n) )
    getal = random.randint(0,150)
    cases.append( (lijst, getal))

    
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
    expression_name = f"groter_dan( {test[0]}, {test[1]} )"
    
    with Capturing() as output:
        result = module.groter_dan( test[0], test[1] )

    outputtxt = ""
    for txt in output:
        outputtxt += txt+ "\n"
    
    print(result)

    # setup for return expressions
    testcase = { "expression": expression_name, "stdout": outputtxt, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)

write_yaml(yamldata)
