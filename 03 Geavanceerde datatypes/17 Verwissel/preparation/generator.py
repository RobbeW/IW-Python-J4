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

fruitsoorten = [
    "appel", "banaan", "peer", "sinaasappel", "kiwi", "mango", "ananas", "druif", "watermeloen", "kers",
    "citroen", "limoen", "mandarijn", "nectarine", "perzik", "pruim", "abrikoos", "granaatappel", "papaja", "passievrucht",
    "guave", "lychee", "ramboetan", "jackfruit", "durian", "cactusvijg", "cranberry", "bosbes", "aardbei", "framboos",
    "braam", "veenbes", "zwarte bes", "rode bes", "witte bes", "loganbes", "moerbei", "tamarillo", "kaki", "physalis",
    "kokosnoot", "lansat", "longan", "sapodilla", "carambola", "salak", "santol", "zuurzak", "cherimoya", "quandong",
    "ugli", "yuzu", "pomelo", "calamondin", "kumquat", "jambolan", "loquat", "mispel", "feijoa", "bael",
    "ackee", "bilimbi", "boeddhistische hand", "canistel", "chico", "cloudberry", "krent", "damson", "vlierbes", "goji bes",
    "honingbes", "huckleberry", "jabuticaba", "langsat", "lucuma", "mamoncillo", "maracuja", "mirabelle", "monstera", "nangka",
    "olijf", "osage oranje", "persimmon", "pitahaya", "rambutan", "rozenappel", "lijsterbes", "safou", "serviceberry", "sleedoorn",
    "surinaamse kers", "tamarinde", "witte sapote", "bosaardbei", "youngberry", "jujube", "zwarte sapote", "bananenpassievrucht", "ijsappel"
]

# generate test data
ntests= 20
cases = [(["appel", "banaan", "peer", "citroen", "druif"], 1, 3),
         (["appel", "banaan", "peer", "citroen", "druif"], 3, 1),
         (["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "z"], 5, 5)]


while len(cases) < ntests:
    keuze = random.randint(0, 2)
    if keuze == 0:
        lijst = random.sample(fruitsoorten, k = random.randint(1, len(fruitsoorten)))
    elif keuze == 1:
        lijst = [ random.randint(-10, 10) for _ in range(random.randint(1,100))]
    else:
        lijst = random.choices("abcdefghijklmnopqrstuvwxyz", k = random.randint(1,100))
    
    num1 = random.randint(1, len(lijst))
    num2 = random.randint(1, len(lijst))
    
    case = (lijst, num1, num2)
    
    if case not in cases:
        cases.append(case)

cases = sorted(cases, key = lambda x : len(x[0]))

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
    expression_name = f"verwissel({test[0]}, {test[1]}, {test[2]})"
    result = module.verwissel(test[0], test[1], test[2])
    
    print(result)
    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)

write_yaml(yamldata)
