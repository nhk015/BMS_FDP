"""
Program to check whether a number is prime or not.
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""
""" is prime"""

def is_prime(number):
    """
    Check if a given number is prime.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    # Handle numbers less than 2
    if number < 2:
        return False
    
    # 2 is the only even prime number
    if number == 2:
        return True
    
    # All other even numbers are not prime
    if number % 2 == 0:
        return False
    
    # Check odd divisors up to the square root of the number
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    
    return True


def main():
    """Main function to interact with user and check prime numbers."""
    print("=" * 50)
    print("Prime Number Checker")
    print("=" * 50)
    
    while True:
        try:
            # Get user input
            user_input = input("\nEnter a number to check if it's prime (or 'quit' to exit): ")
            
            # Check if user wants to exit
            if user_input.lower() == 'quit':
                print("Thank you for using Prime Number Checker. Goodbye!")
                break
            
            # Convert input to integer
            number = int(user_input)
            
            # Check if the number is prime
            if is_prime(number):
                print(f"✓ {number} is a PRIME number!")
            else:
                print(f"✗ {number} is NOT a prime number.")
                
        except ValueError:
            print("❌ Invalid input! Please enter a valid integer or 'quit' to exit.")


if __name__ == "__main__":
    main()
