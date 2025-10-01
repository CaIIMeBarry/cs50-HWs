def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    
    if not s[:2].isalpha():
        return False
    
    digit_seen = False
    for i, char in enumerate(s):
        if char.isdigit():
            if char == '0' and not digit_seen:
                return False
            digit_seen = True
        elif digit_seen:
            return False
    
    return True

main()
