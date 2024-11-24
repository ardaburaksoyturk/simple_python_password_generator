import random
import string
import pyperclip  # For copying to clipboard

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.numbers = string.digits
        self.symbols = string.punctuation
        self.password_history = []

    def generate_password(self, length=12, use_upper=True, use_lower=True, 
                         use_numbers=True, use_symbols=True):
        """Generate a password with specified requirements"""
        try:
            # Start with empty character set
            characters = ''
            
            # Add chosen character types
            if use_lower:
                characters += self.lowercase
            if use_upper:
                characters += self.uppercase
            if use_numbers:
                characters += self.numbers
            if use_symbols:
                characters += self.symbols
                
            if not characters:
                return "Error: No character types selected!"

            # Generate password
            password = ''
            
            # Ensure at least one of each selected type
            if use_lower:
                password += random.choice(self.lowercase)
            if use_upper:
                password += random.choice(self.uppercase)
            if use_numbers:
                password += random.choice(self.numbers)
            if use_symbols:
                password += random.choice(self.symbols)
            
            # Fill remaining length with random characters
            remaining_length = length - len(password)
            if remaining_length > 0:
                password += ''.join(random.choice(characters) for _ in range(remaining_length))
            
            # Shuffle the password
            password_list = list(password)
            random.shuffle(password_list)
            final_password = ''.join(password_list)
            
            # Add to history
            self.password_history.append(final_password)
            
            return final_password
            
        except Exception as e:
            return f"Error generating password: {e}"

    def check_strength(self, password):
        """Check password strength"""
        strength = 0
        reasons = []
        
        if len(password) >= 12:
            strength += 1
            reasons.append("Good length")
        if any(c in self.uppercase for c in password):
            strength += 1
            reasons.append("Has uppercase")
        if any(c in self.lowercase for c in password):
            strength += 1
            reasons.append("Has lowercase")
        if any(c in self.numbers for c in password):
            strength += 1
            reasons.append("Has numbers")
        if any(c in self.symbols for c in password):
            strength += 1
            reasons.append("Has symbols")
            
        return strength, reasons

def main():
    generator = PasswordGenerator()
    
    while True:
        print("\nPassword Generator Menu:")
        print("1. Generate password with default settings")
        print("2. Generate custom password")
        print("3. Check password strength")
        print("4. View password history")
        print("5. Exit")
        
        choice = input("\nChoose an option: ")
        
        try:
            if choice == '1':
                # Generate default password
                password = generator.generate_password()
                print(f"\nGenerated Password: {password}")
                pyperclip.copy(password)
                print("(Password copied to clipboard!)")
                
            elif choice == '2':
                # Get custom requirements
                length = int(input("Password length (8-50): "))
                if length < 8 or length > 50:
                    print("Length must be between 8 and 50!")
                    continue
                    
                use_upper = input("Include uppercase? (y/n): ").lower() == 'y'
                use_lower = input("Include lowercase? (y/n): ").lower() == 'y'
                use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
                use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
                
                if not any([use_upper, use_lower, use_numbers, use_symbols]):
                    print("Must select at least one character type!")
                    continue
                
                # Generate custom password
                password = generator.generate_password(
                    length, use_upper, use_lower, use_numbers, use_symbols
                )
                print(f"\nGenerated Password: {password}")
                pyperclip.copy(password)
                print("(Password copied to clipboard!)")
                
            elif choice == '3':
                password = input("Enter password to check: ")
                strength, reasons = generator.check_strength(password)
                print(f"\nPassword Strength: {strength}/5")
                print("Reasons:", ", ".join(reasons))
                
            elif choice == '4':
                if not generator.password_history:
                    print("\nNo passwords generated yet!")
                else:
                    print("\nPassword History:")
                    for i, pwd in enumerate(generator.password_history, 1):
                        print(f"{i}. {pwd}")
                
            elif choice == '5':
                print("Goodbye!")
                break
                
            else:
                print("Invalid choice! Please choose 1-5")
                
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
