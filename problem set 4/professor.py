import random

def main():
    """
    Main function to run the Little Professor math game.
    It sets the level, generates 10 math problems, tracks the user's score,
    and provides feedback based on their answers.
    """
    # Get the difficulty level from the user.
    level = get_level()
    score = 0

    # Generate and pose 10 math problems.
    for _ in range(10):
        # Keep track of incorrect attempts for the current problem.
        tries = 0
        # Generate two random numbers based on the selected level.
        x = generate_integer(level)
        y = generate_integer(level)

        # Allow the user up to 3 tries to answer correctly.
        while tries < 3:
            try:
                # Display the problem and get the user's answer.
                answer = int(input(f"{x} + {y} = "))
                
                # Check if the answer is correct.
                if answer == x + y:
                    score += 1
                    break  # Correct answer, move to the next problem.
                else:
                    tries += 1
                    print("EEE")

            except ValueError:
                # Handle cases where the input is not an integer.
                tries += 1
                print("EEE")
        
        # If the user failed to answer correctly after 3 tries, show the solution.
        if tries == 3:
            print(f"{x} + {y} = {x + y}")

    # After 10 problems, display the final score.
    print(f"Score: {score}")


def get_level():
    """
    Prompts the user for a difficulty level (1, 2, or 3) and returns it.
    Will re-prompt until a valid input is received.
    """
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            # Catches non-integer inputs. The loop will continue.
            pass


def generate_integer(level):
    """
    Generates and returns a random non-negative integer with 'level' digits.
    Args:
        level (int): The number of digits the integer should have (1, 2, or 3).
    Returns:
        int: A randomly generated integer.
    Raises:
        ValueError: If the level is not 1, 2, or 3.
    """
    if level == 1:
        # 1-digit numbers are from 0 to 9.
        return random.randint(0, 9)
    elif level == 2:
        # 2-digit numbers are from 10 to 99.
        return random.randint(10, 99)
    elif level == 3:
        # 3-digit numbers are from 100 to 999.
        return random.randint(100, 999)
    else:
        # Raise an error for invalid levels, as per the specification.
        raise ValueError


if __name__ == "__main__":
    main()
