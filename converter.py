import argparse  # Importing argparse to handle command-line arguments

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    # Create ArgumentParser object with a description
    parser = argparse.ArgumentParser(
        description='Convert temperatures between Celsius and Fahrenheit.'
    )
    
    # Create a mutually exclusive group: user must provide either --c2f or --f2c, not both
    group = parser.add_mutually_exclusive_group(required=True)
    
    # Add argument to convert Celsius to Fahrenheit
    group.add_argument('--c2f', type=float, help='Convert Celsius to Fahrenheit. Provide Celsius value.')
    
    # Add argument to convert Fahrenheit to Celsius
    group.add_argument('--f2c', type=float, help='Convert Fahrenheit to Celsius. Provide Fahrenheit value.')

    # Parse the command-line arguments
    args = parser.parse_args()

    # If --c2f is provided
    if args.c2f is not None:
        result = celsius_to_fahrenheit(args.c2f)
        # Print the result in a readable format
        print(f"{args.c2f}°C is equal to {result:.2f}°F")
    
    # If --f2c is provided
    elif args.f2c is not None:
        result = fahrenheit_to_celsius(args.f2c)
        # Print the result in a readable format
        print(f"{args.f2c}°F is equal to {result:.2f}°C")

# Entry point of the script
if __name__ == '__main__':
    main()
