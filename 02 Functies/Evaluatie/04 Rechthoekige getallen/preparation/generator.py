import os
import sys
import importlib.util
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
def is_rechthoekig(getal):
    i = 1
    while i * (i + 1) != getal and i < getal:
        i += 1
    return i != getal

def prev_rechthoekig(getal):
    getal -= 1
    while not is_rechthoekig(getal):
        getal -= 1
    return getal

cases = [(12,),(20,), (30,),(47,), (53,),(60,),(100,),(151,),(200,),(210,),(462,),(500,),(1000,)]

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
            outputtxt += line+"\n"
            print(line)
    
            
    testcase = { input: stdin, output: outputtxt }            
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
    
    getal = prev_rechthoekig(test[0])
    # generate test expression
    expression_name = f"is_rechthoekig({getal})"
    result = module.is_rechthoekig(getal)

    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
    
    # generate test expression
    expression_name = f"is_rechthoekig({test[0]})"
    result = module.is_rechthoekig(test[0])

    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)

write_yaml(yamldata)
