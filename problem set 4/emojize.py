import emoji

def main():
  
    user_input = input("Input: ")

    emojized_string = emoji.emojize(user_input, language='alias')

    print(emojized_string)

if __name__ == "__main__":
    main()
