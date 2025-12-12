# 1. Import the regular expression module
import re

def check_length(password):
    # Check 1: Minimum length of 8 characters
    # Returns True if the length is 8 or more.
    return len(password) >= 8

def check_uppercase(password):
    # Check 2: Presence of at least one uppercase letter (A-Z)
    # The pattern r'[A-Z]' searches for any character in that range.
    # re.search returns a match object (True) or None (False).
    return bool(re.search(r'[A-Z]', password))

def check_lowercase(password):
    # Check 3: Presence of at least one lowercase letter (a-z)
    return bool(re.search(r'[a-z]', password))

def check_digit(password):
    # Check 4: Presence of at least one digit (0-9)
    # The pattern r'\d' is a shorthand for [0-9].
    return bool(re.search(r'\d', password))

def check_special_char(password):
    # Check 5: Presence of at least one special character
    # The pattern r'[^a-zA-Z0-9\s]' looks for any character 
    # that is NOT a letter, NOT a number, and NOT whitespace.
    return bool(re.search(r'[^a-zA-Z0-9\s]', password))


# --- Next Micro Problem will integrate these checks ---

def check_password_strength(password):
    # This list stores criteria the password FAILS
    missing_criteria = []
    
    if not check_length(password):
        missing_criteria.append("Minimum length of 8 characters.")
        
    if not check_uppercase(password):
        missing_criteria.append("At least one uppercase letter (A-Z).")
        
    if not check_lowercase(password):
        missing_criteria.append("At least one lowercase letter (a-z).")
        
    if not check_digit(password):
        missing_criteria.append("At least one digit (0-9).")
        
    if not check_special_char(password):
        missing_criteria.append("At least one special character (e.g., !@#$%^&*).")
        
    
    # Evaluate and print results
    if not missing_criteria:
        print("\n---------------------------------")
        print("Strength: STRONG")
        print("Your password meets all security requirements.")
        print("---------------------------------")
    else:
        print("\n---------------------------------")
        print("Strength: WEAK")
        print("Your password fails the following security checks:")
        
        # Print the missing requirements
        for criterion in missing_criteria:
            print(f"- {criterion}")
            
        print("---------------------------------")

# --- Next step is the user interface ---

# --- User Interaction Code (Main Program) ---
def main():
    print("\n--- Prodigy InfoTech Task 03: Password Complexity Checker ---")
    
    # Get the password from the user
    password = input("Enter the password you want to check: ")
    
    # Run the strength check
    check_password_strength(password)

# Run the main function when the script executes
if __name__ == "__main__":
    main()