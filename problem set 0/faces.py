def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    user_input = input("Enter some text: ")
    converted_text = convert(user_input)
    print(converted_text)

main()
                                              
                                          