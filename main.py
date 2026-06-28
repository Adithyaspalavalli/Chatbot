from intents import intents


print("Bot: Hello! I am your assistant")


while True:

    user = input("You: ").lower()


    if any(word in user for word in intents["greeting"]):

        print("Bot: Hi, how can I help you?")


    elif any(word in user for word in intents["account_opening"]):

        print(
        "Bot: We have Savings Account, Fixed Deposit, Recurring Deposit and Current Account"
        )


    elif any(word in user for word in intents["account_recommendation"]):

        print(
        "Bot: It depends on your need. For daily use choose Savings Account, for investment choose FD/RD."
        )


    elif any(word in user for word in intents["goodbye"]):

        print("Bot: Goodbye!")
        break


    else:

        print("Bot: Sorry, I don't understand. Can you explain?")