def chatbot():
    print("=" * 40)
    print("       WELCOME TO PYTHON CHATBOT")
    print("=" * 40)
    print("Hello! I am your chatbot.")
    print("Type 'bye' to exit the conversation.")
    print()

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hi! Nice to meet you!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! How about you?")

        elif user_input == "what is your name":
            print("Bot: I am a Python chatbot.")

        elif user_input == "help":
            print("Bot: You can say hello, ask how I am, or say bye.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day!")
            break

        else:
            print("Bot: Sorry, I don't understand that message.")

        print()


if __name__ == "__main__":
    chatbot()