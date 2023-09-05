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
cases = [("Donna", "De Saeger", 2277.16, 25), 
         ("Julius", "Caesar", 4213.14, 56),
         ("Thomas", "Mertens", 3450, 42),
         ("Nelle", "Vanlangendonck", 3020, 64)]

tab_name = 'Feedback'
settings = f'''
tab name: {tab_name}
python input without prompt: true
block count: multi
input block size: {len(cases[0])}
output block size: ends with
comparison: exact match
'''

# generate test data
ntests= 1
while len(cases) < ntests:
    cases.append( (random.randint(0,9999),) )

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
