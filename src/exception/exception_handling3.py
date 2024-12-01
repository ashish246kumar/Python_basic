#demonstrated the usage of try except else and finally
try:
    # Get input from the user for the numerator and denominator
    numerator = int(input("Enter numerator"))  # Convert input to integer
    denominator = int(input("Enter denominator"))  # Convert input to integer
    
    # Perform division operation
    result = numerator / denominator  # Division might cause ZeroDivisionError

except ZeroDivisionError:
    # Handle the case where denominator is zero
    print("Denominator cannot be zero")

except ValueError:
    # Handle the case where input is not a valid number
    print("Invalid input. Please enter a number")

else:
    # If no exceptions occur, print the result of the division
    print(result)

finally:
    # This block will execute no matter what, whether an exception occurred or not
    print("Program executed successfully")
