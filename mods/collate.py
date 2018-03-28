import os

output_name = 'mod-list.txt'
output = open(output_name, 'w', encoding='utf-8')

for entry in os.walk('.'):
    for file in entry[2]:
        if file != output_name and file != 'collate.py':
            output.write(file + '\n')

output.close()
