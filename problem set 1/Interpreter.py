def main():
    expression = input("Enter an arithmetic expression (x y z): ")
    x, y, z = expression.split()

    x = float(x)
    z = float(z)

    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        result = x / z
    else:
        print("Invalid operator")
        return

    print(f"{result:.1f}")

main()