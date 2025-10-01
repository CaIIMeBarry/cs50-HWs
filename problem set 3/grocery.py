def main():
    grocery_items = {}
    while True:
        try:
            item = input("")
            
            if item in grocery_items:
                grocery_items[item] += 1
            else:
                grocery_items[item] = 1
        except EOFError:
            break

    sorted_items = sorted(grocery_items.keys())
    for item in sorted_items:
        count = grocery_items[item]
        item_upper = item.upper()
        print(f"{count} {item_upper}")


main()