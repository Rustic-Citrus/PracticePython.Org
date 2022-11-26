with open('happynumbers.txt', 'r') as file_one:
    lines_one = file_one.readlines()

with open('primenumbers.txt', 'r') as file_two:
    lines_two = file_two.readlines()
    
happy_numbers = [int(line.strip('\n!')) for line in lines_one]
prime_numbers = [int(line.strip('\n!')) for line in lines_two]
list_overlap = [n for n in prime_numbers if n in happy_numbers]
print(list_overlap)
