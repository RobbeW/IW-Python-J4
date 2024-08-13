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
ntests = 20
voornamen = [
    "Emma", "Liam", "Lucas", "Olivia", "Milan", "Marie", "Noah", "Elise",
    "Arthur", "Louise", "Jules", "Lina", "Louis", "Alice", "Noé", "Camille",
    "Vince", "Anna", "Hugo", "Léa", "Jasper", "Nina", "Max", "Lotte",
    "Finn", "Laura", "Sam", "Eva", "Victor", "Fleur"
]
achternamen = [
    "Peeters", "Dubois", "Maes", "Jacobs", "Willems", "Mertens", "Claes", 
    "Goossens", "De Smet", "Lambert", "Coppens", "De Backer", "Verhoeven", 
    "Lemmens", "De Clercq", "Hendrickx", "Van Damme", "Smets", "Declercq", 
    "Van den Broeck", "Van Hove", "Desmet", "Michiels", "Vermeulen", 
    "Bogaert", "Vandenberghe", "Vandevelde", "Van Acker", "Stevens", "Leclercq"
]
# configuration settings
cases = [("Donna", "De Saeger", 2277.16, 25), 
         ("Julius", "Caesar", 4213.14, 56),
         ("Thomas", "Mertens", 3450, 42),
         ("Nelle", "Vanlangendonck", 3020, 64)]
while len(cases) < ntests:
    voornaam = random.choice(voornamen)
    naam = random.choice(achternamen)
    salaris = round(random.uniform(1800,3500), 2)
    age = random.randint(18,60)
    case = (voornaam, naam, salaris, age)
    if case not in cases:
        cases.append(case)

cases = sorted(cases, key= lambda x : x[3])

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
        if not(line.startswith( 'Geef' ) or line.startswith( 'Voer' )):
            print(line)
            outputtxt += line + "\n"
            
    testcase = { input: stdin, output: outputtxt }            
    yamldata[0]['contexts'][i]["testcases"].append( testcase)

write_yaml(yamldata)