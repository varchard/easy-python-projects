def collatz_conjecture(number):
    work_num = number
    counter = 0
    while work_num > 1:
        if work_num % 2 == 0:
            work_num /= 2
            counter += 1
        else:
            work_num = (work_num*3) + 1
            counter += 1
    return f'It took {counter} steps to go from {number} to one'
num_to_check = ''
while type(num_to_check)!= int:
    try:
        num_to_check = int(input(
                        "What number would you like to count the number of steps to one with the Collatz algorithm? "))
    except ValueError:
        print("Please pass an integer")
print(collatz_conjecture(num_to_check))