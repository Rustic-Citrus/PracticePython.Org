import random

def get_max(var1, var2, var3):
    """Determines which of the three integer arguments is the largest, 
then returns the largest integer."""
    nums = [var1, var2, var3]
    largest_num = var1
    for n in range(len(nums)):
        if nums[n] > largest_num:
            largest_num = nums[n]
    
    return largest_num

def get_three_random_nums():
    """Generates three random numbers between 0 and 1,000,000 and 
then returns them."""
    num1, num2, num3 = [random.randint(0, 1000000) for n in range(0, 3)]
    return num1, num2, num3

print('Generating three random numbers between 0 and 1,000,000: ')
num1, num2, num3 = get_three_random_nums()
print(num1)
print(num2)
print(num3)
print(f'The largest of the three numbers was {get_max(num1, num2, num3)}.')
