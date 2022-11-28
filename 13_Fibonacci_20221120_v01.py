def get_fibonacci(n):
    """Generates a Fibonacci sequence of length n."""
    count = 0
    sequence = []
    while count <= (n - 1):
        if count <= 1:
            sequence.append(1)
        elif count > 1:
            sequence.append(sequence[count - 1] + sequence[count - 2])
        count += 1
    return sequence

repeat = True
while repeat == True:
    user_choice_one = int(input(
        'Type the desired length of your Fibonacci sequence: '))
    print(get_fibonacci(user_choice_one))
    user_choice_two = input('Press Y to generate another sequence. ')
    if user_choice_two.lower() != 'y':
        print('Ending program...')
        repeat = False
