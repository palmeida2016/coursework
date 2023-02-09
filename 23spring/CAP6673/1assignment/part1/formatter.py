import csv

files = ['TEST', 'FIT']

for myFile in files:
    with open(f'{myFile}.dat') as fin, open(f'{myFile}.arff', 'w') as fout:
        o = csv.writer(fout)
        for line in fin:
            o.writerow(line.split())
