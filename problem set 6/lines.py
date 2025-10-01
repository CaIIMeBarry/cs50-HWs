import sys

def main():
   
    check_command_line_args()

    try:
        file_path = sys.argv[1]
        line_count = 0
        with open(file_path, "r") as file:
            for line in file:
                # A line is considered a line of code if it's not blank
                # and doesn't start with a # (after stripping leading whitespace).
                if is_code_line(line):
                    line_count += 1
        print(line_count)

    except FileNotFoundError:
        sys.exit("File does not exist")

def check_command_line_args():
    
    # Check for the number of arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Check for the file extension
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

def is_code_line(line):
    
    # Remove leading and trailing whitespace from the line
    stripped_line = line.strip()

    # A line is not code if it is empty or starts with a comment hash
    if not stripped_line or stripped_line.startswith("#"):
        return False

    return True

if __name__ == "__main__":
    main()
