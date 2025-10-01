def main():
    while True:
        try:
            fraction = input("Enter a fraction (X/Y): ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if x > y:
                continue
            if y == 0:
                continue

            percentage = round((x / y) * 100)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break

        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()