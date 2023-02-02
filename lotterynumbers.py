#Programming Exercise 7-2

import random

def main():
     # Create a list.
    numbers = [0] * 7

    # Populate the list with random numbers.
    for index in range(7):
        numbers[index] = random.randint(0, 56)

    # Display the random numbers.
    print('Here are your lottery numbers:')
    for index in range(7):
        print (numbers[index], end='')

        # Separate current number from next number with commas.
        if index != 6:  
            print (", " , end='')

# Call the main function.
main()