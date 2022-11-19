repeat = True
end = 'Ending program...'
def eviscerate_list(x):
    y = []
    x = x.split(',')
    x = [i.strip() for i in x]
    y = [x[0], x[-1]]
    return x, y

while repeat == True:
    user_input = input('Type or paste a list in the format x, y, z..., \
using commas to separate items: ')
    user_input, eviscerated_list = eviscerate_list(user_input)
    print(f'ORIGINAL LIST: {user_input}')
    print(f'FIRST AND LAST ITEMS ONLY: {eviscerated_list}')
    user_decision = input('Press Y to try on another list: ')
    if user_decision.lower() != 'y':
        print(end)
        repeat = False
