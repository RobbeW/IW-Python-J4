import math
import os
import random
import subprocess
from typing import Text

# set fixed seed for generating test cases
random.seed(123456789)

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join('..', 'solution')
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

# configuration settings
tab_name = 'Feedback'
settings = f'''
tab name: {tab_name}
python input without prompt: true
block count: multi
input block size: 4
output block size: ends with
comparison: exact match
'''

# generate test data
ntests= 20
cases = [(7,4,7,19),(10,7,23,21),]
while len(cases) < ntests:
    vertrek = random.randint(0,23)
    aankomst = random.randint(0,23)
    verschil = aankomst - vertrek
    if verschil >= 0:
        z = random.randint(1, verschil )
        u = abs(verschil-z-1)
    else:
        z = random.randint(1,(24-vertrek+aankomst))
        u = abs(verschil-z-1)
    
    if u <=17 and z < 10:
        cases.append( (u, z, vertrek, aankomst ) )

# configure test files
infile = open(os.path.join(evaldir, '0.in'), 'w')
outfile = open(os.path.join(evaldir, '0.out'), 'w')

# generate unit tests
for stdin in cases:

    # add input to input file
    stdin = '\n'.join(f'{line}' for line in stdin)
    print(stdin, file=infile)

    # generate output to output file
    script = os.path.join(solutiondir, 'solution.nl.py')
    process= subprocess.run(
        ['python3', script],
        input=stdin,
        encoding='utf-8',
        capture_output=True
    )
    
    result_lines = process.stdout.split("\n")
    for line in result_lines:
        if not(line.startswith( 'Geef' )):
            print(line)
            print(line, file=outfile, end='\n')

    # add stdout to output file
    # print(stdout, file=outfile, end='')

# add settings to output file
print('-' * 41 + settings, file=outfile, end='')
