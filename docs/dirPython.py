import os

for line in open('docs\slider.txt'):
    if line[0] == '*':
        os.makedirs("docs\\" + line.split(' ')[1])
        continue
    if line[2] == '-':
        print(line)
    break