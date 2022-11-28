with open('Training_01.txt', 'r') as file:
    lines = file.readlines()

parsed_lines = []
for line in lines:
    line = line.strip('\n!')
    parsed_lines.append(line.split('/'))

for list in parsed_lines:
    list.remove('')

for list in parsed_lines:
    list[0] = ('folder', list[0])
    list[1] = ('category', list[1])
    if len(list) == 4:
        list[2] = ('subcategory', list[2])
        list[3] = ('filename', list[3])
    
    elif len(list) == 3:
        list.append(('filename', list[2]))
        list[2] = ('subcategory', None)

dictionary = {}
count = 0
for list in parsed_lines:
    dictionary[f'file_{count}'] = dict(list)
    count += 1

print(dictionary)
