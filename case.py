def main(): #Main function for 
    try:
        user_choice = input('Choose Converter: | 1 for camelCase to snake_case | 2 for snake_case to camelCase | ')  # Choosing which converter

        # Converter for camelCase to snake_case
        if user_choice == '1':
            camel_input = input('Enter camelCase: ')
            snake_output = camel_to_snake(camel_input)  # Calls the function to convert to snake_case
            print('Converted to snake_case:', snake_output)  # Shows final converted output

        # Converter for snake_case to camelCase
        elif user_choice == '2':
            snake_input = input('Enter snake_case: ')
            camel_output = snake_to_camel(snake_input)  # Calls the function to convert to camelCase
            print('Converted to camelCase:', camel_output) # Shows final converted output

        else:
            raise ValueError('Invalid choice. Please enter 1 or 2.')  # Raise error for invalid input

    except ValueError as val_error:
        print(f'Error: {val_error}')  # Catches the error and stores


def camel_to_snake(camel_input): # Function to convert camelCase to snake_case
    
    snake = ''
    for char in camel_input:
        if char.islower():
            snake += char  # If character is lowercase, append it to snake
        elif char.isupper():
            snake += '_' + char.lower()  # If character is uppercase, adds underscore in front and turns character lowercase
        else:
            raise ValueError('Invalid character in camelCase input. Only letters are allowed.')  # Raise error for invalid characters
    return snake


def snake_to_camel(snake_input): #Function to convert snake_case to camelCase
    """Convert snake_case to camelCase."""
    camel = ''
    skip_underscore = False  # Used as a flag for an underscore
    for char in snake_input:
        if char == '_':
            skip_underscore = True  # If an underscore is detected, raise the flag to skip it and not append it into camel
            continue
        if not char.islower() and not char.isupper() and char != '_':
            raise ValueError('Invalid character in snake_case input. Only letters and underscores are allowed.')  # Raises error for invalid characters
        if skip_underscore:  # If the flag is raised, uppercase the character that follows
            camel += char.upper()
            skip_underscore = False  # Resets the flag and loops
        else:
            camel += char  # If lowercase, just adds character as it is
    return camel


# Call the main function to run the converter
if __name__ == '__main__':
    main()
