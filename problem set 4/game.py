import random
import sys

def main():


    while True:
        try:
            level_str = input("Level: ")
            level = int(level_str)
            if level > 0:
                break
        except ValueError:
            pass
    target_number = random.randint(1, level)

    # Loop to get a valid guess from the user
    while True:
        try:
            guess_str = input("Guess: ")
            guess = int(guess_str)
            if guess <= 0:
                continue
            if guess < target_number:
                print("Too small!")
            elif guess > target_number:
                print("Too large!")
            else:
                print("Just right!")
                break

        except ValueError:
            pass


if __name__ == "__main__":
    main()
