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
cases = [(1990,2,1,997), (2003,1,25,224)]
while len(cases) < ntests:
    jaar = random.randint(1980,2023)
    maand = random.randint(1,12)
    dag = random.randint(1,31)
    dagteller = random.randint(0,999)
    if not (maand == 11 and dag == 31):
        cases.append( (jaar, maand, dag, dagteller) )

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
        capture_output=True,
        text=True
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