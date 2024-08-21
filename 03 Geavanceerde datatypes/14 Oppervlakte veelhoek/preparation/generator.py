import os
import importlib.util
import random
import ruamel.yaml
import math

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
def generate_convex_polygon(n):
    # Algorithm of Pavel Valtr: “Probability that n random points are in convex position.”
    # Not the best implementation
    x = [random.randint(-10,10) for _ in range(n)]
    y = [random.randint(-10,10) for _ in range(n)]
    minx, maxx = min(x), max(x)
    miny, maxy = min(y), max(y)
    x.sort()
    y.sort()

    del x[n-1]
    del x[0]
    del y[n-1]
    del y[0]
    
    perm = list(range(len(x)))
    random.shuffle(perm)
    split = random.randint(1, n - 3)
    x1, x2 = [minx], [minx]
    y1, y2 = [miny], [miny]

    for i in range(len(x)):
        j = perm[i]
        if i < split:
            x1.append(x[j])
            y1.append(y[j])
        else:
            x2.append(x[j])
            y2.append(y[j])
    x1.append(maxx)
    x2.append(maxx)
    y1.append(maxy)
    y2.append(maxy)

    xvec = []
    yvec = []

    for i in range(len(x1)-1):
        xvec.append(x1[i + 1] - x1[i])
        yvec.append(y1[i + 1] - y1[i])
    for i in range(len(x2)-1):
        xvec.append(x2[i] - x2[i+1])
        yvec.append(y2[i] - y2[i+1])

    random.shuffle(xvec)
    random.shuffle(yvec)    

    vecs = []
    for i in range(len(xvec)):
        vecs.append( (xvec[i], yvec[i]))   
    
    vecs = sorted(vecs, key = lambda x: math.atan2(x[1], x[0]))
    xn = [0]
    yn = [0]
    for i in range(len(vecs)-1):
        co = vecs[i]
        xn.append(xn[i] + co[0])
        yn.append(yn[i] + co[1])
        
    return (xn, yn)


ntests= 20
cases = [([0, 3, 0], [0, 0, 2]), ([0, 2, 2, 0], [0, 0, 2, 2]) ]
while len(cases) < ntests:
    e = random.randint(0,2)
    n = random.randint(10**e,10**(e+1))
    n = max(n, 4)
    poly = generate_convex_polygon(n)
        
    if poly not in cases:
        cases.append(poly)

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
    x,y = cases[i]
    yamldata[0]['contexts'].append( {'testcases' : []})
        
    # generate test expression
    #
    expression_name = f"oppervlakte_veelhoek({x}, {y})"
    result = module.oppervlakte_veelhoek(x, y)

    print(result)
    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)

write_yaml(yamldata)
