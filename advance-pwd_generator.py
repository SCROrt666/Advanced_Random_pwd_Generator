"""
Advanced Password Generator Pro
A professional-grade password generation tool with multiple modes and features
Author: Tharaka_N_Weerasooriya
GitHub: https://github.com/SCROrt666
"""
try:
    
    import random
    import string
    
    print("=== Advanced Random Password Generator ===\n")
    
    try:
        # Get password requirements from user
        length = int(input("Enter password length (minimum 4): "))
    
        # Validate length
        if length < 4:
            print("Password length must be at least 4 characters!")
        else:
            # Ask for password options
            use_uppercase = input("Include uppercase letters? (y/n): ").lower()
            use_lowercase = input("Include lowercase letters? (y/n): ").lower()
            use_digits = input("Include numbers? (y/n): ").lower()
            use_symbols = input("Include symbols? (y/n): ").lower()
            
            # Build character pool based on user choices
            characters = ""
            
            if use_uppercase == 'y':
                characters += string.ascii_uppercase  # A-Z
            
            if use_lowercase == 'y':
                characters += string.ascii_lowercase  # a-z
            
            if use_digits == 'y':
                characters += string.digits  # 0-9
            
            if use_symbols == 'y':
                characters += string.punctuation  # !@#$%^&*()
            
            # Check if at least one option was selected
            if characters == "":
                print("\nError: You must select at least one character type!")
            else:
                # Generate password
                password = ""
                
                for i in range(length):
                    random_char = random.choice(characters)
                    password += random_char
                
                # Display the generated password
                print("\n" + "="*40)
                print("Your generated password is:")
                print(password)
                print("="*40)
                
                # Show password strength
                strength = ""
                if length >= 12 and use_uppercase == 'y' and use_lowercase == 'y' and use_digits == 'y' and use_symbols == 'y':
                    strength = "Very Strong 💪"
                elif length >= 8 and (use_uppercase == 'y' or use_lowercase == 'y') and use_digits == 'y':
                    strength = "Strong 👍"
                elif length >= 6:
                    strength = "Medium ⚠️"
                else:
                    strength = "Weak ❌"
                
                print(f"Password Strength: {strength}")
    
    except ValueError:
        print("\nError: Please enter a valid number for password length!")
except ValueError:
    print("Invalid input! Please enter numeric values for length.")
