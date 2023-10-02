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
input block size: 5
output block size: ends with
comparison: exact match
'''

# generate test data
cases = [("printerinkt", 0.015, 920, 50, 0.029)]
surface_tension = [("ethanol", 0.012, 790, 0.02255),
                   ("methanol", 0.00545, 791.4, 0.0226),
                   ("aceton", 0.00306, 790, 0.0233),
                   ("glycerol", 1.412, 1261.3, 0.0634),
                   ("water", 0.001, 999.972, 0.07275),
                   ("kwik", 0.016, 13596, 0.473)]
for surface in surface_tension:
    d = random.randint(3,10) * 10
    matter = surface[0]
    neta = surface[1]
    rho = surface[2]
    sigma = surface[3]
    cases.append( (matter, neta, rho, d, sigma) )
    

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
            print(line, file=outfile)

    # add stdout to output file
    # print(stdout, file=outfile, end='')

# add settings to output file
print('-' * 41 + settings, file=outfile, end='')
