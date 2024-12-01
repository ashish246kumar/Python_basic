from datetime import datetime  # Importing the datetime module to get the current year

try:
    # Getting the current year using datetime.now().year
    current_year = datetime.now().year  
    
    # Taking user input for name
    name = input('Enter your name')  
    
    # Taking user input for year of birth and converting it to integer
    year_born = input('Enter your age')  
    
    # Calculating age by subtracting year_born from current_year
    age = current_year - int(year_born)  # Convert year_born to integer
    
    # Printing the name and calculated age
    print(f"Hello {name}! your age is approximately {age}")

# Handling TypeError when an operation or function is applied to an object of inappropriate type
except TypeError:
    print("Type Error Occurred")    

# Handling ValueError when a function receives an argument of the right type but inappropriate value
except ValueError:
    print("Value Error Occurred")

# Generic exception handler to catch any other errors not handled above
except Exception as e:
    print(f"An error occurred: {e}")
