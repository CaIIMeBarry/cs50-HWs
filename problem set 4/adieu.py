import inflect
import sys

def main():


    p = inflect.engine()


    names = []


    while True:
        try:
            # Prompt the user for a name.
            name = input()
            # Add the entered name to our list
            names.append(name)
        except EOFError:

            break # Exit the loop.


    if names:

        formatted_names = p.join(names)


        print(f"Adieu, adieu, to {formatted_names}")

import inflect
import sys

def main():
    """
    Main function to run the adieu program.
    It prompts the user for names, one per line, until EOF (control-d) is received.
    Then, it prints a farewell message including all the names, correctly formatted.
    """
    # Initialize the inflect engine to help with joining words
    p = inflect.engine()

    # Create an empty list to store the names entered by the user
    names = []

    # Start an infinite loop to continuously ask for names
    while True:
        try:
            # Prompt the user for a name.
            name = input()
            # Add the entered name to our list
            names.append(name)
        except EOFError:
            # The user has pressed control-d, signaling the end of input.
            # This raises an EOFError (End-of-File Error).
            # The extra print() statement was removed from here.
            break # Exit the loop.

    # Check if at least one name was entered
    if names:
        # Use the inflect engine's join() method to format the list of names
        # into a grammatically correct string.
        # e.g., ["Liesl"] -> "Liesl"
        # e.g., ["Liesl", "Friedrich"] -> "Liesl and Friedrich"
        # e.g., ["Liesl", "Friedrich", "Louisa"] -> "Liesl, Friedrich, and Louisa"
        formatted_names = p.join(names)

        # Print the final farewell message.
        print(f"Adieu, adieu, to {formatted_names}")


if __name__ == "__main__":
    main()
