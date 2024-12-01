from datetime import datetime  # Importing datetime module to get the current year

try:
    # Get the current year using datetime
    current_year = datetime.now().year  
    
    # Taking user input for name and year of birth, stripping leading/trailing spaces
    name = input("Enter your name").strip()  
    
    # Taking user input for year of birth and stripping any extra spaces
    year_born = input("Enter your year of birth").strip()  
    
    # Check if the name is empty, raise ValueError if it is
    if not name:
        raise ValueError("Name can not be empty")
    
    # Check if the year of birth contains only digits, raise ValueError if not
    if not year_born.isdigit():
        raise ValueError("Year of birth must be a digit")
    
    # Check if the year of birth is not greater than the current year
    if int(year_born) > current_year:
        raise ValueError("Year of birth can not be greater than current year")
    
    # Calculate age and display the result
    print(f"Hello {name} you are {current_year - int(year_born)} years old")

# Handle both ValueError and TypeError exceptions, displaying error message
except (ValueError, TypeError) as e:
    print(f"Input Error: {e}")

# Catch any other exceptions not caught by the above blocks
except Exception as e:
    print(f"An error occurred: {e}")
