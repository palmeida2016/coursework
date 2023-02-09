import csv
import re

files = ['TEST', 'FIT']

for myFile in files:
    with open(f'{myFile}.dat') as fin, open(f'{myFile}_numbers.arff', 'w') as fout:
        o = csv.writer(fout)
        for line in fin:
            count = int(re.search(r'\d+$',line)[0])
            if count < 2:
                line = re.sub(r'\d+$', 'nfp', line)
            else:
                line = re.sub(r'\d+$', 'fp', line)
            o.writerow(line.split())
