import os
import sys
import importlib
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

names = ["Cédric", "Luiz", "Ward", "Briek", "Miel", "Menno", "Alice", "Andreas","Ishita", 
         "Eben", "Arend", "Joppe", "Veronika", "Lieze", "Kristina", "Cristina", "Lisa", 
         "Daan", "Ana", "Lous", "Maarte","Hanne", "Arnaud", "Rosie Lou", "Lasse", "Marcel",
         "Calin", "Xander", "Tiemen", "Faris", "Ruben", "Manu", "Bolder", "Alexander", "Jonas", 
         "Jonas", "Simon", "Victor", "Helena", "Hasse", "Alice", "Melanie", "Anna", "Mien", "Marthe",
         "Jary Sirin", "Babette", "Bastiaan", "Ides", "Ferit", "Camu", "Michiel", "Ro", "Jelena",
         "Thomas", "Mano", "Agon", "Arthur", "Arne", "Julien", "Sunny","Marthe", "Zahidullah", 
         "Jitske", "Jules", "Sieben", "Nikolay"]
# generate test data
ntests= 20
cases = [["Cédric", "Luiz", "Ward", "Briek", "Miel"], ["Babette","Nikolay"], ["Daan"]]
while len(cases) < ntests:
    n = random.randint(1,len(names))
    test = list(random.choices(names, k = n))
    cases.append(test)
    
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
    expression_name = f"verwissel( {test} )"
    result = module.verwissel( test )

    print(result)
    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)

write_yaml(yamldata)
