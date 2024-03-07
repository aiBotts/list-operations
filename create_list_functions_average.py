# Create a list called numbers
numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

# Create a valid numbers list
valid_numbers = []

# Create a main function for the program
def main():
    # Call the list1 function
    list1()
    # Call the sum_of_valid function
    sum_of_valid()

# Create the list for the valid numbers
def list1():
    # Creating the loop for my valid_numbers list
    for number in numbers:
        # Getting the valid numbers from the numbers list
        if number >= 0 and number <= 101:
            # Copying the correct numbers to the valid_numbers list
            valid_numbers.append(number)
    # Displaying the valid numbers list
    print(valid_numbers)

# Creating an average of the valid_numbers
def sum_of_valid():
    # Create a total score variable
    total_score = 0
    # Run a loop to get the sum of the valid_numbers
    for num in valid_numbers:
        # Adding up the valid_numbers
        total_score = total_score + num
    # Displaying the total of the valid_numbers
    print("Total: ", total_score)
    # Displaying the average for the valid_numbers
    print("Average: ", total_score / len(valid_numbers))

# Call the main function
main()